# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/frameworks/wulf/resource_manager.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/frameworks/wulf/resource_manager.py
from __future__ import absolute_import
import typing
from .py_object_binder import PyObjectEntity

class ResourceManager(PyObjectEntity):

    @classmethod
    def create(cls, proxy):
        manager = ResourceManager()
        manager.bind(proxy)
        return manager

    def destroy(self):
        self.unbind()

    def getTranslatedText(self, resourceID):
        return self.proxy.getTranslatedText(resourceID)

    def getImagePath(self, resourceID):
        return self.proxy.getImagePath(resourceID)

    def getSoundEffectId(self, resourceID):
        return self.proxy.getSoundEffectId(resourceID)

    def getRootNode(self):
        return self.proxy.getRootNode()
