# wot-extractor: codigo DESCOMPILADO de sources/res/battle_royale/scripts/client/AccountBattleRoyaleTournamentComponent.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: battle_royale/scripts/client/AccountBattleRoyaleTournamentComponent.py
from __future__ import absolute_import
import logging, BigWorld
from helpers import dependency
from skeletons.gui.game_control import IBattleRoyaleTournamentController
import BattleRoyaleTournament
_logger = logging.getLogger(__name__)

class AccountBattleRoyaleTournamentComponent(BigWorld.StaticScriptComponent):
    __battleRoyaleTournamentController = dependency.descriptor(IBattleRoyaleTournamentController)

    def setParticipants(self, participants):
        _logger.debug("got tournament participants: '%r'", participants)
        self.__battleRoyaleTournamentController.updateParticipants(participants)

    def setTournamentToken(self, token):
        _logger.debug("got joined tournament token: '%r'", token)
        self.__battleRoyaleTournamentController.selectBattleRoyaleTournament(token)

    def tournamentJoin(self, tournamentID, callback=None):
        self.entity._doCmdIntStr(BattleRoyaleTournament.CMD_BATTLE_ROYALE_TRN_JOIN, 0, tournamentID, callback)

    def tournamentLeave(self, callback=None):
        self.entity._doCmdIntStr(BattleRoyaleTournament.CMD_BATTLE_ROYALE_TRN_LEAVE, 0, '', callback)

    def tournamentReady(self, vehInvID, tournamentID, callback=None):
        self.entity._doCmdIntStr(BattleRoyaleTournament.CMD_BATTLE_ROYALE_TRN_READY, vehInvID, tournamentID, callback)

    def tournamentNotReady(self, tournamentID, callback=None):
        self.entity._doCmdIntStr(BattleRoyaleTournament.CMD_BATTLE_ROYALE_TRN_NOT_READY, 0, tournamentID, callback)

    def tournamentForceStart(self, mapID, callback=None):
        self.entity._doCmdIntStr(BattleRoyaleTournament.CMD_BATTLE_ROYALE_TRN_START_BATTLE, mapID, '', callback)
