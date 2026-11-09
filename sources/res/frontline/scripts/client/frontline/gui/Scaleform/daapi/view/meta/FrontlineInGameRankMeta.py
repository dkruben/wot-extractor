# wot-extractor: codigo DESCOMPILADO de sources/res/frontline/scripts/client/frontline/gui/Scaleform/daapi/view/meta/FrontlineInGameRankMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: frontline/scripts/client/frontline/gui/Scaleform/daapi/view/meta/FrontlineInGameRankMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class FrontlineInGameRankMeta(BaseDAAPIComponent):

    def levelUpAnimationComplete(self):
        self._printOverrideError('levelUpAnimationComplete')

    def as_triggerLevelUpS(self, previousProgress):
        if self._isDAAPIInited():
            return self.flashObject.as_triggerLevelUp(previousProgress)

    def as_updateProgressS(self, previousProgress, currentProgress):
        if self._isDAAPIInited():
            return self.flashObject.as_updateProgress(previousProgress, currentProgress)

    def as_setRankS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setRank(data)
