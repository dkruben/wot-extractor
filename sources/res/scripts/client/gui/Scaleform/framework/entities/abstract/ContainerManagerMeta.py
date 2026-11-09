# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/framework/entities/abstract/ContainerManagerMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/framework/entities/abstract/ContainerManagerMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class ContainerManagerMeta(BaseDAAPIComponent):

    def isModalViewsIsExists(self):
        self._printOverrideError('isModalViewsIsExists')

    def as_getViewS(self, name):
        if self._isDAAPIInited():
            return self.flashObject.as_getView(name)

    def as_showS(self, name, x=0, y=0):
        if self._isDAAPIInited():
            return self.flashObject.as_show(name, x, y)

    def as_registerContainerS(self, layer, name):
        if self._isDAAPIInited():
            return self.flashObject.as_registerContainer(layer, name)

    def as_unregisterContainerS(self, layer):
        if self._isDAAPIInited():
            return self.flashObject.as_unregisterContainer(layer)

    def as_closePopUpsS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_closePopUps()

    def as_isOnTopS(self, layer, windowName):
        if self._isDAAPIInited():
            return self.flashObject.as_isOnTop(layer, windowName)

    def as_bringToFrontS(self, layer, windowName):
        if self._isDAAPIInited():
            return self.flashObject.as_bringToFront(layer, windowName)

    def as_showContainersS(self, layers, time=0):
        if self._isDAAPIInited():
            return self.flashObject.as_showContainers(layers, time)

    def as_hideContainersS(self, layers, time=0):
        if self._isDAAPIInited():
            return self.flashObject.as_hideContainers(layers, time)

    def as_isContainerShownS(self, layer):
        if self._isDAAPIInited():
            return self.flashObject.as_isContainerShown(layer)

    def as_getVisibleLayersS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getVisibleLayers()

    def as_setVisibleLayersS(self, layers):
        if self._isDAAPIInited():
            return self.flashObject.as_setVisibleLayers(layers)
