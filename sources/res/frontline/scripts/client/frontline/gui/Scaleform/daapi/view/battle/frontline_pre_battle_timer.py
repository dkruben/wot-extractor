# wot-extractor: codigo DESCOMPILADO de sources/res/frontline/scripts/client/frontline/gui/Scaleform/daapi/view/battle/frontline_pre_battle_timer.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: frontline/scripts/client/frontline/gui/Scaleform/daapi/view/battle/frontline_pre_battle_timer.py
from __future__ import absolute_import
import BigWorld
from constants import ARENA_GUI_TYPE
from gui.impl import backport
from gui.Scaleform.daapi.view.battle.shared.prebattle_timers.timer_base import PreBattleTimerBase
from gui.impl.gen import R
from gui.shared.utils import functions

class FrontlinePreBattleTimer(PreBattleTimerBase):

    def updateBattleCtx(self, battleCtx):
        player = BigWorld.player()
        self._battleTypeStr = self.__getTitle()
        self.as_setMessageS(self._getMessage())
        if self._isDisplayWinCondition():
            self.as_setWinConditionTextS(functions.getBattleSubTypeWinText(player.arenaTypeID, player.team))

    @staticmethod
    def __getTitle():
        descriptionRes = R.strings.menu.loading.battleTypes.num(ARENA_GUI_TYPE.EPIC_BATTLE)
        if descriptionRes.exists():
            return backport.text(descriptionRes())
        return ''
