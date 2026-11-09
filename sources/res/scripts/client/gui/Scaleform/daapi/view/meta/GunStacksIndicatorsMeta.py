# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/meta/GunStacksIndicatorsMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/GunStacksIndicatorsMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class GunStacksIndicatorsMeta(BaseDAAPIComponent):

    def as_setVisibleS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setVisible(value)

    def as_setBonusS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setBonus(value)

    def as_setProgressS(self, idx, percent):
        if self._isDAAPIInited():
            return self.flashObject.as_setProgress(idx, percent)

    def as_setProgressAsPercentS(self, idx, percent):
        if self._isDAAPIInited():
            return self.flashObject.as_setProgressAsPercent(idx, percent)
