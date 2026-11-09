# wot-extractor: codigo DESCOMPILADO de sources/res/comp7_core/scripts/client/comp7_core/gui/Scaleform/daapi/view/meta/Comp7PrebattleTimerMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7_core/scripts/client/comp7_core/gui/Scaleform/daapi/view/meta/Comp7PrebattleTimerMeta.py
from gui.Scaleform.daapi.view.battle.shared.battle_timers import PreBattleTimer

class Comp7PrebattleTimerMeta(PreBattleTimer):

    def onReadyBtnClick(self):
        self._printOverrideError('onReadyBtnClick')

    def as_hideInfoS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideInfo()
