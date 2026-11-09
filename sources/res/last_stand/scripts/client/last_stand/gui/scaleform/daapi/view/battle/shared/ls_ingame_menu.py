# wot-extractor: codigo DESCOMPILADO de sources/res/last_stand/scripts/client/last_stand/gui/scaleform/daapi/view/battle/shared/ls_ingame_menu.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: last_stand/scripts/client/last_stand/gui/scaleform/daapi/view/battle/shared/ls_ingame_menu.py
from __future__ import absolute_import
from BWUtil import AsyncReturn
import BattleReplay
from last_stand_common.last_stand_constants import ARENA_GUI_TYPE
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider
from wg_async import wg_async, wg_await
from gui.impl.gen import R
from LSArenaPhasesComponent import LSArenaPhasesComponent
from gui.Scaleform.daapi.view.battle.shared.ingame_menu import IngameMenu
from gui.Scaleform.daapi.view.battle.shared.premature_leave import showResDialogWindow, showLeaverReplayWindow
from gui.Scaleform.daapi.view.battle.shared.premature_leave import showExitWindow
from last_stand.gui.impl.battle.help_view import HelpWindow

@wg_async
def showLeaverAliveWindow(arenaGuiType):
    quitBattleR = R.strings.dialogs.lastStandQuitBattle
    title = quitBattleR.leaver.title()
    confirm = quitBattleR.leaver.submit()
    description = quitBattleR.leaver.descriptionAlive()
    icon = R.images.last_stand.gui.maps.icons.battle.deserterLeaveBattle()
    result = yield wg_await(showResDialogWindow(title, confirm=confirm, description=description, icon=icon))
    raise AsyncReturn(result)


class LSIngameMenu(IngameMenu):
    sessionProvider = dependency.descriptor(IBattleSessionProvider)

    @property
    def arenaPhases(self):
        return LSArenaPhasesComponent.getInstance()

    def helpClick(self):
        HelpWindow().load()

    @wg_async
    def _doLeaveArena(self):
        prematureLeave = self._isEventPrematureLeave()
        self.as_setVisibilityS(False)
        if BattleReplay.isPlaying():
            result = yield wg_await(showLeaverReplayWindow())
        elif prematureLeave:
            result = yield wg_await(showLeaverAliveWindow(self.sessionProvider.arenaVisitor.getArenaGuiType()))
        else:
            result = yield wg_await(showExitWindow())
        if result:
            self._doExit()
        else:
            self.destroy()

    def _isEventPrematureLeave(self):
        arenaPhases = self.arenaPhases
        if arenaPhases is None:
            return False
        else:
            lastPhase = arenaPhases.activePhase == arenaPhases.phasesCount
            inPostmortem = self.sessionProvider.shared.vehicleState.isInPostmortem
            if not arenaPhases.isRespawnEnabled and lastPhase and inPostmortem:
                return False
            return True
