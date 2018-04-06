from PIL import Image
from math import ceil

im = Image.open('foo_new.png', 'r')
pix = im.load()
startX = im.size[0] - 1
startY = im.size[1] - 1

## 1111000
## should Read: 120
## Security is fun
length = ""
msg_start = 11
for i in range(0, msg_start):
    [R, G, B] = pix[startX - i, startY]
    # print(str(i).zfill(2), bin(G)[2:].zfill(8), bin(R)[2:].zfill(8))
    length = length + str(R % 2 if "1" else "0") + str(G % 2 if "1" else "0")
    if i < 10:
        length = length + str(B % 2 if "1" else "0")
length = int(length, 2)

character = ""
pixel_to_read = ceil(length / 3) + msg_start
msg = ""
for i in range(msg_start, pixel_to_read):
    for j in range(0, 3):
        character = character + str(
            pix[startX - (i - (startX * int(i / startX))), startY - int(i / startX)][j] % 2 if "1" else "0")
        if len(character) == 8:
            msg = msg + chr(int(character, 2))
            character = ""

print(msg)
