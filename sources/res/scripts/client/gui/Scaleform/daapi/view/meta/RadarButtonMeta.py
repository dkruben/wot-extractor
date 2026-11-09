# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/meta/RadarButtonMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/RadarButtonMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class RadarButtonMeta(BaseDAAPIComponent):

    def onClick(self):
        self._printOverrideError('onClick')

    def as_initS(self, keyCode, sfKeyCode, iconPath, tooltipText, isReplay):
        if self._isDAAPIInited():
            return self.flashObject.as_init(keyCode, sfKeyCode, iconPath, tooltipText, isReplay)

    def as_setCoolDownTimeS(self, duration, baseTime, startTime, animation):
        if self._isDAAPIInited():
            return self.flashObject.as_setCoolDownTime(duration, baseTime, startTime, animation)

    def as_updateEnableS(self, isEnabled):
        if self._isDAAPIInited():
            return self.flashObject.as_updateEnable(isEnabled)

    def as_setCoolDownPosAsPercentS(self, percent):
        if self._isDAAPIInited():
            return self.flashObject.as_setCoolDownPosAsPercent(percent)

    def as_setCoolDownTimeSnapshotS(self, time):
        if self._isDAAPIInited():
            return self.flashObject.as_setCoolDownTimeSnapshot(time)
