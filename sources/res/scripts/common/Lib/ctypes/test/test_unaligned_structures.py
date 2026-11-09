# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/Lib/ctypes/test/test_unaligned_structures.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/ctypes/test/test_unaligned_structures.py
import sys, unittest
from ctypes import *
structures = []
byteswapped_structures = []
if sys.byteorder == 'little':
    SwappedStructure = BigEndianStructure
else:
    SwappedStructure = LittleEndianStructure
for typ in [c_short, c_int, c_long, c_longlong, 
 c_float, c_double, 
 c_ushort, c_uint, 
 c_ulong, c_ulonglong]:

    class X(Structure):
        _pack_ = 1
        _fields_ = [('pad', c_byte),
         (
          'value', typ)]


    class Y(SwappedStructure):
        _pack_ = 1
        _fields_ = [('pad', c_byte),
         (
          'value', typ)]


    structures.append(X)
    byteswapped_structures.append(Y)

class TestStructures(unittest.TestCase):

    def test_native(self):
        for typ in structures:
            self.assertEqual(typ.value.offset, 1)
            o = typ()
            o.value = 4
            self.assertEqual(o.value, 4)

    def test_swapped(self):
        for typ in byteswapped_structures:
            self.assertEqual(typ.value.offset, 1)
            o = typ()
            o.value = 4
            self.assertEqual(o.value, 4)


if __name__ == '__main__':
    unittest.main()
