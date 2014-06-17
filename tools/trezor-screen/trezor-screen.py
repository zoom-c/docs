#!/usr/bin/python
from PIL import Image
import sys
import os

path = sys.argv[1]
data = open(path, 'r').read().strip()
data = data.decode('hex')
name, ext = os.path.splitext(path)

im = Image.open('trezor-screen.png')
left, top = 161, 497
pix = im.load()

for x in range(128):
    for y in range(64):
        rx, ry = 127 - x, 63 - y
        val = ((ord(data[rx + (ry / 8) * 128]) & (1 << (ry % 8))) > 0) and (255, 255) or (0, 255)
        for i in range(5):
            for j in range(5):
                pix[left + x * 5 + i, top + y * 5 + j] = val

im.save("trezor-screen-%s.png" % name)
