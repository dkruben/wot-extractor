# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/Lib/ctypes/test/test_buffers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/ctypes/test/test_buffers.py
from ctypes import *
from ctypes.test import need_symbol
import unittest

class StringBufferTestCase(unittest.TestCase):

    def test_buffer(self):
        b = create_string_buffer(32)
        self.assertEqual(len(b), 32)
        self.assertEqual(sizeof(b), 32 * sizeof(c_char))
        self.assertIs(type(b[0]), str)
        b = create_string_buffer('abc')
        self.assertEqual(len(b), 4)
        self.assertEqual(sizeof(b), 4 * sizeof(c_char))
        self.assertIs(type(b[0]), str)
        self.assertEqual(b[0], 'a')
        self.assertEqual(b[:], 'abc\x00')
        self.assertEqual(b[::], 'abc\x00')
        self.assertEqual(b[::-1], '\x00cba')
        self.assertEqual(b[::2], 'ac')
        self.assertEqual(b[::5], 'a')
        return

    def test_buffer_interface(self):
        self.assertEqual(len(bytearray(create_string_buffer(0))), 0)
        self.assertEqual(len(bytearray(create_string_buffer(1))), 1)

    def test_string_conversion(self):
        b = create_string_buffer(u'abc')
        self.assertEqual(len(b), 4)
        self.assertEqual(sizeof(b), 4 * sizeof(c_char))
        self.assertTrue(type(b[0]) is str)
        self.assertEqual(b[0], 'a')
        self.assertEqual(b[:], 'abc\x00')
        self.assertEqual(b[::], 'abc\x00')
        self.assertEqual(b[::-1], '\x00cba')
        self.assertEqual(b[::2], 'ac')
        self.assertEqual(b[::5], 'a')
        return

    @need_symbol('c_wchar')
    def test_unicode_buffer(self):
        b = create_unicode_buffer(32)
        self.assertEqual(len(b), 32)
        self.assertEqual(sizeof(b), 32 * sizeof(c_wchar))
        self.assertIs(type(b[0]), unicode)
        b = create_unicode_buffer(u'abc')
        self.assertEqual(len(b), 4)
        self.assertEqual(sizeof(b), 4 * sizeof(c_wchar))
        self.assertIs(type(b[0]), unicode)
        self.assertEqual(b[0], u'a')
        self.assertEqual(b[:], 'abc\x00')
        self.assertEqual(b[::], 'abc\x00')
        self.assertEqual(b[::-1], '\x00cba')
        self.assertEqual(b[::2], 'ac')
        self.assertEqual(b[::5], 'a')
        return

    @need_symbol('c_wchar')
    def test_unicode_conversion(self):
        b = create_unicode_buffer('abc')
        self.assertEqual(len(b), 4)
        self.assertEqual(sizeof(b), 4 * sizeof(c_wchar))
        self.assertIs(type(b[0]), unicode)
        self.assertEqual(b[0], u'a')
        self.assertEqual(b[:], 'abc\x00')
        self.assertEqual(b[::], 'abc\x00')
        self.assertEqual(b[::-1], '\x00cba')
        self.assertEqual(b[::2], 'ac')
        self.assertEqual(b[::5], 'a')
        return


if __name__ == '__main__':
    unittest.main()
