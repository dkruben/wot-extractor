# wot-extractor: codigo DESCOMPILADO de sources/res/halloween/scripts/client/halloween/gui/scaleform/daapi/view/meta/HWBossIndicatorProgressMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: halloween/scripts/client/halloween/gui/scaleform/daapi/view/meta/HWBossIndicatorProgressMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class HWBossIndicatorProgressMeta(BaseDAAPIComponent):

    def as_setValueS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setValue(value)

    def as_setIndicatorEnabledS(self, isEnabled):
        if self._isDAAPIInited():
            return self.flashObject.as_setIndicatorEnabled(isEnabled)

    def as_setAlphaS(self, alpha):
        if self._isDAAPIInited():
            return self.flashObject.as_setAlpha(alpha)
