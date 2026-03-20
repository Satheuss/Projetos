import qrcode
from PIL import Image

x = input("Digite o URL de um Site para Gerar um QR code: ")
data = x

qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)
image = qr.make_image(fill_color="black", black_color="white")

image.save("qr_code.png")
Image.open("qr_code.png").show()