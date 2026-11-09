# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/meta/PrebattleTimerBaseMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/PrebattleTimerBaseMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class PrebattleTimerBaseMeta(BaseDAAPIComponent):

    def as_setTimerS(self, totalTime):
        if self._isDAAPIInited():
            return self.flashObject.as_setTimer(totalTime)

    def as_setMessageS(self, msg):
        if self._isDAAPIInited():
            return self.flashObject.as_setMessage(msg)

    def as_hideAllS(self, useAnim):
        if self._isDAAPIInited():
            return self.flashObject.as_hideAll(useAnim)

    def as_setWinConditionTextS(self, winCondition):
        if self._isDAAPIInited():
            return self.flashObject.as_setWinConditionText(winCondition)

    def as_togglePreBattleHighlightsVisibilityS(self, isVisible):
        if self._isDAAPIInited():
            return self.flashObject.as_togglePreBattleHighlightsVisibility(isVisible)
