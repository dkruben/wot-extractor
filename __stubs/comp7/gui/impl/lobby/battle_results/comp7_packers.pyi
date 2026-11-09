# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/battle_results/comp7_packers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from copy import deepcopy as deepcopy
import typing as typing
from comp7.gui.impl.gen.view_models.views.lobby.battle_results.comp7_detailed_stats_parameter_model import Comp7ParamType as Comp7ParamType
from comp7.gui.impl.lobby.battle_results.comp7_team_stats_params_settings import COMP7_PARAMETERS_UPDATE as COMP7_PARAMETERS_UPDATE
from comp7.gui.impl.lobby.comp7_helpers import comp7_shared as comp7_shared
from comp7.gui.impl.gen.view_models.views.lobby.battle_results.comp7_player_model import Comp7PlayerModel as Comp7PlayerModel
from comp7.gui.impl.gen.view_models.views.lobby.battle_results.comp7_stats_efficiency_model import Comp7StatsEfficiencyModel as Comp7StatsEfficiencyModel
from comp7.gui.impl.gen.view_models.views.lobby.battle_results.comp7_team_stats_model import Comp7ColumnType as Comp7ColumnType
from comp7.gui.impl.lobby.comp7_helpers.comp7_shared import getPlayerDivisionByRankAndIndex as getPlayerDivisionByRankAndIndex
from gui.battle_results import stored_sorting as stored_sorting
from gui.battle_results.presenters.packers.team.statistics_packer import Statistics as Statistics
from gui.battle_results.presenters.packers.team.stats_params_settings import REGULAR_PARAMETERS as REGULAR_PARAMETERS
from gui.battle_results.presenters.packers.team.team_stats_packer import TeamStats as TeamStats, TeamAchievementsPacker as TeamAchievementsPacker
from gui.battle_results.presenters.packers.user_info import AccountInfo as AccountInfo, PlayerInfo as PlayerInfo, UserStatus as UserStatus
from gui.impl.gen.view_models.views.lobby.battle_results.team_stats_model import SortingOrder as SortingOrder
from gui.shared.gui_items.Vehicle import VEHICLE_TAGS as VEHICLE_TAGS
from gui.shared.system_factory import collectBattleResultsStatsSorting as collectBattleResultsStatsSorting
from comp7.gui.impl.gen.view_models.views.lobby.battle_results.comp7_team_stats_model import Comp7TeamStatsModel as Comp7TeamStatsModel
from comp7_core.gui.battle_results.reusable.shared import Comp7CoreVehicleSummarizeInfo as Comp7CoreVehicleSummarizeInfo
from gui.battle_results.stats_ctrl import BattleResults as BattleResults
_VehicleTags: tuple

class Comp7PlayerInfo(PlayerInfo):
    __slots__: tuple
    @classmethod
    def packModel(cls, model, battleResults, vehicleSumInfo):
        ...
    @classmethod
    def _packAccountInfo(cls, model, battleResults, vehicleSumInfo):
        ...

class Comp7UserStatus(UserStatus):
    _USER_INFO_PACKER = AccountInfo

class Comp7Statistics(Statistics):
    __ALL_PARAMETERS: dict
    _STATS_PARAMETERS: Any
    @classmethod
    def _getAllParameters(cls):
        ...

class Comp7TeamEfficiency(TeamStats):
    _PLAYER_MODEL_CLS = Comp7PlayerModel
    _PLAYER_INFO_PACKER = Comp7PlayerInfo
    _STATS_PACKER = Comp7Statistics
    @classmethod
    def packModel(cls, model, battleResults):
        ...
    @classmethod
    def _packSortingParams(cls, model, battleResults):
        ...
    @classmethod
    def _packEfficiency(cls, efficiencyModel, summarizeInfo):
        ...
