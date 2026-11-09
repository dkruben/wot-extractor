# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_results/presenters/packers/team/statistics_packer.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from copy import deepcopy as deepcopy
import typing as typing
from gui.battle_results.presenters.packers.team.stats_params_settings import REGULAR_PARAMETERS as REGULAR_PARAMETERS
from gui.impl.gen.view_models.views.lobby.battle_results.detailed_stats_parameter_model import DetailedStatsParameterModel as DetailedStatsParameterModel
from gui.battle_results.presenters.packers.interfaces import IStatisticsPacker as IStatisticsPacker
from gui.impl.gen.view_models.views.lobby.battle_results.simple_stats_parameter_model import SimpleStatsParameterModel as SimpleStatsParameterModel, RegularParamType as RegularParamType
from soft_exception import SoftException as SoftException
from frameworks.wulf import Array as Array
from gui.battle_results.stats_ctrl import BattleResults as BattleResults
from gui.battle_results.reusable.shared import VehicleSummarizeInfo as VehicleSummarizeInfo
from gui.battle_results.presenters.packers.team.stats_params_settings import _Parameter as _Parameter

class Statistics(IStatisticsPacker):
    __ALL_PARAMETERS: dict
    _STATS_PARAMETERS: tuple
    @classmethod
    def packModel(cls, model, info, battleResults):
        ...
    @classmethod
    def _getAllParameters(cls):
        ...
    @classmethod
    def _packParamLabel(cls, model, paramSettings):
        ...
    @classmethod
    def __packDetails(cls, detailsModel, paramType, info, battleResults):
        ...
    @classmethod
    def __packParameter(cls, model, paramSettings, info, battleResults):
        ...
    @classmethod
    def __packValue(cls, model, values):
        ...
