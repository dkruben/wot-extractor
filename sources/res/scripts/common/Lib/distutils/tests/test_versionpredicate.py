# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/Lib/distutils/tests/test_versionpredicate.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/distutils/tests/test_versionpredicate.py
import distutils.versionpredicate, doctest
from test.test_support import run_unittest

def test_suite():
    return doctest.DocTestSuite(distutils.versionpredicate)


if __name__ == '__main__':
    run_unittest(test_suite())
