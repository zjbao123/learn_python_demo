#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'zjbao123'
#1.导入Image类

from PIL import Image

#2.使用Image的对象读取图片路径
Image_name = 'e.jpg'
img = Image.open(Image_name)
img = img.convert('L')

#3.将图片转为灰度图片

#4。获取原图片大小，并根据实际需要按比例缩小图片

w,h = img.size
if w>100 or w < 50:
    h = int((100.0/w) * h / 2)
    w = 50
print (h,w)
img = img.resize((w,h), Image.ANTIALIAS)
img.save('b.png')

#将缩小的图片像素点的颜色值转为字符并保存
data=[]
#根据图片的宽高来遍历像素点并取出像素点的颜色值
chars = [' ', ',', '+', '1', 'n', 'D', '@', 'W']

for i in range(0,h):
    line=''
    for j in range(0,w):
        pi = img.getpixel((j,i))
        for k in range(0,8):
            if pi < (k+1)*32:
                line += chars[7-k]
                break
    data.append(line)


#将保存的字符列表写到文件中
f = open(Image_name+'.txt','w')
for d in data:
    print(d,file=f)
f.close()
