# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/py2to3/compat/base64compat.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/py2to3/compat/base64compat.py
from __future__ import absolute_import
import base64, typing
from past.builtins import unicode
from py2to3.utils import PY3

def _toBytes(value, encoding='utf-8'):
    if isinstance(value, unicode):
        return value.encode(encoding)
    return value


def _toStr(value):
    return str(value.decode('ascii'))


def b32encode(value):
    return _toStr(base64.b32encode(_toBytes(value)))


def b32decode(value):
    return base64.b32decode(_toBytes(value, 'ascii'))


def b32decodeStr(value, encoding='utf-8'):
    res = b32decode(value)
    if PY3:
        return res.decode(encoding)
    return res


def b64encode(value):
    return _toStr(base64.b64encode(_toBytes(value)))


def b64decode(value):
    return base64.b64decode(_toBytes(value, 'ascii'))


def b64decodeStr(value, encoding='utf-8'):
    res = b64decode(value)
    if PY3:
        return res.decode(encoding)
    return res


def urlsafe_b64encode(value):
    return _toStr(base64.urlsafe_b64encode(_toBytes(value)))


def urlsafe_b64decode(value):
    return base64.urlsafe_b64decode(_toBytes(value, 'ascii'))
