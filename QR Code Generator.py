#QR code generator
import pyqrcode
link = pyqrcode.create('Paste the url here.')
link.png('code.png', scale=8)