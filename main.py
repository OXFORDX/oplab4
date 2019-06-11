from color_cont import PIXELDATA
from header_container import container
import numpy as np
import struct
import time

np.set_printoptions(threshold=9999999)


class resize:
    def __init__(self, file, pow):
        self.file = file
        self.pow = pow
        self.header = container(file)
        self.pixeldata = np.zeros([self.header.height, self.header.width], dtype=classmethod)
        self.pix_arr = np.zeros([self.header.height * self.pow, self.header.width * self.pow],
                                dtype=classmethod)
        self.byte_arr = np.zeros(
            [self.header.height * self.pow, self.header.width * self.pow * 3 + self.padding(self.pow)],
            dtype=int)
        self.arr_bytes = []

    def padding(self, pow):
        var = self.header.width * 3 * pow
        padding = 0
        while var % 4:
            padding += 1
            var += 1
        print(padding)
        return padding

    def pixelcollector(self):
        with open(self.file, 'rb') as file:
            file.read(54)
            for i in range(self.header.height):
                for j in range(self.header.width):
                    pixel = []
                    for k in range(3):
                        x = struct.unpack('B', file.read(1))[0]
                        pixel.append(x)
                    self.pixeldata[i, j] = PIXELDATA(pixel[0], pixel[1], pixel[2])
                file.read(self.padding(1))
        for i in self.pixeldata:
            for j in i:
                print(j.colors())
        return self.pixeldata

    def new_pix(self):
        self.pixelcollector()
        for i in range(self.header.height * self.pow):
            for j in range(self.header.width * self.pow):
                self.pix_arr[i][j] = self.pixeldata[i // self.pow][j // self.pow]
        return self.pix_arr

    def new_byte_array(self):
        self.new_pix()
        for i in range(self.header.height * self.pow):
            var = 0
            for j in range(self.header.width * self.pow):
                for k, n in enumerate(self.pix_arr[i][j].colors()):
                    self.byte_arr[i][var] = n
                    var += 1
        print(self.byte_arr)
        return self.byte_arr

    def final(self):
        self.new_byte_array()
        self.header.height = len(self.byte_arr)
        self.header.width = int(len(self.byte_arr[0]) / 3)
        self.header.filesize = 54 + self.header.height * self.header.width
        print(self.header.height, self.header.width, self.header.filesize)
        self.header.write('love.bmp', self.byte_arr)


start = time.time()
s = resize('rifle.bmp', 100)
s.final()
end = time.time()
print(end - start)
