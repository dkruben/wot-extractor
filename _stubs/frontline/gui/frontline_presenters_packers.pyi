# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline/gui/frontline_presenters_packers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
import json as json
from epic_constants import EPIC_BATTLE_TEAM_ID as EPIC_BATTLE_TEAM_ID
from frameworks.wulf.view.array import fillViewModelsArray as fillViewModelsArray
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.battle_results import stored_sorting as stored_sorting
from gui.battle_results.pbs_helpers.common import getTeamPlayerAchievements as getTeamPlayerAchievements
from gui.battle_results.presenters.packers.team.statistics_packer import Statistics as Statistics
from gui.battle_results.presenters.packers.team.team_stats_packer import TeamStats as TeamStats
from gui.battle_results.presenters.packers.user_info import AccountInfo as AccountInfo, PlayerInfo as PlayerInfo
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.battle_results.detailed_stats_parameter_model import DetailedStatsParameterModel as DetailedStatsParameterModel
from gui.impl.gen.view_models.views.lobby.battle_results.team_stats_model import SortingOrder as SortingOrder
from gui.impl.gen.view_models.views.lobby.battle_results.simple_stats_parameter_model import ValueType as ValueType
from gui.impl.lobby.common.vehicle_model_helpers import fillVehicleModel as fillVehicleModel
from gui.shared.gui_items.Vehicle import VEHICLE_TAGS as VEHICLE_TAGS
from gui.shared.system_factory import collectBattleResultsStatsSorting as collectBattleResultsStatsSorting
from frontline.gui.impl.gen.view_models.views.lobby.views.post_battle_results_view.player_model import PlayerModel as PlayerModel
from frontline.gui.impl.gen.view_models.views.lobby.views.post_battle_results_view.battle_team_stats_model import FrontlineColumnType as FrontlineColumnType
from frontline.gui.impl.gen.view_models.views.lobby.views.post_battle_results_view.achievement_model import AchievementModel as AchievementModel
from frontline.gui.impl.gen.view_models.views.lobby.views.post_battle_results_view.vehicle_stats_model import VehicleStatsModel as VehicleStatsModel
from frontline.gui.impl.gen.view_models.views.lobby.views.post_battle_results_view.vehicle_stats_model import FrontlineParamType as FrontlineParamType
from gui.battle_results.stats_ctrl import BattleResults as BattleResults
from frontline.gui.impl.gen.view_models.views.lobby.views.post_battle_results_view.battle_team_stats_model import BattleTeamStatsModel as BattleTeamStatsModel

class FrontlinePlayerInfo(PlayerInfo):
    __slots__: tuple
    @classmethod
    def packModel(cls, model, battleResults, vehicleSumInfo):
        ...
    @classmethod
    def _packAccountInfo(cls, model, battleResults, vehicleSumInfo):
        ...

class FrontlineTeamEfficiency(TeamStats):
    _PLAYER_MODEL_CLS = PlayerModel
    _PLAYER_INFO_PACKER = FrontlinePlayerInfo
    @classmethod
    def packModel(cls, model, battleResults):
        ...
    @classmethod
    def packPlayer(cls, playerModel, summarizeInfo, battleResults):
        ...
    @classmethod
    def packVehStatistics(cls, playerModel, summarizeInfo, battleResults):
        ...
    @classmethod
    def getAdditionalStatModel(cls, isTeamAttacker, key, val1, val2):
        ...
    @classmethod
    def _packSortingParams(cls, model, battleResults):
        ...

class FrontlineTeamAchievementsPacker(object):
    @classmethod
    def packModel(cls, playerAchievementsModel, summarizeInfo, battleResults):
        ...

def getAchievementResultsModel(achievement):
    ...
def getRankAchievementResultsModel(playerRank):
    ...
