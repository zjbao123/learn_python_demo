#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'zjbao123'
'''insertion sort'''


def insertion_sort(sort_list):
    iter_len = len(sort_list)
    if iter_len < 2:
        return sort_list
    for i in range(1, iter_len):
        key = sort_list[i]
        location = i
        for j in range(i - 1, -1, -1):
            if sort_list[j] > key:
                sort_list[j + 1] = sort_list[j]
                location = j
        sort_list[location] = key
    return sort_list

