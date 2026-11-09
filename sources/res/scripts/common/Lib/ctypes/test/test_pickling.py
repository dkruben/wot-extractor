# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/Lib/ctypes/test/test_pickling.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/ctypes/test/test_pickling.py
import unittest, pickle
from ctypes import *
import _ctypes_test
dll = CDLL(_ctypes_test.__file__)

class X(Structure):
    _fields_ = [
     (
      'a', c_int), ('b', c_double)]
    init_called = 0

    def __init__(self, *args, **kw):
        X.init_called += 1
        self.x = 42


class Y(X):
    _fields_ = [
     (
      'str', c_char_p)]


class PickleTest:

    def dumps(self, item):
        return pickle.dumps(item, self.proto)

    def loads(self, item):
        return pickle.loads(item)

    def test_simple(self):
        for src in [
         c_int(42),
         c_double(3.14)]:
            dst = self.loads(self.dumps(src))
            self.assertEqual(src.__dict__, dst.__dict__)
            self.assertEqual(memoryview(src).tobytes(), memoryview(dst).tobytes())

    def test_struct(self):
        X.init_called = 0
        x = X()
        x.a = 42
        self.assertEqual(X.init_called, 1)
        y = self.loads(self.dumps(x))
        self.assertEqual(X.init_called, 1)
        self.assertEqual(y.__dict__, x.__dict__)
        self.assertEqual(memoryview(y).tobytes(), memoryview(x).tobytes())

    def test_unpickable(self):
        self.assertRaises(ValueError, (lambda : self.dumps(Y())))
        prototype = CFUNCTYPE(c_int)
        for item in [
         c_char_p(),
         c_wchar_p(),
         c_void_p(),
         pointer(c_int(42)),
         dll._testfunc_p_p,
         prototype((lambda : 42))]:
            self.assertRaises(ValueError, (lambda : self.dumps(item)))

    def test_wchar(self):
        self.dumps(c_char('x'))
        self.dumps(c_wchar(u'x'))


for proto in range(pickle.HIGHEST_PROTOCOL + 1):
    name = 'PickleTest_%s' % proto
    globals()[name] = type(name, (
     PickleTest, unittest.TestCase), {'proto': proto})

if __name__ == '__main__':
    unittest.main()
