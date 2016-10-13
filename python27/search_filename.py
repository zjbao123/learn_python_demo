#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'zjbao123'
'''编写一个search(s)的函数，
能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，
并打印出完整路径

Usage:
    > search.py str
    str: the str what you want to search in filename in your dir
'''

import os
import sys
def search(s):
    for root,dirs,files in os.walk('.'):
        for f in files:
            if(f.find(s) != -1):
                print os.path.join(root,f)[2:]

if __name__ == '__main__':
    search(sys.argv[1])