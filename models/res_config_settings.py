from odoo import fields, models

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    openwa_base_url = fields.Char(
        string='OpenWA Base URL',
        help='URL server OpenWA, contoh: http://localhost:2785',
        config_parameter='pos_whatsapp_receipt.openwa_base_url'
    )
    openwa_api_key = fields.Char(
        string='OpenWA API Key',
        help='API key dari OpenWA (buat di menu Auth > API Keys)',
        config_parameter='pos_whatsapp_receipt.openwa_api_key'
    )
    openwa_session_id = fields.Char(
        string='Session ID',
        help='ID sesi WhatsApp di OpenWA (contoh: default)',
        config_parameter='pos_whatsapp_receipt.openwa_session_id',
        default='default'
    )
    openwa_message_template = fields.Char(
        string='Template Pesan WhatsApp',
        help='Gunakan {total}, {date}, {receipt_url} sebagai variabel',
        config_parameter='pos_whatsapp_receipt.openwa_message_template',
        default="""Terima kasih telah berbelanja!

Total: {total}
Tanggal: {date}

Lihat resit lengkap:
{receipt_url}"""
    )
