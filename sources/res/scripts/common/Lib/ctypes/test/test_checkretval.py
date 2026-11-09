# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/Lib/ctypes/test/test_checkretval.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/ctypes/test/test_checkretval.py
import unittest
from ctypes import *
from ctypes.test import need_symbol

class CHECKED(c_int):

    def _check_retval_(value):
        return str(value.value)

    _check_retval_ = staticmethod(_check_retval_)


class Test(unittest.TestCase):

    def test_checkretval(self):
        import _ctypes_test
        dll = CDLL(_ctypes_test.__file__)
        self.assertEqual(42, dll._testfunc_p_p(42))
        dll._testfunc_p_p.restype = CHECKED
        self.assertEqual('42', dll._testfunc_p_p(42))
        dll._testfunc_p_p.restype = None
        self.assertEqual(None, dll._testfunc_p_p(42))
        del dll._testfunc_p_p.restype
        self.assertEqual(42, dll._testfunc_p_p(42))
        return

    @need_symbol('oledll')
    def test_oledll(self):
        self.assertRaises(WindowsError, oledll.oleaut32.CreateTypeLib2, 0, None, None)
        return


if __name__ == '__main__':
    unittest.main()
