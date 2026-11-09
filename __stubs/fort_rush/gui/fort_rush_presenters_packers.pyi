# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/client/fort_rush/gui/fort_rush_presenters_packers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from copy import deepcopy as deepcopy
from fort_rush.gui.battle_results.pbs_helpers import getProgressionPointsCountToShow as getProgressionPointsCountToShow, isProgressionPointsShown as isProgressionPointsShown, FORT_RUSH_PARAMETERS_UPDATE as FORT_RUSH_PARAMETERS_UPDATE
from fort_rush.gui.impl.gen.view_models.views.lobby.post_battle_results_view.battle_team_stats_model import FortRushColumnType as FortRushColumnType
from fort_rush.gui.impl.gen.view_models.views.lobby.post_battle_results_view.detailed_personal_efficiency_item_model import DetailedPersonalEfficiencyItemModel as DetailedPersonalEfficiencyItemModel
from fort_rush.gui.impl.gen.view_models.views.lobby.post_battle_results_view.fort_rush_reward_item_model import FortRushRewardTypes as FortRushRewardTypes, FortRushRewardItemModel as FortRushRewardItemModel
from fort_rush.gui.impl.gen.view_models.views.lobby.post_battle_results_view.player_model import PlayerModel as PlayerModel
from fort_rush.gui.impl.gen.view_models.views.lobby.post_battle_results_view.vehicle_stats_model import VehicleStatsModel as VehicleStatsModel
from gui.battle_results import stored_sorting as stored_sorting
from gui.battle_results.pbs_helpers.economics import getTotalCreditsToShow as getTotalCreditsToShow
from gui.battle_results.presenters.packers.personal_efficiency import PersonalEfficiency as PersonalEfficiency
from gui.battle_results.presenters.packers.personal_rewards import PersonalRewards as PersonalRewards
from gui.battle_results.presenters.packers.team.statistics_packer import Statistics as Statistics
from gui.battle_results.presenters.packers.team.stats_params_settings import REGULAR_PARAMETERS as REGULAR_PARAMETERS
from gui.battle_results.presenters.packers.team.team_stats_packer import TeamStats as TeamStats
from gui.battle_results.presenters.packers.user_info import AccountInfo as AccountInfo, PlayerInfo as PlayerInfo
from gui.impl.gen.view_models.views.lobby.battle_results.simple_stats_parameter_model import RegularParamType as RegularParamType
from gui.impl.gen.view_models.views.lobby.battle_results.team_stats_model import SortingOrder as SortingOrder
from gui.impl.lobby.common.vehicle_model_helpers import fillVehicleModel as fillVehicleModel
from gui.shared.system_factory import collectBattleResultsStatsSorting as collectBattleResultsStatsSorting
from gui.battle_results.stats_ctrl import BattleResults as BattleResults
from fort_rush.gui.battle_results.reusable.fort_rush_shared import FortRushVehicleSummarizeInfo as FortRushVehicleSummarizeInfo
from fort_rush.gui.impl.gen.view_models.views.lobby.post_battle_results_view.fort_rush_stats_efficiency_model import FortRushStatsEfficiencyModel as FortRushStatsEfficiencyModel
from fort_rush.gui.impl.gen.view_models.views.lobby.post_battle_results_view.battle_team_stats_model import BattleTeamStatsModel as BattleTeamStatsModel

class FortRushPersonalEfficiency(PersonalEfficiency):
    _DEFAULT_PARAMS: tuple
    _VALUE_EXTRACTORS: dict
    _EFFICIENCY_ITEM_MODEL_CLS = DetailedPersonalEfficiencyItemModel
    @classmethod
    def _createParameterModel(cls, parameter, vehicleInfo):
        ...

class FortRushPlayerInfo(PlayerInfo):
    __slots__: tuple
    @classmethod
    def _packAccountInfo(cls, model, battleResults, vehicleSumInfo):
        ...

class FortRushPersonalRewards(PersonalRewards):
    _AVAILABLE_REWARDS: list
    _ITEM_MODEL_CLS = FortRushRewardItemModel
    _REWARD_GETTERS: dict
    _REWARDS_TO_CONDITION_MAP: dict

class FortRushStatisticsPacker(Statistics):
    __ALL_PARAMETERS: dict
    _STATS_PARAMETERS: tuple
    @classmethod
    def _getAllParameters(cls):
        ...

class FortRushTeamEfficiency(TeamStats):
    _PLAYER_MODEL_CLS = PlayerModel
    _PLAYER_INFO_PACKER = FortRushPlayerInfo
    @classmethod
    def packModel(cls, model, battleResults):
        ...
    @classmethod
    def packPlayer(cls, playerModel, summarizeInfo, battleResults):
        ...
    @classmethod
    def _packEfficiency(cls, efficiencyModel, summarizeInfo):
        ...
    @classmethod
    def packVehStatistics(cls, playerModel, summarizeInfo, battleResults):
        ...
    @classmethod
    def _packSortingParams(cls, model, battleResults):
        ...
