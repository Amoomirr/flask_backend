#pip install pyqrcode

import pyqrcode #module package/Dependecies
from pyqrcode import QRCode #it will extract QRcode from the pyqrcode package
  
# String which represent the QR code 
s = "https://www.google.com/"
  
# Generate QR code 
url = pyqrcode.create(s) #actual package which is having functions or methods
  
# Create and save the png file naming "myqr.png" 
#Scalable Vector Graphics
url.svg("mygoogle.svg", scale = 8)
