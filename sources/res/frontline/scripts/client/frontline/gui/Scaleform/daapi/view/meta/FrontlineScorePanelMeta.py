# wot-extractor: codigo DESCOMPILADO de sources/res/frontline/scripts/client/frontline/gui/Scaleform/daapi/view/meta/FrontlineScorePanelMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: frontline/scripts/client/frontline/gui/Scaleform/daapi/view/meta/FrontlineScorePanelMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class FrontlineScorePanelMeta(BaseDAAPIComponent):

    def as_updateBasesS(self, west, center, east):
        if self._isDAAPIInited():
            return self.flashObject.as_updateBases(west, center, east)

    def as_updateHeadquarterHealthS(self, id, healthInPercent):
        if self._isDAAPIInited():
            return self.flashObject.as_updateHeadquarterHealth(id, healthInPercent)

    def as_headquarterDestroyedS(self, idx):
        if self._isDAAPIInited():
            return self.flashObject.as_headquarterDestroyed(idx)

    def as_updatePointsForBaseS(self, idx, points):
        if self._isDAAPIInited():
            return self.flashObject.as_updatePointsForBase(idx, points)

    def as_setTargetS(self, targetType, targetId):
        if self._isDAAPIInited():
            return self.flashObject.as_setTarget(targetType, targetId)

    def as_setPrebattleTimerS(self, remainingPrebattleTime):
        if self._isDAAPIInited():
            return self.flashObject.as_setPrebattleTimer(remainingPrebattleTime)
