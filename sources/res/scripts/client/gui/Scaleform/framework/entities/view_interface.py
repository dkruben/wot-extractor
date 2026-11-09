# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/framework/entities/view_interface.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/framework/entities/view_interface.py
from __future__ import absolute_import

class ViewInterface(object):

    @property
    def uiImpl(self):
        raise NotImplementedError

    @property
    def layer(self):
        raise NotImplementedError

    @property
    def viewScope(self):
        raise NotImplementedError

    @property
    def key(self):
        raise NotImplementedError

    @property
    def alias(self):
        raise NotImplementedError

    @property
    def uniqueName(self):
        raise NotImplementedError

    @property
    def settings(self):
        raise NotImplementedError

    @property
    def soundManager(self):
        raise NotImplementedError

    def isViewModal(self):
        raise NotImplementedError

    def getAlias(self):
        raise NotImplementedError

    def setAlias(self, alias):
        raise NotImplementedError

    def getSubContainersSettings(self):
        raise NotImplementedError

    def getUniqueName(self):
        raise NotImplementedError

    def setUniqueName(self, name):
        raise NotImplementedError

    def getCurrentScope(self):
        raise NotImplementedError

    def setCurrentScope(self, scope):
        raise NotImplementedError
