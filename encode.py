from PIL import Image
from math import ceil
import argparse
import os.path as path

im = Image.open('test.jpg')
pix = im.load()
startX = im.size[0] - 1
startY = im.size[1] - 1
msg_start = 11
msg_bin = ""

parser = argparse.ArgumentParser()
parser.add_argument("fileName", help="Enter a filename")
args = parser.parse_args()
if path.isfile(args.fileName):

    file = open(args.fileName, "r")

    for line in file:
        for charater in line:
            msg_bin = msg_bin + (bin(ord(charater))[2:].zfill(8))

    length_bin = bin(len(msg_bin))[2:].zfill(msg_start * 3 - 1)

    length = len(msg_bin)
    print(length)
    for i in range(0, msg_start):
        pixel = pix[startX - i, startY]
        encoded_pixel = [pixel[0], pixel[1], pixel[2]]
        for j in range(0, 3):
            if j == 2 and i == 10:
                break
            tmp = bin(pixel[j])[2:-1] + str(length_bin[i * 3 + j])
            encoded_pixel[j] = int(tmp, 2)
        pixel = (encoded_pixel[0], encoded_pixel[1], encoded_pixel[2])

        pix[startX - i, startY] = pixel
    print(len(msg_bin))
    for i in range(msg_start, msg_start + ceil(length / 3)):
        pixel = pix[startX - (i - (startX * int(i / startX))), startY - int(i / startX)]
        encoded_pixel = [pixel[0], pixel[1], pixel[2]]
        for j in range(0, 3):
            if (i - msg_start) * 3 + j == length:
                break
            tmp = bin(pixel[j])[2:-1] + str(msg_bin[(i - msg_start) * 3 + j])
            encoded_pixel[j] = int(tmp, 2)
        pixel = (encoded_pixel[0], encoded_pixel[1], encoded_pixel[2])

        pix[startX - (i - (startX * int(i / startX))), startY - int(i / startX)] = pixel
    im.save("foo_new.png")
else:
    print("File doesn't exist!")
