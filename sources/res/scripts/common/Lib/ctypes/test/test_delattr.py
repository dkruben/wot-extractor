# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/Lib/ctypes/test/test_delattr.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/ctypes/test/test_delattr.py
import unittest
from ctypes import *

class X(Structure):
    _fields_ = [
     (
      'foo', c_int)]


class TestCase(unittest.TestCase):

    def test_simple(self):
        self.assertRaises(TypeError, delattr, c_int(42), 'value')

    def test_chararray(self):
        self.assertRaises(TypeError, delattr, (c_char * 5)(), 'value')

    def test_struct(self):
        self.assertRaises(TypeError, delattr, X(), 'foo')


if __name__ == '__main__':
    unittest.main()
