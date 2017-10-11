# -*- coding: utf-8 -*-
import ConfigParser

__author__ = 'zjbao123'
import os
import ctypes
import myadd
CUR_PATH = os.path.dirname(__file__)

print 'starting...'
# 不同的dll
dll = ctypes.WinDLL(os.path.join(CUR_PATH, 'HelloWorld.dll'))
dll.hello()
myadd.add("hello.dll", ctypes.c_int(2), 4)
# dll = ctypes.cdll.LoadLibrary('HelloWorld.dll')
# dll.hello()
