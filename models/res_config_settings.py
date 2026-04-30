from odoo import fields, models

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    fonnte_token = fields.Char(
        string='Fonnte API Token',
        help='Token dari akun Fonnte (md.fonnte.com)',
        config_parameter='pos_whatsapp_receipt.fonnte_token'
    )
    fonnte_sender = fields.Char(
        string='Nomor WhatsApp Pengirim',
        help='Nomor WhatsApp yang terhubung ke Fonnte (format: 628xxx)',
        config_parameter='pos_whatsapp_receipt.fonnte_sender'
    )
    fonnte_message_template = fields.Char(
        string='Template Pesan WhatsApp',
        help='Gunakan {total}, {date}, {receipt_url} sebagai variabel',
        config_parameter='pos_whatsapp_receipt.fonnte_message_template',
        default="""Terima kasih telah berbelanja!

Total: {total}
Tanggal: {date}

Lihat resit lengkap:
{receipt_url}"""
    )
