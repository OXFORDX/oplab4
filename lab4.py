from crw_bmp import container
import struct

head_one = container('test.bmp')
head_one.read('test.bmp')