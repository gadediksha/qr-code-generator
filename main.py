# qr-code-generator
import qrcode
from PIL import Image

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=6
)

qr.add_data("https://www.youtube.com/watch?v=c199yjfSVPg")
qr.make(fit=True)

qr_img = qr.make_image(
    fill_color="purple",
    back_color="lavender"
).convert("RGBA")

logo = Image.open("logo.png").convert("RGBA")
qr_width, qr_height = qr_img.size
logo_size = qr_width // 5

logo = logo.resize((logo_size, logo_size))

pos = (
    (qr_width - logo_size) // 2,
    (qr_height - logo_size) // 2
)

qr_img.paste(logo, pos, logo)

qr_img.save("final__qr.png")
print("QR CODE Successfully generated !!")
print("Qr code saved as final__qr .png")
print("Scan qr ..")
