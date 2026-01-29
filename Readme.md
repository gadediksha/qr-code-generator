# 🟣 QR Code Generator with Logo (Python)

Generate **custom QR codes** with your own colors and embed a **center logo** easily using Python! 🚀

---

## 🔹 Features
- ✅ Generate QR codes from **URLs or text**
- 🎨 Customizable **fill and background colors**
- 🔒 High error correction (`ERROR_CORRECT_H`) for better scanning
- 🖼️ Embed a **logo at the center**
- 💾 Saves QR code as `final_qr.png`

---

## 📂 Project Structure
qr-code-generator/
│
├── main.py # Python script to generate QR code
├── logo.png # Logo to embed in the QR code
├── requirements.txt # Python dependencies
└── README.md # Project description


---

## ⚙️ Installation

1️⃣ **Clone the repository:**
```bash
1.git clone https://github.com/gadediksha/qr-code-generator.git
cd qr-code-generator

```
2.pip install -r requirements.txt

```
3.QR code will be generated as:
final_qr.png
4.Scan it using any QR code scanner 📱

## 🎨 Customization
# Change URL/Text:
qr.add_data("https://example.com")
# Change colors:
fill_color="purple"
back_color="lavender"
# Change logo size:
logo_size = qr_width // 5
# Replace logo: use any PNG image with square dimensions 🖼️

## 💡 Notes

* Logo should ideally be square for best results 🟦

* High error correction allows QR code to remain scannable even with logo 🛡️

* Great for projects, portfolio, or demo apps 🎓💼

## 🖥️ Tech Stack

* Python 3.x 🐍

* qrcode library

* Pillow (PIL) library
Made with 💜 and 🖤 for the perfect QR code experience!

# Thank You...
# Diksha Gade
# BCA


