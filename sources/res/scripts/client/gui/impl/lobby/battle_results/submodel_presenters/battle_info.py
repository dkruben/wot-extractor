# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/battle_results/submodel_presenters/battle_info.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/battle_results/submodel_presenters/battle_info.py
import typing
from gui.battle_results.pbs_helpers.common import getArenaNameStr, getRegularFinishResultResource
from gui.battle_results.presenters.battle_results_sub_presenter import BattleResultsSubPresenter
from gui.battle_results.settings import BATTLE_RESULTS_RECORD as _RECORD, PLAYER_TEAM_RESULT
from gui.impl.gen.view_models.views.lobby.battle_results.random.random_battle_info_model import RandomBattleInfoModel
if typing.TYPE_CHECKING:
    from frameworks.wulf import ViewModel
    from gui.battle_results.stats_ctrl import BattleResults

class BattleInfoSubPresenter(BattleResultsSubPresenter):

    @classmethod
    def getViewModelType(cls):
        return RandomBattleInfoModel

    def packBattleResults(self, battleResults):
        reusable, results = battleResults.reusable, battleResults.results
        common = results[_RECORD.COMMON]
        personal = results[_RECORD.PERSONAL]
        teamResult = reusable.getPersonalTeamResult()
        team = reusable.getPersonalTeam()
        winnerIfDraw = reusable.personal.avatar.winnerIfDraw
        if teamResult == PLAYER_TEAM_RESULT.DRAW and winnerIfDraw:
            if team == winnerIfDraw:
                teamResult = PLAYER_TEAM_RESULT.WIN
            else:
                teamResult = PLAYER_TEAM_RESULT.DEFEAT
        with self.getViewModel().transaction() as model:
            model.setArenaName(getArenaNameStr(reusable))
            model.setArenaGuiType(reusable.common.arenaGuiType)
            model.setBattleStartTime(common['arenaCreateTime'])
            model.setBattleDuration(common['duration'])
            model.setFinishReason(getRegularFinishResultResource(reusable.common.finishReason, teamResult))
            model.setFinishReasonKey(reusable.common.finishReason)
            model.setWinStatus(teamResult)
            model.setModeName(reusable.common.arenaType.getGamePlayName())
            model.setFinishReasonClarification('finishAllPlayersLeft' if reusable.common.finishAllPlayersLeft else '')
            model.setCommendationsReceived(personal[_RECORD.PERSONAL_AVATAR]['commendationsReceived'])
