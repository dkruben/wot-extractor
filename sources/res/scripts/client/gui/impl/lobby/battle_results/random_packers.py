# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/battle_results/random_packers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/battle_results/random_packers.py
import typing
from gui.battle_results import stored_sorting
from gui.battle_results.presenters.packers.team.team_stats_packer import TeamStats, TeamAchievementsPacker
from gui.battle_results.presenters.packers.user_info import AccountInfo, PlayerInfo, UserStatus
from gui.impl.gen.view_models.views.lobby.battle_results.random.random_player_model import RandomPlayerModel
from gui.impl.gen.view_models.views.lobby.battle_results.random.random_team_stats_model import RandomColumnType
from gui.impl.gen.view_models.views.lobby.battle_results.team_stats_model import SortingOrder
from gui.shared.system_factory import collectBattleResultsStatsSorting
if typing.TYPE_CHECKING:
    from gui.battle_results.stats_ctrl import BattleResults
    from gui.impl.gen.view_models.views.lobby.battle_results.random.random_team_stats_model import RandomTeamStatsModel

class RandomPlayerInfo(PlayerInfo):
    __slots__ = ()

    @classmethod
    def packModel(cls, model, battleResults, vehicleSumInfo):
        super(RandomPlayerInfo, cls).packModel(model, battleResults, vehicleSumInfo)
        personalInfo = battleResults.reusable.getPlayerInfo()
        model.setPrebattleID(personalInfo.prebattleID if personalInfo.squadIndex else 0)
        TeamAchievementsPacker.packModel(model.getAchievements(), vehicleSumInfo, battleResults)

    @classmethod
    def _packAccountInfo(cls, model, battleResults, vehicleSumInfo):
        AccountInfo.packFullUserNames(model.userNames, vehicleSumInfo, battleResults)
        RandomUserStatus.packUserStatus(model.userStatus, battleResults, vehicleSumInfo)


class RandomUserStatus(UserStatus):
    _USER_INFO_PACKER = AccountInfo


class RandomTeamEfficiency(TeamStats):
    _PLAYER_MODEL_CLS = RandomPlayerModel
    _PLAYER_INFO_PACKER = RandomPlayerInfo

    @classmethod
    def packModel(cls, model, battleResults):
        allies, enemies = battleResults.reusable.getBiDirectionTeamsIterator(battleResults.results['vehicles'])
        cls._packTeam(model.getAllies(), allies, battleResults)
        cls._packTeam(model.getEnemies(), enemies, battleResults)
        cls._packSortingParams(model, battleResults)

    @classmethod
    def _packSortingParams(cls, model, battleResults):
        reusable = battleResults.reusable
        bonusType = reusable.common.arenaBonusType
        sortingKey = collectBattleResultsStatsSorting().get(bonusType)
        column, sortingOrder = stored_sorting.readStatsSorting(sortingKey)
        randomColumnValues = {item.value for item in RandomColumnType}
        model.setSortingOrder(SortingOrder(sortingOrder))
        model.setSortingColumn(RandomColumnType(column) if column in randomColumnValues else RandomColumnType.VEHICLE)
