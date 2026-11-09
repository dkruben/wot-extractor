# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/meta/PrebattleTimerMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/PrebattleTimerMeta.py
from gui.Scaleform.daapi.view.battle.shared.prebattle_timers.timer_base import PreBattleTimerBase

class PrebattleTimerMeta(PreBattleTimerBase):

    def onShowInfo(self):
        self._printOverrideError('onShowInfo')

    def onHideInfo(self):
        self._printOverrideError('onHideInfo')

    def as_addInfoS(self, linkage, data):
        if self._isDAAPIInited():
            return self.flashObject.as_addInfo(linkage, data)

    def as_setInfoHintS(self, hint):
        if self._isDAAPIInited():
            return self.flashObject.as_setInfoHint(hint)

    def as_showInfoS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_showInfo()
