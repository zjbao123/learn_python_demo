#!/usr/bin/env python
# -*- coding: utf-8 -*-
import msvcrt
import math
__author__ = 'zjbao123'
L=range(33);
for i in L:
   print "%",bin(int((((math.sin(i*math.pi/16))+1)/2)*256)).replace("0b","")

print("Press 'D' to exit...")
while True:
    if ord(msvcrt.getch()) in [68, 100]:
        print ord(msvcrt.getch())
        break
