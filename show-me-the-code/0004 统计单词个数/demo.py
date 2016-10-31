#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'zjbao123'
def counter(filename):
    with open(filename,'r') as f:
        content = f.read()
        list= content.split()
        print '单词总共 %d 个。' %(len(list))

counter('content.txt')

