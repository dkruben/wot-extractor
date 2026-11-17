# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/comp7_helpers/comp7_model_helpers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from future.utils import viewvalues as viewvalues
from comp7.gui.impl.gen.view_models.views.lobby.enums import Rank as Rank
from comp7.gui.impl.lobby.comp7_helpers import comp7_shared as comp7_shared
from helpers import dependency as dependency
from skeletons.gui.game_control import IComp7Controller as IComp7Controller
from comp7.gui.impl.gen.view_models.views.lobby.enums import SeasonName as SeasonName
from typing import Optional as Optional
from comp7.helpers.comp7_server_settings import Comp7RanksConfig as Comp7RanksConfig
from comp7_ranks_common import Comp7Division as Comp7Division
from comp7.gui.impl.gen.view_models.views.lobby.division_info_model import DivisionInfoModel as DivisionInfoModel
_logger: Any
SEASONS_NUMBERS_BY_NAME: dict

def setDivisionInfo(model, division=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def setRanksInactivityInfo(model, comp7Controller=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def setElitePercentage(model, comp7Controller=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def setRankInfo(model, comp7Controller=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getYearlyRewardsRank(comp7Controller=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def setMaxRankInfo(model, comp7Controller=None):
    ...
