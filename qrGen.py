"""
===================================
EPICS SPEEDWAY // ELECTRONICS 2020
===================================
"""
from os import getcwd ## Working Directory
import qrcode ## QR Code Module: pip install qrcode
from PIL import Image ## Python Imaging Library



qrL = qrcode.QRCode(
    version = 3, ## How complex the code is
    error_correction = qrcode.constants.ERROR_CORRECT_L, ## 'Little' Error margin
    box_size = 100, #qr size
    border = 2) #qr border
qrL.add_data("purdue.edu") # Temp address
qrL.make(fit = True)

## Output image 
outputQR = qrL.make_image(fill_color = "black", back_color = "white")
outputName = "/Users/G/Desktop/qrOut.png"  #getcwd() once implemented correctly

try:
    outputImage = outputQR.save(outputName) ## NEEDS RELOCATION TO SERVER LOCATION
    print(f"\n\nQR Successfully outputted at {outputName}\n\n")
except:
    print("QR Code Creation unsuccessful.")


