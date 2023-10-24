# Install library qrcode = pip install qrcode
# Install library image = pip install image
# code . untuk membuka vs code lewat terminal
# install python 3.12 di microsoft store bagi yang error di pip

import qrcode # import library yang akan di pakai 
import image
qr = qrcode.QRCode(
  version = 15, # untuk versi qr codenya
  box_size = 10, # untuk ukuran qr codenya
  border = 5, #ukuran putihnya qr code
)

data = "https://youtu.be/EJx6q5aw4ck?si=kXh8s1gpLDTLqy1n" # link qr code

qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill="blue", back_color = "white") # setting warna qr code
img.save("link.png") # untuk build rq ke gambar png 
