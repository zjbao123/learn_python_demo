#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'zjbao123'

import unittest


class test_abs(unittest.TestCase):
    def test_value(self):
        d = abs(-1)
        self.assertEqual(d,1)

    def test_abserror(self):
        with self.assertRaises(TypeError):
           abs('sd')

    def setUp(self):
        print 'setUp...'

    def tearDown(self):
        print 'tearDown...'
if __name__ == '__main__':
    unittest.main()