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
        base_url = params.get_param('pos_whatsapp_receipt.openwa_base_url')
        api_key = params.get_param('pos_whatsapp_receipt.openwa_api_key')
        session_id = params.get_param('pos_whatsapp_receipt.openwa_session_id') or 'default'
        template = params.get_param('pos_whatsapp_receipt.openwa_message_template')

        if not base_url or not api_key:
            return {'success': False, 'error': 'OpenWA belum dikonfigurasi (Base URL dan API Key wajib diisi)'}

        web_base_url = params.get_param('web.base.url')
        long_url = f"{web_base_url}/pos/ticket/validate?access_token={order.access_token}"

        try:
            r = requests.get(f"https://tinyurl.com/api-create.php?url={long_url}", timeout=5)
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

        chat_id = f"{phone}@c.us"

        try:
            response = requests.post(
                f"{base_url.rstrip('/')}/api/sessions/{session_id}/messages/send-text",
                headers={'x-api-key': api_key, 'Content-Type': 'application/json'},
                json={'chatId': chat_id, 'text': message},
                timeout=10
            )
            if response.status_code in (200, 201):
                return {'success': True}
            else:
                result = response.json() if response.content else {}
                error_msg = result.get('message') or result.get('error') or f"HTTP {response.status_code}"
                _logger.error("OpenWA error: %s", result)
                return {'success': False, 'error': error_msg}
        except Exception as e:
            return {'success': False, 'error': str(e)}
