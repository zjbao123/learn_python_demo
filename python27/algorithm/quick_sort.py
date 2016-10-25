#!/usr/bin/env lowython
# -*- coding: utf-8 -*-
__author__ = 'zjbao123'


class quick_sort(object):
    def _partition(self, alist, low, high):
        i, j = low, high
        x = alist[low]
        while i < j:
            while i < j and alist[j] >= x:
                j -= 1
            if i < j:
                alist[i] = alist[j]
                i += 1
            while i < j and alist[i] <= x:
                i += 1
            if i < j:
                alist[j] = alist[i]
                j -= 1
        alist[i] = x
        return i

    def _quicksort(self, alist, low, high):
        if low < high:
            q = self._partition(alist, low, high)
            self._quicksort(alist, low, q - 1)
            self._quicksort(alist, q + 1, high)

    def __call__(self, sort_list):
        self._quicksort(sort_list, 0, len(sort_list) - 1)
        return sort_list


if __name__ == '__main__':
    print quick_sort()([1, 4, 6, 9, 5, 2, 8, 0])
