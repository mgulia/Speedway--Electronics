"""
==================================
EPICS SPEEDWAY // ELECTRONICS
==================================
"""
from os import getcwd
import qrcode
from PIL import Image  
import PIL



qrL = qrcode.QRCode(
    version = 3, ## How complex the code is
    error_correction = qrcode.constants.ERROR_CORRECT_L, ## Little Error
    box_size = 100, #qr size
    border = 2) #qr border
qrL.add_data("Purdue.edu") #address
qrL.make(fit = True)

## Output image 
outputQR = qrL.make_image(fill_color = "black", back_color = "white")
outputName = getcwd() + "/qrcode.png"
outputImage = outputQR.save(outputName) ## NEEDS RELOCATION TO SERVER LOCATION