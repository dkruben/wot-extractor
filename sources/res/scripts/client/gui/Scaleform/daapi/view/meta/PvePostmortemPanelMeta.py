# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/meta/PvePostmortemPanelMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/PvePostmortemPanelMeta.py
from gui.Scaleform.daapi.view.battle.shared.postmortem_panel import PostmortemPanel

class PvePostmortemPanelMeta(PostmortemPanel):

    def updateTime(self, value):
        self._printOverrideError('updateTime')

    def as_setHintTitleS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setHintTitle(value)

    def as_setHintDescrS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setHintDescr(value)

    def as_setTimerS(self, totalTime, currentTime):
        if self._isDAAPIInited():
            return self.flashObject.as_setTimer(totalTime, currentTime)

    def as_setCanExitS(self, canExit):
        if self._isDAAPIInited():
            return self.flashObject.as_setCanExit(canExit)

    def as_showLockedLivesS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_showLockedLives()

    def as_hidePanelS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hidePanel()
