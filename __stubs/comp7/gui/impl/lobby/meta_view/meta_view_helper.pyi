# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/meta_view/meta_view_helper.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from comp7.gui.impl.gen.view_models.views.lobby.enums import Division as Division, Rank as Rank
from comp7.gui.impl.gen.view_models.views.lobby.progression_division import ProgressionDivision as ProgressionDivision, State as State
from comp7.gui.impl.lobby.comp7_helpers import comp7_shared as comp7_shared
from helpers import dependency as dependency
from intervals import Interval as Interval
from skeletons.gui.game_control import IComp7Controller as IComp7Controller
from comp7_ranks_common import Comp7Division as Comp7Division
from comp7.gui.impl.gen.view_models.views.lobby.meta_view.progression_base_model import ProgressionBaseModel as ProgressionBaseModel
from comp7.gui.impl.gen.view_models.views.lobby.progression_item_base_model import ProgressionItemBaseModel as ProgressionItemBaseModel
from comp7.helpers.comp7_server_settings import Comp7RanksConfig as Comp7RanksConfig
_logger: Any

def setRankItemData(itemModel, rankIdx, ranksConfig):
    ...
def setProgressionItemData(itemModel, parentModel, rankIdx, ranksConfig):
    ...
def setRankData(itemModel, rank, ranksConfig):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def setCurrentProgressionIdx(model, rank, ranksConfig, rating=None, comp7Controller=None):
    ...
def getRankDivisions(rank, ranksConfig):
    ...
def setDivisionData(itemModel, divisions, rating=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getDivisionState(division, rating=None, comp7Controller=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getEliteRank(comp7Controller=None):
    ...
