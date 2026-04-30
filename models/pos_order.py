import requests
import logging
from odoo import models, api

_logger = logging.getLogger(__name__)

class PosOrder(models.Model):
    _inherit = 'pos.order'

    @api.model
    def send_whatsapp_receipt(self, order_id=None, phone_number=None):
        order = self.sudo().browse(order_id)
        if not order:
            return {'success': False, 'error': 'Order not found'}

        params = self.env['ir.config_parameter'].sudo()
        token = params.get_param('pos_whatsapp_receipt.fonnte_token')
        sender = params.get_param('pos_whatsapp_receipt.fonnte_sender')
        template = params.get_param('pos_whatsapp_receipt.fonnte_message_template')

        if not token:
            return {'success': False, 'error': 'Fonnte token belum dikonfigurasi'}

        base_url = params.get_param('web.base.url')
        long_url = f"{base_url}/pos/ticket/validate?access_token={order.access_token}"

        try:
            r = requests.get(f"https://tinyurl.com/api-create.php?url={long_url}", timeout=5)
            _logger.info("TinyURL: %s -> %s", long_url, r.text)
            receipt_url = r.text.strip() if r.status_code == 200 else long_url
        except Exception as e:
            _logger.error("TinyURL error: %s", str(e))
            receipt_url = long_url

        message = template.format(
            total=f"Rp {order.amount_total:,.0f}",
            date=order.date_order.strftime('%d/%m/%Y %H:%M'),
            receipt_url=receipt_url
        )

        phone = phone_number.strip().replace('+', '').replace('-', '').replace(' ', '')
        if phone.startswith('0'):
            phone = '62' + phone[1:]

        try:
            data = {'target': phone, 'message': message, 'countryCode': '62'}
            if sender:
                data['sender'] = sender.strip().replace('+', '')

            response = requests.post(
                'https://api.fonnte.com/send',
                headers={'Authorization': token},
                data=data,
                timeout=10
            )
            result = response.json()
            _logger.info("Fonnte result: %s", result)
            if result.get('status'):
                return {'success': True}
            else:
                return {'success': False, 'error': result.get('reason', 'Gagal kirim pesan')}
        except Exception as e:
            return {'success': False, 'error': str(e)}
