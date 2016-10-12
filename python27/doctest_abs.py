#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'zjbao123'
def abs(n):
    '''
    Function to get absolute value of number.

    Example:

    >>> abs(-1)
    1
    >>> abs(0)
    0
    >>> abs('sd')
    Traceback (most recent call last):
        ...
    TypeError: bad operand type
    '''
    if isinstance(n,int):
        return n if n >= 0 else (-n)
    else:
        raise TypeError('bad operand type')
if __name__=='__main__':
    import doctest
    doctest.testmod()