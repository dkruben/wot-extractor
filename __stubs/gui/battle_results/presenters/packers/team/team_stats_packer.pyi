# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_results/presenters/packers/team/team_stats_packer.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS as _CAPS
from frameworks.wulf.view.array import fillViewModelsArray as fillViewModelsArray
from gui.battle_results import stored_sorting as stored_sorting
from gui.battle_results.pbs_helpers.common import getTeamPlayerAchievements as getTeamPlayerAchievements
from gui.battle_results.presenters.packers.interfaces import IBattleResultsPacker as IBattleResultsPacker
from gui.battle_results.presenters.packers.team.statistics_packer import Statistics as Statistics
from gui.battle_results.presenters.packers.user_info import PlayerInfo as PlayerInfo
from gui.impl.gen.view_models.views.lobby.battle_results.player_model import PlayerModel as PlayerModel
from gui.impl.gen.view_models.views.lobby.battle_results.team_stats_column_types import TeamStatsColumnTypes as TeamStatsColumnTypes
from gui.impl.gen.view_models.views.lobby.battle_results.team_stats_model import TeamStatsModel as TeamStatsModel, SortingOrder as SortingOrder
from gui.impl.lobby.common.vehicle_model_helpers import fillVehicleModel as fillVehicleModel
from gui.shared.gui_items.Vehicle import VEHICLE_TAGS as VEHICLE_TAGS
from gui.shared.system_factory import collectBattleResultsStatsSorting as collectBattleResultsStatsSorting
from gui.impl.gen.view_models.views.lobby.battle_results.postbattle_achievement_model import PostbattleAchievementModel as PostbattleAchievementModel
from frameworks.wulf import Array as Array
from gui.battle_results.pbs_helpers.common import _AchievementData as _AchievementData
from gui.battle_results.reusable import _ReusableInfo as _ReusableInfo
from gui.battle_results.stats_ctrl import BattleResults as BattleResults
from gui.battle_results.reusable.shared import VehicleSummarizeInfo as VehicleSummarizeInfo
from gui.impl.gen.view_models.views.lobby.battle_results.stats_efficiency_model import StatsEfficiencyModel as StatsEfficiencyModel
_VehicleTags: tuple

class TeamStats(IBattleResultsPacker):
    _PLAYER_MODEL_CLS = PlayerModel
    _PLAYER_INFO_PACKER = PlayerInfo
    _STATS_PACKER = Statistics
    _STATS_VALUES_COLUMNS: dict
    _SORTING_PRIORITIES: tuple
    @classmethod
    def packModel(cls, model, battleResults):
        ...
    @classmethod
    def packPlayer(cls, playerModel, summarizeInfo, battleResults):
        ...
    @classmethod
    def _getAlternativeSortingParams(cls, reusable):
        ...
    @classmethod
    def _packEfficiency(cls, efficiencyModel, summarizeInfo):
        ...
    @classmethod
    def _packSortingParams(cls, model, battleResults):
        ...
    @classmethod
    def _packShownColumns(cls, columnsModel, battleResults):
        ...
    @classmethod
    def _packTeam(cls, teamModel, teamData, battleResults):
        ...

class TeamAchievementsPacker(object):
    @classmethod
    def packModel(cls, playerAchievementsModel, summarizeInfo, battleResults):
        ...
    @classmethod
    def __setAchievementsResults(cls, achievement):
        ...
