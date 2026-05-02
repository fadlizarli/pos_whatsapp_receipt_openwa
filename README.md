# POS WhatsApp Receipt for Odoo 17

![Odoo](https://img.shields.io/badge/Odoo-17.0-purple)
![License](https://img.shields.io/badge/License-LGPL--3-blue)
![WhatsApp](https://img.shields.io/badge/WhatsApp-Fonnte-green)

Module Odoo 17 untuk mengirim struk POS via WhatsApp menggunakan [Fonnte](https://fonnte.com) — layanan WhatsApp API lokal Indonesia.

---

## ✨ Fitur

- ✅ Kirim struk otomatis ke WhatsApp pelanggan setelah transaksi
- ✅ Tampilan struk lengkap: logo toko, kasir, item, metode pembayaran, kembalian
- ✅ Link struk bisa dibuka tanpa login (public access)
- ✅ Responsive di mobile
- ✅ Integrasi dengan Fonnte API (WhatsApp API lokal Indonesia)
- ✅ Template pesan yang bisa dikustomisasi
- ✅ Nomor WA otomatis diformat ke format internasional (08xxx → 628xxx)

---

## 🔧 Requirement

- Odoo 17.0
- Akun Fonnte ([fonnte.com](https://fonnte.com))
- Module Odoo: point_of_sale, website

---

## 📦 Instalasi

1. Download module:

cd /opt/odoo/custom-addons
git clone https://github.com/fadlizarli/pos_whatsapp_receipt.git

2. Tambahkan path di odoo.conf:

addons_path = /usr/lib/python3/dist-packages/odoo/addons,/opt/odoo/custom-addons

3. Restart Odoo:

sudo systemctl restart odoo

4. Install module:
- Masuk Odoo -> Apps -> Search "POS WhatsApp Receipt" -> Install

---

## ⚙️ Konfigurasi

Masuk ke Settings -> WhatsApp Receipt:

| Field | Keterangan |
|-------|-----------|
| API Token | Token dari akun Fonnte |
| Nomor Pengirim | Nomor WA terhubung ke Fonnte (628xxx) |
| Template Pesan | Template dengan variabel {total}, {date}, {receipt_url} |

Contoh template pesan:

Terima kasih telah berbelanja!

Total: {total}
Tanggal: {date}

Lihat struk lengkap:
{receipt_url}

Set base URL agar link struk menggunakan domain yang benar:

sudo -u odoo psql -d NAMA_DATABASE -c "UPDATE ir_config_parameter SET value='https://domain-kamu.com' WHERE key='web.base.url';"

---

## 🚀 Cara Pakai

1. Buka POS dan lakukan transaksi seperti biasa
2. Setelah payment, muncul kolom WhatsApp di halaman struk
3. Masukkan nomor WA pelanggan (format: 08xxx atau 628xxx)
4. Klik tombol hijau WA
5. Pelanggan menerima pesan WA dengan link struk lengkap
6. Link struk dapat dibuka tanpa perlu login ke Odoo

---

## 🛠️ Troubleshooting

**Link struk 404 / Not Found**
- Pastikan module sudah ter-install di database yang aktif
- Cek web.base.url sudah sesuai domain
- Pastikan dbfilter di odoo.conf tidak memblokir akses publik

**WA tidak terkirim**
- Cek token Fonnte di Settings
- Pastikan nomor pengirim aktif dan terhubung di Fonnte
- Cek log Odoo: sudo journalctl -u odoo -n 50

---

## 📁 Struktur Module

pos_whatsapp_receipt/
├── controllers/
│   └── main.py
├── models/
│   ├── pos_order.py
│   ├── res_config_settings.py
│   └── short_url.py
├── static/src/
│   ├── js/receipt_button.js
│   └── xml/receipt_button.xml
├── views/
│   ├── res_config_settings_views.xml
│   └── receipt_template.xml
├── __manifest__.py
└── README.md

---

## 📋 Changelog

### v17.0.1.0.0 (2026-04-30)
- Initial release
- Kirim struk via WhatsApp menggunakan Fonnte
- Halaman struk publik dengan tampilan responsive
- Konfigurasi template pesan

---

## 🤝 Kontribusi

1. Fork repo ini
2. Buat branch baru: git checkout -b fitur-baru
3. Commit: git commit -m 'Tambah fitur X'
4. Push: git push origin fitur-baru
5. Buat Pull Request

---

## 📄 Lisensi

LGPL-3

---

## 👨‍💻 Developer

Dibuat untuk kebutuhan bisnis ritel Indonesia.
Menggunakan Fonnte sebagai WhatsApp API gateway.

---

## 📞 Jasa Setup & Support

Butuh bantuan instalasi, konfigurasi, atau kustomisasi module ini? Kami menyediakan jasa setup profesional.

**Layanan:**
- ✅ Instalasi dan konfigurasi Odoo POS
- ✅ Setup module WhatsApp Receipt
- ✅ Kustomisasi template struk
- ✅ Training penggunaan sistem
- ✅ Support teknis

**Kontak:**
- 📧 Email: fadlizarli68@gmail.com
- 💬 WhatsApp: [+62 823-9711-4317](https://wa.me/6282397114317)

