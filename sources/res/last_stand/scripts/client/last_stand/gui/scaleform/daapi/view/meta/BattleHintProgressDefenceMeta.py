# wot-extractor: codigo DESCOMPILADO de sources/res/last_stand/scripts/client/last_stand/gui/scaleform/daapi/view/meta/BattleHintProgressDefenceMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: last_stand/scripts/client/last_stand/gui/scaleform/daapi/view/meta/BattleHintProgressDefenceMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class BattleHintProgressDefenceMeta(BaseDAAPIComponent):

    def as_updateProgressS(self, value, progressValue, pointsLeft):
        if self._isDAAPIInited():
            return self.flashObject.as_updateProgress(value, progressValue, pointsLeft)

    def as_updateHealthPointsS(self, nextWavePoints):
        if self._isDAAPIInited():
            return self.flashObject.as_updateHealthPoints(nextWavePoints)

    def as_updateVehiclesS(self, vehicles):
        if self._isDAAPIInited():
            return self.flashObject.as_updateVehicles(vehicles)

    def as_handleAsReplayS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_handleAsReplay()
