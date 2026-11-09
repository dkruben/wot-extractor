# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/ranked_battles/ranked_builders/rewards_vos.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from gui.Scaleform.genConsts.RANKEDBATTLES_CONSTS import RANKEDBATTLES_CONSTS as RANKEDBATTLES_CONSTS
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.formatters import icons as icons, text_styles as text_styles
from gui.shared.utils.functions import makeTooltip as makeTooltip
from gui.Scaleform.genConsts.RANKEDBATTLES_ALIASES import RANKEDBATTLES_ALIASES as RANKEDBATTLES_ALIASES
from gui.ranked_battles.ranked_builders import shared_vos as shared_vos
from gui.ranked_battles.constants import STANDARD_POINTS_COUNT as STANDARD_POINTS_COUNT
from gui.ranked_battles.ranked_models import Rank as Rank, Division as Division
from gui.ranked_battles.constants import YearAwardsNames as YearAwardsNames

def getSeasonOnTabs(selectedLinkage, isYearRewardEnabled):
    ...
def getSeasonOffTabs(isYearRewardEnabled):
    ...
def __getRanksTab(selected, enabled):
    ...
def __getLeaguesTab(selected, enabled):
    ...
def __getYearRewardTab(selected, enabled):
    ...
def getDivisionVO(division):
    ...
def getRankRewardsVO(rank, bonuses, currentRankID):
    ...
def getLeagueRewardVO(leagueID, styleBonus, styleID, styleName, badgeID, isCurrent):
    ...
def getYearRewardDataVO(points, awards, rewardingComplete, awardType, compensation, exchange):
    ...
