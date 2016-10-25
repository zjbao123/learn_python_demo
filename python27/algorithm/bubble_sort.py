#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'zjbao123'

def bubble_sort(sort_list):
    iter_len = len(sort_list)
    if iter_len<2:
        return sort_list
    for i in range(iter_len-1):
        for j in range(iter_len-1-i):
            if sort_list[j]>sort_list[j+1]:
                sort_list[j],sort_list[j+1]=sort_list[j+1],sort_list[j]

    return sort_list
if __name__ == '__main__':
    print bubble_sort([2,5,7,9,1,3,4,8,0])