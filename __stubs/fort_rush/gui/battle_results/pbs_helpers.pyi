# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/client/fort_rush/gui/battle_results/pbs_helpers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Dict as Dict, TYPE_CHECKING as TYPE_CHECKING
from fort_rush_common.configs.fort_rush_battles_config import fortRushBattlesConfigGameParamsSchema as fortRushBattlesConfigGameParamsSchema
from fort_rush_common.fort_rush_constants import FINISH_REASON as FINISH_REASON
from fort_rush.skeletons.battle_controller import IFortRushBattleController as IFortRushBattleController
from helpers import dependency as dependency
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.battle_results.simple_stats_parameter_model import ValueType as ValueType, RegularParamType as RegularParamType
from gui.battle_results.pbs_helpers.team_stats_helpers import getStatsParamValue as getStatsParamValue
from gui.battle_results.presenters.packers.team.stats_params_settings import _Parameter as _Parameter
from gui.battle_results.reusable import _ReusableInfo as _ReusableInfo
FORT_RUSH_PARAMETERS_UPDATE: dict

def getProgressionPointsCountToShow(reusable):
    ...
def isProgressionPointsShown(value, hasFines, rewardValues, reusable):
    ...
def makeFortRushFinishResultLabel(finishReason, teamResult):
    ...
