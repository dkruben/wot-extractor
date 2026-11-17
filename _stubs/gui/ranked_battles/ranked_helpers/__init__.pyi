# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/ranked_battles/ranked_helpers/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from collections import namedtuple as namedtuple
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.ranked_battles.constants import RANKED_QUEST_ID_PREFIX as RANKED_QUEST_ID_PREFIX, RankedTokenQuestPostfix as RankedTokenQuestPostfix, LOBBY_SUB_LANDING_PARAM as LOBBY_SUB_LANDING_PARAM, SEASON_RATING_PARAM as SEASON_RATING_PARAM, QUALIFICATION_QUEST as QUALIFICATION_QUEST
from gui.Scaleform.genConsts.RANKEDBATTLES_ALIASES import RANKEDBATTLES_ALIASES as RANKEDBATTLES_ALIASES
from gui.shared.utils.functions import makeTooltip as makeTooltip
from gui.shared.formatters import text_styles as text_styles
from helpers import dependency as dependency
from skeletons.gui.game_control import IRankedBattlesController as IRankedBattlesController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
_logger: Any
_AlertMessage: Any

def getBonusBattlesLabel(bonusBattlesCount):
    ...
def getBonusMultiplierLabel():
    ...
def getBonusBattlesIncome(resRoot, stepsCount, efficiencyCount, isStepsDaily):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getRankedBattlesSeasonRatingUrl(lobbyContext=None, spaID=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getRankedBattlesInfoPageUrl(lobbyContext=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getRankedBattlesIntroPageUrl(lobbyContext=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getRankedBattlesSeasonGapUrl(lobbyContext=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getRankedBattlesYearRatingUrl(lobbyContext=None, isLobbySub=False):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getRankedBattlesShopUrl(lobbyContext=None, isLobbySub=False):
    ...
def isSeasonTokenQuest(questID):
    ...
def isFinalTokenQuest(questID):
    ...
def isLeaderTokenQuest(questID):
    ...
def getDataFromSeasonTokenQuestID(questID):
    ...
def getDataFromFinalTokenQuestID(questID):
    ...
def getShieldSizeByRankSize(rankSize):
    ...
def isRankedQuestID(questID):
    ...
def makeStatTooltip(statKey):
    ...
def isQualificationQuestID(qID):
    ...
def getQualificationBattlesCountFromID(qID):
    ...
