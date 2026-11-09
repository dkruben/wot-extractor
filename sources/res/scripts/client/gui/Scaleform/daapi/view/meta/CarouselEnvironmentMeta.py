# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/meta/CarouselEnvironmentMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/CarouselEnvironmentMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class CarouselEnvironmentMeta(BaseDAAPIComponent):

    def selectVehicle(self, id):
        self._printOverrideError('selectVehicle')

    def resetFilters(self):
        self._printOverrideError('resetFilters')

    def updateHotFilters(self):
        self._printOverrideError('updateHotFilters')

    def as_getDataProviderS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getDataProvider()

    def as_setInitDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(data)

    def as_setEnabledS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setEnabled(value)

    def as_showCounterS(self, countText, isAttention):
        if self._isDAAPIInited():
            return self.flashObject.as_showCounter(countText, isAttention)

    def as_hideCounterS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideCounter()

    def as_blinkCounterS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_blinkCounter()

    def as_setCarouselFilterS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setCarouselFilter(data)

    def as_initCarouselFilterS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_initCarouselFilter(data)
