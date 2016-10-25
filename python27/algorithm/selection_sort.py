#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'zjbao123'
def selection_sort(sort_list):
    iter_len = len(sort_list)
    if iter_len<2:
        return sort_list
    for i in range(iter_len-1):
        smallest = sort_list[i]
        location = i
        for j in range(i+1,iter_len):
            if sort_list[j]<smallest:
                smallest = sort_list[j]
                location = j
        if i !=location:
            sort_list[i],sort_list[location]= sort_list[location],sort_list[i]
    return sort_list
if __name__ == '__main__':
    print selection_sort([1, 4, 6, 9, 5, 2, 8, 0])