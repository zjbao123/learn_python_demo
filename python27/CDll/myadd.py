# -*- coding: utf-8 -*-
from ctypes import cdll

__author__ = 'zjbao123'


def add(filename, a, b):
    dll = cdll.LoadLibrary(filename)
    ret = dll.Add(a, b)
    var = dll.Mul(a, b)
    print ret, var
