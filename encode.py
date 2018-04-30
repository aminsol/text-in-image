from PIL import Image
from math import ceil
import argparse
import os.path as path

# Getting argumrnts from terminal
parser = argparse.ArgumentParser()
parser.add_argument("textfile", help="text file to encode")
parser.add_argument("imagefile", help="input image")
parser.add_argument("outputfile", help="name of output image")
args = parser.parse_args()

# check if image and text file exist
if path.isfile(args.textfile) and path.isfile(args.imagefile):

    im = Image.open(args.imagefile)
    pix = im.load()
    im = im.convert('RGB')
    startX = im.size[0] - 1
    startY = im.size[1] - 1
    msg_start = 11
    msg_bin = ""
    file = open(args.textfile, "r")

    # Reading a file character by character
    for line in file:
        for charater in line:
            msg_bin = msg_bin + (bin(ord(charater))[2:].zfill(8))

    length_bin = bin(len(msg_bin))[2:].zfill(msg_start * 3 - 1)

    length = len(msg_bin)
    print(length)

    # Encoding length of message
    for i in range(0, msg_start):
        pixel = im.getpixel((startX - i, startY))
        encoded_pixel = [pixel[0], pixel[1], pixel[2]]
        for j in range(0, 3):
            if j == 2 and i == 10:
                break
            tmp = bin(pixel[j])[2:-1] + str(length_bin[i * 3 + j])
            encoded_pixel[j] = int(tmp, 2)
        pixel = (encoded_pixel[0], encoded_pixel[1], encoded_pixel[2])

        im.putpixel((startX - i, startY), pixel)
    print(len(msg_bin))

    # Encoding message
    X = startX - msg_start + 1
    Y = startY
    for i in range(msg_start, msg_start + ceil(length / 3)):

        # Encoding into a pixel
        # Y increase by one every time with hit a number dividable by number of X
        if X == 0:
            Y -= 1
            X = startX
        else:
            X -= 1

        pixel = im.getpixel((X, Y))
        # Turning tuple to array just so I can edit RBG separately.
        encoded_pixel = [pixel[0], pixel[1], pixel[2]]
        for j in range(0, 3):
            if (i - msg_start) * 3 + j == length:
                break
            tmp = bin(pixel[j])[2:-1] + str(msg_bin[(i - msg_start) * 3 + j])
            encoded_pixel[j] = int(tmp, 2)

        # Turning the array back to tuple
        pixel = (encoded_pixel[0], encoded_pixel[1], encoded_pixel[2])

        im.putpixel((X, Y), pixel)
    im.save(args.outputfile + ".png")
else:
    print("File doesn't exist!")
