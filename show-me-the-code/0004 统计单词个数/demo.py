#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
第 0004 题：任一个英文的纯文本文件，统计其中的单词出现的个数。
"""
__author__ = 'zjbao123'
def counter(filename):
    with open(filename,'r') as f:
        content = f.read()
        list= content.split()
        print '单词总共 %d 个。' %(len(list))

counter('content.txt')

