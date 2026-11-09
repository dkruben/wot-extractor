# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/Lib/ctypes/test/test_libc.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/ctypes/test/test_libc.py
import unittest
from ctypes import *
import _ctypes_test
lib = CDLL(_ctypes_test.__file__)

class LibTest(unittest.TestCase):

    def test_sqrt(self):
        lib.my_sqrt.argtypes = (
         c_double,)
        lib.my_sqrt.restype = c_double
        self.assertEqual(lib.my_sqrt(4.0), 2.0)
        import math
        self.assertEqual(lib.my_sqrt(2.0), math.sqrt(2.0))

    def test_qsort(self):
        comparefunc = CFUNCTYPE(c_int, POINTER(c_char), POINTER(c_char))
        lib.my_qsort.argtypes = (c_void_p, c_size_t, c_size_t, comparefunc)
        lib.my_qsort.restype = None

        def sort(a, b):
            return cmp(a[0], b[0])

        chars = create_string_buffer('spam, spam, and spam')
        lib.my_qsort(chars, len(chars) - 1, sizeof(c_char), comparefunc(sort))
        self.assertEqual(chars.raw, '   ,,aaaadmmmnpppsss\x00')
        return


if __name__ == '__main__':
    unittest.main()
