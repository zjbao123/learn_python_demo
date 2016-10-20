#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'zjbao123'

import random
l = [chr(i) for i in range(97,123)] + [chr(i) for i in range(48,58)] + [chr(i) for i in range(65,91)]

def random_seq(number, length = 10):
    seq = []
    l = [chr(i) for i in range(97,123)] + [chr(i) for i in range(48,58)] + [chr(i) for i in range(65,91)]
    for i in range(number):
        k = ('').join(random.sample(l,length))
        seq.append(k)
    return seq

if __name__ =='__main__':
    with open('seq.txt','w') as f:
        for i in random_seq(200):
            f.write(i+'\n')
        print '生成成功！'