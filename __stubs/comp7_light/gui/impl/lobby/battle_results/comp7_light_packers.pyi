# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_light/scripts/client/comp7_light/gui/impl/lobby/battle_results/comp7_light_packers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from copy import deepcopy as deepcopy
import typing as typing
from comp7_light.gui.impl.gen.view_models.views.lobby.battle_results import comp7_light_detailed_stats_parameter_model as detailed_stats_model
from comp7_light.gui.impl.lobby.battle_results.comp7_light_team_stats_params_settings import COMP7_LIGHT_PARAMETERS_UPDATE as COMP7_LIGHT_PARAMETERS_UPDATE
from comp7_light.gui.impl.gen.view_models.views.lobby.battle_results.comp7_light_player_model import Comp7LightPlayerModel as Comp7LightPlayerModel
from comp7_light.gui.impl.gen.view_models.views.lobby.battle_results.comp7_light_stats_efficiency_model import Comp7LightStatsEfficiencyModel as Comp7LightStatsEfficiencyModel
from comp7_light.gui.impl.gen.view_models.views.lobby.battle_results.comp7_light_team_stats_model import Comp7LightColumnType as Comp7LightColumnType
from gui.battle_results import stored_sorting as stored_sorting
from gui.battle_results.presenters.packers.team.statistics_packer import Statistics as Statistics
from gui.battle_results.presenters.packers.team.stats_params_settings import REGULAR_PARAMETERS as REGULAR_PARAMETERS
from gui.battle_results.presenters.packers.team.team_stats_packer import TeamStats as TeamStats, TeamAchievementsPacker as TeamAchievementsPacker
from gui.battle_results.presenters.packers.user_info import AccountInfo as AccountInfo, PlayerInfo as PlayerInfo, UserStatus as UserStatus
from gui.impl.gen.view_models.views.lobby.battle_results.team_stats_model import SortingOrder as SortingOrder
from gui.shared.system_factory import collectBattleResultsStatsSorting as collectBattleResultsStatsSorting
from comp7_light.gui.impl.gen.view_models.views.lobby.battle_results.comp7_light_team_stats_model import Comp7LightTeamStatsModel as Comp7LightTeamStatsModel
from comp7_core.gui.battle_results.reusable.shared import Comp7CoreVehicleSummarizeInfo as Comp7CoreVehicleSummarizeInfo
from gui.battle_results.stats_ctrl import BattleResults as BattleResults

class Comp7LightPlayerInfo(PlayerInfo):
    __slots__: tuple
    @classmethod
    def packModel(cls, model, battleResults, vehicleSumInfo):
        ...
    @classmethod
    def _packAccountInfo(cls, model, battleResults, vehicleSumInfo):
        ...

class Comp7LightUserStatus(UserStatus):
    _USER_INFO_PACKER = AccountInfo

class Comp7LightStatistics(Statistics):
    __ALL_PARAMETERS: dict
    _STATS_PARAMETERS: Any
    @classmethod
    def _getAllParameters(cls):
        ...

class Comp7LightTeamEfficiency(TeamStats):
    _PLAYER_MODEL_CLS = Comp7LightPlayerModel
    _PLAYER_INFO_PACKER = Comp7LightPlayerInfo
    _STATS_PACKER = Comp7LightStatistics
    @classmethod
    def packModel(cls, model, battleResults):
        ...
    @classmethod
    def _packSortingParams(cls, model, battleResults):
        ...
    @classmethod
    def _packEfficiency(cls, efficiencyModel, summarizeInfo):
        ...
