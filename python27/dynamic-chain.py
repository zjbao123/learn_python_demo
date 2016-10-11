#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'zjbao123'
'create dynamic chain '


class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path
print Chain().status.user.timeline.list
# '/status/user/timeline/list'
#调用Github的URL时，需要把:user替换为实际用户名。

