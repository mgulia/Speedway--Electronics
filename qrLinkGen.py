"""
=======================================================================
* Program Name:   QR Code Link Generator
* Description:    Using a list of links in a text file, Program outputs QR codes in directory
* Comments:       Requires list to run (method to create list pending)
*
* EPICS SPEEDWAY // ELECTRONICS
=======================================================================
"""
from os import getcwd, mkdir
import sys
import qrcode

# Global Variables
DataPath = getcwd()
linkPath = DataPath + '/qrForLinks'

"""
=======================================================================
* Function Name:  createFolder
* Description:    Creates a folder that will contain QR Codes
* Parameters:     void
* Return:         void
=======================================================================
"""
def createFolder():
    mkdir(linkPath)

"""
=======================================================================
* Function Name:  loopFile
* Description:    Loops through text file to get link
* Parameters:     void
* Return:         void
=======================================================================
"""
def loopFile():
    with open("links.txt", 'r') as FILE:
        dataFile = FILE.readlines()

    for idx, line in enumerate(dataFile):
        generator(idx+1, line)

"""
=======================================================================
* Function Name:  generator
* Description:    Helper function that generates the codes
* Parameters:     count, int, QR code number 
*                 link, string, Link data to be transformed to QR code
* Return:         void
=======================================================================
"""
def generator(count, link):
    qr = qrcode.QRCode()
    qr.add_data(link)
    qr.make()
    img = qr.make_image()
    img.save(linkPath + '/qrCode_' + str(count) + '.png') #saves QR codes

"""
*****************************
MAIN
*****************************
"""
if __name__ == "__main__":
    createFolder()
    loopFile()