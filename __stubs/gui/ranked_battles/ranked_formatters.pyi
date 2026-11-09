# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/ranked_battles/ranked_formatters.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.daapi.view.lobby.missions.awards_formatters import CurtailingAwardsComposer as CurtailingAwardsComposer
from gui.impl import backport as backport
from gui.ranked_battles.constants import AWARDS_ORDER as AWARDS_ORDER, DEFAULT_REWARDS_COUNT as DEFAULT_REWARDS_COUNT, YEAR_AWARDS_BONUS_ORDER as YEAR_AWARDS_BONUS_ORDER
from gui.server_events.awards_formatters import AWARDS_SIZES as AWARDS_SIZES, getRankedAwardsPacker as getRankedAwardsPacker
from gui.server_events.bonuses import getNonQuestBonuses as getNonQuestBonuses
from gui.shared.formatters import text_styles as text_styles
_UNAVAILABLE_VALUE = -1
_UNAVAILABLE_SYMBOL = '--'
_PERCENT_SYMBOL = '%'

class _RankedAwardsComposer(CurtailingAwardsComposer):
    _displayedRewardsCount: Any
    def __init__(self, displayedAwardsCount, context=None):
        ...
    def setMaxRewardsCount(self, maxRewardsCount):
        ...
    def getFormattedBonuses(self, bonuses, size=..., compareMethod=None):
        ...

class _BonusNameRankedAwardsComposer(_RankedAwardsComposer):
    def _packBonus(self, bonus, size=...):
        ...

def getFloatPercentStrStat(value):
    ...
def getIntegerStrStat(value):
    ...
def getTimeLongStr(value):
    ...
def getRankedAwardsFormatter(maxRewardsCount=...):
    ...
def getFormattedBonusesForYearAwardsWindow(rawRewards, maxRewardsCount=..., selectionsLeft=None):
    ...
def rankedYearAwardsSortFunction(b1, b2):
    ...
def _getOrderByBonusType(bonusName, order=...):
    ...
def _getValueOrUnavailable(targetValue):
    ...
def _sortBonusesFunc(b1, b2):
    ...
