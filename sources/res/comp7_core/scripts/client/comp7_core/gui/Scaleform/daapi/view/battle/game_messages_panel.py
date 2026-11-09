# wot-extractor: codigo DESCOMPILADO de sources/res/comp7_core/scripts/client/comp7_core/gui/Scaleform/daapi/view/battle/game_messages_panel.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7_core/scripts/client/comp7_core/gui/Scaleform/daapi/view/battle/game_messages_panel.py
from __future__ import absolute_import
from gui.battle_control import avatar_getter
from helpers import dependency
from gui.Scaleform.daapi.view.battle.shared.game_messages_panel import GameMessagesPanel
from gui.impl import backport
from gui.impl.gen import R
from skeletons.gui.battle_session import IBattleSessionProvider
from comp7_core_constants import FINISH_REASON

class Comp7GameMessagesPanel(GameMessagesPanel):
    guiSessionProvider = dependency.descriptor(IBattleSessionProvider)

    def sendEndGameMessage(self, winningTeam, reason):
        if reason in FINISH_REASON.DRAW_RESOLVED_REASONS:
            isWinner = avatar_getter.getPlayerTeam() == winningTeam
            params = None
            if reason == FINISH_REASON.SURVIVORS_LEFT:
                battleFieldCtrl = self.guiSessionProvider.dynamic.battleField
                params = sorted([len(vehs) for vehs in battleFieldCtrl.getAliveVehicles()], reverse=isWinner)
            elif reason == FINISH_REASON.DAMAGE_DEALT:
                arena = avatar_getter.getArena()
                teamsDamageDealt = arena.arenaInfo.comp7.teamsDamageDealt if arena and arena.arenaInfo else [0, 0]
                params = sorted(list(teamsDamageDealt), reverse=isWinner)
            messageType = self._getMessageType(winningTeam)
            reasonKey = ('c_{}{}').format(reason, messageType)
            subTitle = backport.text(R.strings.battle_results.battle_finish.reason.dyn(reasonKey)())
            if params:
                subTitle = subTitle.format(*params)
            self._sendEndGameMessage(messageType, subTitle)
        super(Comp7GameMessagesPanel, self).sendEndGameMessage(winningTeam, reason)
        return
