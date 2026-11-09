# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/messenger/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/messenger/__init__.py
from __future__ import absolute_import
import typing
from external_strings_utils import unicode_from_utf8
from soft_exception import SoftException
from messenger.m_settings import MessengerSettings

class error(SoftException):
    pass


g_settings = MessengerSettings()

def normalizeGroupId(itemId):
    if isinstance(itemId, bytes):
        return unicode_from_utf8(itemId)[1]
    return itemId
