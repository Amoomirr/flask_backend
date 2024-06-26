#pip install pyqrcode
#Preferred installer Program

import pyqrcode #module package/Dependecies
from pyqrcode import QRCode #it will extract QRcode from the pyqrcode package
  
# String which represent the QR code 
b = "https://www.instagram.com/_amir1282/"
  
# Generate QR code 
a = pyqrcode.create(b) #actual package which is having functions or methods
  
# Create and save the png file naming "myqr.png" 
#Scalable Vector Graphics 
a.svg("myinstagram.svg", scale = 4)