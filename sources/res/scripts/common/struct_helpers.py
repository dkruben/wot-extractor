# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/struct_helpers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/struct_helpers.py
from __future__ import absolute_import
from struct import unpack, pack

def unpackByte(char):
    return unpack('B', char)[0]


def packByte(code):
    return pack('B', code)
