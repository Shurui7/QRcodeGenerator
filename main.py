import qrcode

link = input("Put your link here:")
namelink = input("Put here the name of site: ")



img = qrcode.make(f"{link}")
img.save(f"{namelink}QR.jpg")