import pyqrcode
import png

link = "https://www.google.com/"
qr_code = pyqrcode.create(link)
qr_code.png("Google.png", scale=7)