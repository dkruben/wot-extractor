# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/commendations_common/CommendationHelpers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from collections import namedtuple as namedtuple
import BigWorld as BigWorld
from constants import CommendationsState as CommendationsState, IS_CLIENT as IS_CLIENT, ARENA_PERIOD as ARENA_PERIOD
AVATAR_COMPONENT_NAME = 'commendations'
ARENA_COMPONENT_NAME = 'ArenaCommendationsMasterComponent'
ARENA_CONTROLLER_NAME = 'commendationsController'
TEAM_INFO_LIVETAGS_COMPONENT = 'liveTagsInfoComponent'
CommendationStatistics: Any
CommendationsStatisticsType: Any
CommendationStateType: Any

class CommendationsSource(object):
    EARS = 'ears'
    TAB_SCREEN = 'tab'
    CALLOUT = 'callout'

def canCommendNow(period):
    ...
def getCommendationState(vehicleID):
    ...
def getAvatarComponent(entity):
    ...
def getArenaComponent(entity):
    ...
def getArenaController(entity):
    ...
def getTeamInfoLiveTagsComponent(entity):
    ...
