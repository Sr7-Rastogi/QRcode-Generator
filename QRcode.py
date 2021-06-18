import qrcode
import image
qrcode=qrcode.QRCode(
    version=15,
    box_size=10,
    border=2
    )
url="https://www.youtube.com"
qrcode.add_data(url)
image=qrcode.make_image(fill="black",back_color="white")
image.save("QRcode.png")
