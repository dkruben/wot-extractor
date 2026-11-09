# wot-extractor: codigo DESCOMPILADO de sources/res/story_mode/scripts/client/story_mode/gui/scaleform/daapi/view/battle/game_messages_panel.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: story_mode/scripts/client/story_mode/gui/scaleform/daapi/view/battle/game_messages_panel.py
from __future__ import absolute_import
from gui.Scaleform.daapi.view.battle.shared.game_messages_panel import GameMessagesPanel, PlayerMessageData
from gui.Scaleform.genConsts.GAME_MESSAGES_CONSTS import GAME_MESSAGES_CONSTS
from gui.battle_control import avatar_getter
from gui.impl import backport
from gui.impl.gen import R

class StoreModeGameMessagesPanel(GameMessagesPanel):

    def sendEndGameMessage(self, winningTeam, reason):
        messageType = GAME_MESSAGES_CONSTS.WIN if avatar_getter.getPlayerTeam() == winningTeam else GAME_MESSAGES_CONSTS.DRAW
        rReason = R.strings.sm_battle.battleResult.reason
        endGameMsgData = {'title': (backport.text(R.strings.sm_battle.battleResult.resultLabel.dyn(messageType)())), 
           'subTitle': (backport.text(rReason.num(reason, rReason.default)()))}
        msg = PlayerMessageData(messageType, GAME_MESSAGES_CONSTS.DEFAULT_MESSAGE_LENGTH, GAME_MESSAGES_CONSTS.GAME_MESSAGE_PRIORITY_END_GAME, endGameMsgData)
        self._addMessage(msg.getDict())
