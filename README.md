# POS WhatsApp Receipt for Odoo 17

![Odoo](https://img.shields.io/badge/Odoo-17.0-purple)
![License](https://img.shields.io/badge/License-LGPL--3-blue)
![WhatsApp](https://img.shields.io/badge/WhatsApp-OpenWA-green)

Module Odoo 17 untuk mengirim struk POS via WhatsApp menggunakan [OpenWA](https://github.com/fadlizarli/openwa) — WhatsApp API gateway open-source yang self-hosted.

---

## Fitur

- Kirim struk otomatis ke WhatsApp pelanggan setelah transaksi
- Tampilan struk lengkap: logo toko, kasir, item, metode pembayaran, kembalian
- Link struk bisa dibuka tanpa login (public access)
- Responsive di mobile
- Integrasi dengan OpenWA (self-hosted, gratis, open-source)
- Template pesan yang bisa dikustomisasi
- Nomor WA otomatis diformat ke format internasional (08xxx → 628xxx)

---

## Requirement

- Odoo 17.0
- OpenWA berjalan di server (lihat [panduan instalasi OpenWA](https://github.com/fadlizarli/openwa))
- Module Odoo: `point_of_sale`, `web`

---

## Instalasi

**1. Clone module ke addon path:**

```bash
cd /opt/odoo/custom-addons
git clone https://github.com/fadlizarli/pos_whatsapp_receipt_openwa.git pos_whatsapp_receipt
```

**2. Tambahkan path di `odoo.conf`:**

```ini
addons_path = /usr/lib/python3/dist-packages/odoo/addons,/opt/odoo/custom-addons
```

**3. Restart Odoo:**

```bash
sudo systemctl restart odoo
```

**4. Install module:**

Masuk Odoo → Apps → Search `POS WhatsApp Receipt` → Install

---

## Setup OpenWA

Sebelum mengkonfigurasi module ini, pastikan OpenWA sudah berjalan:

**1. Jalankan OpenWA via Docker:**

```bash
git clone https://github.com/fadlizarli/openwa.git
cd openwa
cp .env.minimal .env
docker compose up -d
```

**2. Buka dashboard OpenWA:**

```
http://IP-SERVER:2886
```

**3. Buat sesi WhatsApp baru:**
- Klik **New Session** → beri nama (contoh: `default`)
- Scan QR code dengan WhatsApp di HP

**4. Buat API Key:**
- Menu **Auth → API Keys** → **Create Key**
- Salin API key yang dihasilkan

---

## Konfigurasi di Odoo

Masuk ke **Settings → WhatsApp Receipt**:

| Field | Keterangan | Contoh |
|-------|-----------|--------|
| **Base URL** | URL server OpenWA | `http://192.168.1.10:2785` |
| **API Key** | API key dari OpenWA | `owk_xxxxxxxxxxxx` |
| **Session ID** | Nama sesi WhatsApp | `default` |
| **Template Pesan** | Template dengan variabel `{total}`, `{date}`, `{receipt_url}` | Lihat contoh di bawah |

**Contoh template pesan:**

```
Terima kasih telah berbelanja!

Total: {total}
Tanggal: {date}

Lihat struk lengkap:
{receipt_url}
```

**Set base URL agar link struk menggunakan domain yang benar:**

```bash
sudo -u odoo psql -d NAMA_DATABASE -c \
  "UPDATE ir_config_parameter SET value='https://domain-kamu.com' WHERE key='web.base.url';"
```

---

## Cara Pakai

1. Buka POS dan lakukan transaksi seperti biasa
2. Setelah payment, muncul kolom WhatsApp di halaman struk
3. Masukkan nomor WA pelanggan (format: `08xxx` atau `628xxx`)
4. Klik tombol kirim
5. Pelanggan menerima pesan WA dengan link struk lengkap
6. Link struk dapat dibuka tanpa perlu login ke Odoo

---

## Troubleshooting

**Link struk 404 / Not Found**
- Pastikan module sudah ter-install di database yang aktif
- Cek `web.base.url` sudah sesuai domain
- Pastikan `dbfilter` di `odoo.conf` tidak memblokir akses publik

**WA tidak terkirim**
- Cek Base URL dan API Key OpenWA di Settings
- Pastikan sesi WhatsApp di OpenWA statusnya `CONNECTED`
- Cek log Odoo: `sudo journalctl -u odoo -n 50`
- Cek log OpenWA: `docker compose logs -f`

**Error koneksi ke OpenWA**
- Pastikan port `2785` bisa diakses dari server Odoo
- Jika Odoo dan OpenWA di server berbeda, pastikan firewall mengizinkan koneksi

---

## Perbedaan dengan Versi Fonnte

| | Versi Lama (Fonnte) | Versi Ini (OpenWA) |
|--|--------------------|--------------------|
| **Biaya** | Berbayar (per pesan/bulan) | Gratis |
| **Data** | Di server Fonnte | Di server sendiri |
| **Setup** | Daftar akun Fonnte | Install OpenWA sendiri |
| **Konfigurasi** | Token + Nomor pengirim | Base URL + API Key + Session ID |

---

## Struktur Module

```
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
```

---

## Changelog

### v17.0.2.0.0
- Migrasi dari Fonnte ke OpenWA (self-hosted)
- Ganti konfigurasi token/sender dengan Base URL, API Key, Session ID
- Update endpoint API ke format OpenWA

### v17.0.1.0.0
- Initial release dengan Fonnte

---

## Kontribusi

1. Fork repo ini
2. Buat branch baru: `git checkout -b fitur-baru`
3. Commit: `git commit -m 'Tambah fitur X'`
4. Push: `git push origin fitur-baru`
5. Buat Pull Request

---

## Lisensi

LGPL-3

---

## Developer

Dibuat untuk kebutuhan bisnis ritel Indonesia.
Menggunakan OpenWA sebagai WhatsApp API gateway open-source.
