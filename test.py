import struct
from color_cont import PIXELDATA
with open('test.bmp', 'rb') as file:
    pixels = []
    file.read(54)
    for i, j in enumerate(file.read()):
        if i % 3 == 0:
            pixels.append(PIXELDATA(j, j + 1, j + 2))
for i in pixels:
    print(i.colors())