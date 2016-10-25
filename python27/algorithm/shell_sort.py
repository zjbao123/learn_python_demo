#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'zjbao123'
import time

def shell_sort(sort_list):
    begin = time.clock()
    iter_len = len(sort_list)
    if iter_len < 2:
        return sort_list
    gap = iter_len / 2
    while gap > 0:
        for i in range(0, gap):
            for j in range(i + gap, iter_len, gap):
                if (sort_list[j] < sort_list[j - gap]):
                    key = sort_list[j]
                    k = j - gap
                    while k >= 0 and sort_list[k]>key:
                        sort_list[k + gap] = sort_list[k]
                        k -= gap

                    sort_list[k + gap] = key
        gap /= 2
    end = time.clock()
    print end - begin
    return sort_list

print shell_sort([2,5,3,6,1,7,9,11,4])

