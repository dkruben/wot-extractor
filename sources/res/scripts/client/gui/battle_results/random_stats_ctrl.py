# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/battle_results/random_stats_ctrl.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/battle_results/random_stats_ctrl.py
import typing
from constants import ARENA_BONUS_TYPE
from gui.battle_control.battle_constants import WinStatus
from gui.battle_results.settings import PLAYER_TEAM_RESULT
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider
from soft_exception import SoftException
from gui.battle_results.pbs_helpers.common import pushNoBattleResultsDataMessage
from gui.battle_results.stats_ctrl import IBattleResultStatsCtrl, BattleResults
from gui.shared.event_dispatcher import showBattleResultsWindow
if typing.TYPE_CHECKING:
    from gui.battle_results.reusable import _ReusableInfo

class RandomBattleResultStatsCtrl(IBattleResultStatsCtrl):
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self, _):
        self._battleResults = None
        return

    @property
    def ctrlImplType(self):
        return self.CTRL_IMPL_TYPE_GAMEFACE

    def clear(self):
        self._battleResults = None
        return

    def getVO(self):
        raise SoftException('Unsupported method')

    def setResults(self, results, reusable):
        self._battleResults = BattleResults(results, reusable)

    def getResults(self):
        return self._battleResults

    def onResultsPosted(self, arenaUniqueID):
        if self._battleResults:
            self.__setBattleContext()
            bonusType = self._battleResults.reusable.bonusType
            showBattleResultsWindow(arenaUniqueID, bonusType)
            return
        pushNoBattleResultsDataMessage()

    @staticmethod
    def onShowResults(arenaUniqueID):
        return

    def __setBattleContext(self):
        reusable = self._battleResults.reusable
        teamResult = reusable.getPersonalTeamResult()
        team = reusable.getPersonalTeam()
        winnerIfDraw = reusable.personal.avatar.winnerIfDraw
        if teamResult == PLAYER_TEAM_RESULT.DRAW and winnerIfDraw:
            if team == winnerIfDraw:
                winStatus = WinStatus.WIN
            else:
                winStatus = WinStatus.LOSE
            sessionCtx = self.__sessionProvider.getCtx()
            if sessionCtx.extractLastArenaWinStatus() is not None:
                sessionCtx.setLastArenaWinStatus(WinStatus(winStatus))
        return

    @classmethod
    def representativeArenaBonusType(cls):
        return ARENA_BONUS_TYPE.REGULAR
