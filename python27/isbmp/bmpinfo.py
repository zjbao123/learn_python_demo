#!/usr/bin/env python
# -*- coding: utf-8 -*-
import struct


def isbmp(s):
    f = open(s, 'rb').read(30)
    b = struct.unpack('<ccIIIIIIHH', f)
    if b[0] == 'B' and b[1] == 'M':
        print "size = %s * %s" % (b[6], b[7])
        print "color = %s " % (b[-1])
    else:
        print "it's not bmp!"


if __name__ == '__main__':
    isbmp('1.bmp')
    isbmp("1.jpg")
