# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/prb_windows/PrebattleUserCMHandler.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/prb_windows/PrebattleUserCMHandler.py
from __future__ import absolute_import
from adisp import adisp_process
from gui.Scaleform.locale.MENU import MENU
from gui.Scaleform.daapi.view.lobby.user_cm_handlers import AppealCMHandler
from gui.Scaleform.daapi.view.lobby.lobby_constants import USER
from gui.prb_control.entities.base.legacy.ctx import KickPlayerCtx
from gui.prb_control.entities.base.legacy.listener import ILegacyListener
from gui.shared.system_factory import registerLobbyContexMenuHandler
from messenger.m_constants import PROTO_TYPE
from messenger.proto import proto_getter
KICK_FROM_PREBATTLE = 'kickPlayerFromPrebattle'

def kickPlayerFromPrebattle(cm):
    cm.kickPlayerFromPrebattle(cm.databaseID)


registerLobbyContexMenuHandler(KICK_FROM_PREBATTLE, kickPlayerFromPrebattle)

class PrebattleUserCMHandler(AppealCMHandler, ILegacyListener):

    def __init__(self, cmProxy, ctx=None):
        super(PrebattleUserCMHandler, self).__init__(cmProxy, ctx)
        self._isCreator = self.prbEntity.isCommander()
        self.startPrbListening()

    @proto_getter(PROTO_TYPE.BW_CHAT2)
    def bwProto(self):
        return

    def fini(self):
        self._isCreator = None
        self.stopPrbListening()
        super(PrebattleUserCMHandler, self).fini()
        return

    def onPlayerRemoved(self, entity, playerInfo):
        self.onContextMenuHide()

    @adisp_process
    def kickPlayerFromPrebattle(self, databaseID):
        playerInfo = self.prbEntity.getPlayerInfoByDbID(databaseID)
        yield self.prbDispatcher.sendPrbRequest(KickPlayerCtx(playerInfo.accID, 'prebattle/kick'))

    def _addMutedInfo(self, options, userCMInfo):
        muted = USER.UNSET_MUTED if userCMInfo.isMuted else USER.SET_MUTED
        if not userCMInfo.isIgnored and self.bwProto.voipController.isVOIPEnabled():
            options.append(self._makeItem(muted, MENU.contextmenu(muted)))
        return options

    def _addPrebattleInfo(self, options, userCMInfo):
        disabled = self.prbEntity.getTeamState().isInQueue()
        if self._canKickPlayer():
            options.append(self._makeItem(KICK_FROM_PREBATTLE, MENU.contextmenu(KICK_FROM_PREBATTLE), {'enabled': (not disabled)}))
        return options

    def _canKickPlayer(self):
        playerInfo = self.prbEntity.getPlayerInfoByDbID(self.databaseID)
        team = self.prbEntity.getPlayerTeam(playerInfo.accID)
        return self.prbEntity.getPermissions().canKick(team)
