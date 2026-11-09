# wot-extractor: codigo DESCOMPILADO de sources/res/last_stand/scripts/client/last_stand/gui/scaleform/daapi/view/battle/battle_timers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: last_stand/scripts/client/last_stand/gui/scaleform/daapi/view/battle/battle_timers.py
from __future__ import absolute_import
import BigWorld
from gui.Scaleform.daapi.view.battle.shared import battle_timers
from gui.battle_control.battle_constants import COUNTDOWN_STATE
from gui.impl import backport
from gui.impl.gen import R
_HIDE_ALL_DELAY = 1.0

class PreBattleTimer(battle_timers.PreBattleTimer):

    def __init__(self):
        super(PreBattleTimer, self).__init__()
        self._hideAllCB = None
        self._arenaBonusType = None
        return

    def _dispose(self):
        self._clearHideAllCB()
        super(PreBattleTimer, self)._dispose()

    def updateBattleCtx(self, battleCtx):
        self._arenaBonusType = battleCtx.getArenaDP().getPersonalDescription().getArenaBonusType()
        super(PreBattleTimer, self).updateBattleCtx(battleCtx)

    def _getMessage(self):
        if self._state == COUNTDOWN_STATE.WAIT:
            return backport.text(R.strings.last_stand_battle.prebattle.waiting.title())
        difficulty = backport.text(R.strings.last_stand_battle.prebattle.difficulty.num(self._arenaBonusType)())
        return backport.text(R.strings.last_stand_battle.prebattle.description.title(), difficulty=difficulty)

    def _getWinConditionText(self, battleCtx):
        return self._getWinMessage()

    def _getWinMessage(self):
        messageId = R.strings.last_stand_battle.prebattle.description.message()
        return backport.text(messageId)

    def _onHideAll(self, speed):
        self._clearHideAllCB()
        self._hideAllCB = BigWorld.callback(_HIDE_ALL_DELAY, self._doHideAll)

    def _doHideAll(self):
        self._clearHideAllCB()
        self.as_hideAllS(False)

    def _clearHideAllCB(self):
        if self._hideAllCB is not None:
            BigWorld.cancelCallback(self._hideAllCB)
            self._hideAllCB = None
        return
