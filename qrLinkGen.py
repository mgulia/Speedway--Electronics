import os
import sys
import qrcode

DataPath = os.getcwd()
linkPath = DataPath + '/qrForLinks'

#Creates folder that will contain QR codes
def createFolder():
    os.mkdir(linkPath)

#Loops through textfile and sends data to helper function
def loopFile():
    with open("links.txt", 'r') as FILE:
        dataFile = FILE.readlines()

    for idx, line in enumerate(dataFile):
        generator(idx+1, line)

#Helper function that generates QR codes
def generator(count, link):
    qr = qrcode.QRCode()
    qr.add_data(link)
    qr.make()
    img = qr.make_image()
    img.save(linkPath + '/qrCode_' + str(count) + '.png') #saves QR codes


if __name__ == "__main__":
    createFolder()
    loopFile()
