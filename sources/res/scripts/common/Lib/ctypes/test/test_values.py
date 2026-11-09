# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/Lib/ctypes/test/test_values.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/ctypes/test/test_values.py
import unittest, sys
from ctypes import *
import _ctypes_test

class ValuesTestCase(unittest.TestCase):

    def test_an_integer(self):
        ctdll = CDLL(_ctypes_test.__file__)
        an_integer = c_int.in_dll(ctdll, 'an_integer')
        x = an_integer.value
        self.assertEqual(x, ctdll.get_an_integer())
        an_integer.value *= 2
        self.assertEqual(x * 2, ctdll.get_an_integer())

    def test_undefined(self):
        ctdll = CDLL(_ctypes_test.__file__)
        self.assertRaises(ValueError, c_int.in_dll, ctdll, 'Undefined_Symbol')


class PythonValuesTestCase(unittest.TestCase):

    def test_optimizeflag(self):
        opt = c_int.in_dll(pythonapi, 'Py_OptimizeFlag').value
        if ValuesTestCase.__doc__ is not None:
            self.assertEqual(opt, 1)
        else:
            self.assertEqual(opt, 2)
        return

    def test_frozentable(self):

        class struct_frozen(Structure):
            _fields_ = [
             (
              'name', c_char_p),
             (
              'code', POINTER(c_ubyte)),
             (
              'size', c_int)]

        FrozenTable = POINTER(struct_frozen)
        ft = FrozenTable.in_dll(pythonapi, 'PyImport_FrozenModules')
        items = []
        for entry in ft:
            if entry.name is None:
                break
            items.append((entry.name, entry.size))

        expected = [('__hello__', 104),
         ('__phello__', -104),
         ('__phello__.spam', 104)]
        self.assertEqual(items, expected)
        from ctypes import _pointer_type_cache
        del _pointer_type_cache[struct_frozen]
        return

    def test_undefined(self):
        self.assertRaises(ValueError, c_int.in_dll, pythonapi, 'Undefined_Symbol')


if __name__ == '__main__':
    unittest.main()
