# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/comp7_helpers/comp7_shared.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from shared_utils import findFirst as findFirst
from comp7.gui.impl.gen.view_models.views.lobby.enums import Division as Division, Rank as Rank
from helpers import dependency as dependency
from skeletons.gui.game_control import IComp7Controller as IComp7Controller
from comp7_ranks_common import Comp7Division as Comp7Division
from comp7.helpers.comp7_server_settings import Comp7RanksConfig as Comp7RanksConfig
from gui.shared.utils.requesters import RequestCriteria as RequestCriteria

def getDivisionEnumValue(division):
    ...
def getRankEnumValue(division):
    ...
def getRankById(rankId):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getRating(comp7Controller=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def isElite(seasonNumber=None, comp7Controller=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def isQualification(comp7Controller=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getPlayerDivisionByRating(rating, seasonNumber=None, comp7Controller=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getPlayerDivisionByRankAndIndex(rank, divisionIdx, comp7Controller=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getPlayerDivisionByDvsnID(dvsnId, comp7Controller=None):
    ...
def getPlayerDivision():
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def hasRankInactivity(rank, comp7Controller=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def hasPlayerRankInactivityWarning(comp7Controller=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getRankByName(rankName, comp7Controller=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getRankOrder(rank, comp7Controller=None):
    ...
def getComp7Criteria():
    ...
