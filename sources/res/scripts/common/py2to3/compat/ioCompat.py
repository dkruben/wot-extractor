# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/py2to3/compat/ioCompat.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/py2to3/compat/ioCompat.py
from __future__ import absolute_import
import typing
from past.builtins import unicode

def _toUnicode(value, errors='replace'):
    if isinstance(value, unicode):
        return value
    if isinstance(value, bytes):
        return value.decode('utf-8', errors=errors)
    return unicode(value)


class UnicodeFileAdapter(object):

    def __init__(self, target):
        self.target = target

    def write(self, data):
        return self.target.write(_toUnicode(data))

    def writelines(self, lines):
        return self.target.writelines(_toUnicode(line) for line in lines)

    def __getattr__(self, name):
        return getattr(self.target, name)
