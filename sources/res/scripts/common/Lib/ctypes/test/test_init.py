# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/Lib/ctypes/test/test_init.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/ctypes/test/test_init.py
from ctypes import *
import unittest

class X(Structure):
    _fields_ = [
     (
      'a', c_int),
     (
      'b', c_int)]
    new_was_called = False

    def __new__(cls):
        result = super(X, cls).__new__(cls)
        result.new_was_called = True
        return result

    def __init__(self):
        self.a = 9
        self.b = 12


class Y(Structure):
    _fields_ = [
     (
      'x', X)]


class InitTest(unittest.TestCase):

    def test_get(self):
        y = Y()
        self.assertEqual((y.x.a, y.x.b), (0, 0))
        self.assertEqual(y.x.new_was_called, False)
        x = X()
        self.assertEqual((x.a, x.b), (9, 12))
        self.assertEqual(x.new_was_called, True)
        y.x = x
        self.assertEqual((y.x.a, y.x.b), (9, 12))
        self.assertEqual(y.x.new_was_called, False)


if __name__ == '__main__':
    unittest.main()
