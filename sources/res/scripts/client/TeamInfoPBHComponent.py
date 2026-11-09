# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/TeamInfoPBHComponent.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/TeamInfoPBHComponent.py
from __future__ import absolute_import
import logging, BattleReplay, BigWorld
from helpers import isPlayerAvatar, dependency
from script_component.DynamicScriptComponent import DynamicScriptComponent
from skeletons.gui.battle_session import IBattleSessionProvider
_logger = logging.getLogger(__name__)

class TeamInfoPBHComponent(DynamicScriptComponent):
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self, *_, **__):
        super(TeamInfoPBHComponent, self).__init__(*_, **__)
        _logger.debug('[PBH] TeamInfoPBHComponent init, winners: %s', self.winners)

    def _onAvatarReady(self):
        _logger.debug('[PBH] TeamInfoPBHComponent _onAvatarReady, winners: %s', self.winners)
        self.__updateWinnersInfo()

    def set_winners(self, _):
        _logger.debug('[PBH] TeamInfoPBHComponent set winners: %s', self.winners)
        if self._isAvatarReady:
            self.__updateWinnersInfo()

    def __updateWinnersInfo(self):
        _logger.debug('[PBH] TeamInfoPBHComponent update winners info: winners %s', self.winners)
        pbhCtrl = self.__sessionProvider.dynamic.prebattleHighlightsController
        if pbhCtrl is not None and not BattleReplay.isPlaying():
            winners = [self.__convertWinnerToDict(winner) for winner in self.winners]
            pbhCtrl.setWinnersStats(winners)
        return

    @classmethod
    def getInstance(cls):
        if not isPlayerAvatar():
            return
        else:
            player = BigWorld.player()
            if not player:
                return
            if not player.arena or not player.arena.teamInfo:
                return
            return getattr(player.arena.teamInfo, 'pbh', None)

    def __convertWinnerToDict(self, winner):
        winnerDict = {}
        winnerDict['id'] = winner['id']
        winnerDict['stats'] = {stat['name']: stat['value'] for stat in winner['stats']}
        return winnerDict
