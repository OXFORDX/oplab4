import struct
import numpy as np


class container:
    def __init__(self, file):
        self.bmp = open(file, 'rb')
        self.type = self.bmp.read(2).decode()
        self.filesize = 0
        self.reserved1 = np.int16(struct.unpack('H', self.bmp.read(2))[0])
        self.reserverd2 = np.int16(struct.unpack('H', self.bmp.read(2))[0])
        self.offset = np.int32(struct.unpack('I', self.bmp.read(4))[0])
        self.headersize = np.int32(struct.unpack('I', self.bmp.read(4))[0])
        self.width = 0
        self.height = 0
        self.numofpix = self.width * self.height
        self.col_planes = np.int16(struct.unpack('H', self.bmp.read(2))[0])
        self.bits_per_pix = np.int16(struct.unpack('H', self.bmp.read(2))[0])
        self.compress_metod = np.int32(struct.unpack('I', self.bmp.read(4))[0])
        self.raw_size = np.int32(struct.unpack('I', self.bmp.read(4))[0])
        self.horiz_rez = np.int32(struct.unpack('I', self.bmp.read(4))[0])
        self.vert_rez = np.int32(struct.unpack('I', self.bmp.read(4))[0])
        self.num_ofcol = np.int32(struct.unpack('I', self.bmp.read(4))[0])
        self.import_col = np.int32(struct.unpack('I', self.bmp.read(4))[0])

    def read_header(self, file):
        self.bmp = open(file, 'rb')
        self.type = self.bmp.read(2).decode()
        self.filesize = np.int32(struct.unpack('I', self.bmp.read(4))[0])  ##
        self.reserved1 = np.int16(struct.unpack('H', self.bmp.read(2))[0])
        self.reserverd2 = np.int16(struct.unpack('H', self.bmp.read(2))[0])
        self.offset = np.int32(struct.unpack('I', self.bmp.read(4))[0])
        self.headersize = np.int32(struct.unpack('I', self.bmp.read(4))[0])
        self.width = np.int32(struct.unpack('I', self.bmp.read(4))[0])  ##
        self.height = np.int32(struct.unpack('I', self.bmp.read(4))[0])  ##
        self.col_planes = np.int16(struct.unpack('H', self.bmp.read(2))[0])
        self.bits_per_pix = np.int16(struct.unpack('H', self.bmp.read(2))[0])
        self.compress_metod = np.int32(struct.unpack('I', self.bmp.read(4))[0])
        self.raw_size = np.int32(struct.unpack('I', self.bmp.read(4))[0])
        self.horiz_rez = np.int32(struct.unpack('I', self.bmp.read(4))[0])
        self.vert_rez = np.int32(struct.unpack('I', self.bmp.read(4))[0])
        self.num_ofcol = np.int32(struct.unpack('I', self.bmp.read(4))[0])
        self.import_col = np.int32(struct.unpack('I', self.bmp.read(4))[0])

    def write(self, file):
        f = open(file, 'wb')
        f.write(self.type.encode())  # type
        f.write(struct.pack('I', self.filesize))
        f.write(struct.pack('H', self.reserved1))
        f.write(struct.pack('H', self.reserverd2))
        f.write(struct.pack('I', self.offset))
        f.write(struct.pack('I', self.headersize))
        f.write(struct.pack('I', self.width))
        f.write(struct.pack('I', self.height))
        f.write(struct.pack('H', self.col_planes))
        f.write(struct.pack('H', self.bits_per_pix))
        f.write(struct.pack('I', self.compress_metod))
        f.write(struct.pack('I', self.raw_size))
        f.write(struct.pack('I', self.horiz_rez))
        f.write(struct.pack('I', self.vert_rez))
        f.write(struct.pack('I', self.num_ofcol))
        f.write(struct.pack('I', self.import_col))
        f.close()


g = container('test.bmp')
print(g.type.encode())
g.write('kek.bmp')
