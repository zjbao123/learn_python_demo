#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'zjbao123'

from PIL import Image,ImageDraw,ImageFont
import random
def addNum(r):
    img = Image.open('1.jpg')
    img = img.convert('RGB')
    draw = ImageDraw.Draw(img)
    myfont = ImageFont.truetype('C:/windows/fonts/Arial.ttf', size=20)
    draw.text((img.size[1]-20, 20), unicode(r),font=myfont, fill = 'red')
    img.save('2.jpg','jpeg')

if __name__ == "__main__":
    addNum(random.randint(0,99))