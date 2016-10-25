#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'zjbao123'


class heap_sort(object):
    def _max_heapify(self, alist, i, heap_size=None):
        length = len(alist)
        if heap_size is None:
            heap_size = length
        l = 2 * i + 1
        r = 2 * i + 2
        largest = i
        if l < heap_size and alist[l] > alist[i]:
            largest = l
        if l < heap_size and alist[r] > alist[i]:
            largest = r
        if largest != i:
            alist[i], alist[largest] = alist[largest], alist[i]
            self._max_heapify(alist, largest, heap_size)

    def _build_max_heap(self, alist):
        root_end = int(len(alist) / 2)
        for i in range(root_end-1,-1,-1):
            self._max_heapify(alist,i)

    def __call__(self, sort_list):
        self._build_max_heap(sort_list)
        heap_size = len(sort_list)
        for i in range(len(sort_list)-1,0,-1):
            sort_list[0],sort_list[i]=sort_list[i],sort_list[0]
            heap_size -=1
            self._max_heapify(sort_list, 0, heap_size)
        return sort_list
