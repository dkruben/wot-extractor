# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/messenger/inject.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/messenger/inject.py
from __future__ import absolute_import
from messenger import MessengerEntry

class messengerEntryProperty(property):

    def __get__(self, obj, objType=None):
        return MessengerEntry.g_instance


class channelsCtrlProperty(property):

    def __get__(self, obj, objType=None):
        return MessengerEntry.g_instance.gui.channelsCtrl
