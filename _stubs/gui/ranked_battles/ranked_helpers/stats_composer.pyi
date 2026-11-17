# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/ranked_battles/ranked_helpers/stats_composer.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
import time as time
import typing as typing
from gui.ranked_battles.constants import RankedDossierKeys as RankedDossierKeys, ARCHIVE_SEASON_ID as ARCHIVE_SEASON_ID, ZERO_DIVISION_ID as ZERO_DIVISION_ID
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache
EfficiencyStamp: Any

class RankedBattlesStatsComposer(object):
    itemsCache: Any
    __slots__: tuple
    __settings: Any
    __currentSeason: Any
    def __init__(self, settings, currentSeason):
        ...
    @property
    def amountBattles(self):
        ...
    @property
    def amountBattlesInLeagues(self):
        ...
    @property
    def amountSteps(self):
        ...
    @property
    def amountStepsInLeagues(self):
        ...
    @property
    def bonusBattlesCount(self):
        ...
    @property
    def persistentBonusBattles(self):
        ...
    @property
    def dailyBonusBattles(self):
        ...
    @property
    def dailyBonusBattlesIncome(self):
        ...
    @property
    def cachedSeasonEfficiency(self):
        ...
    @property
    def currentSeasonEfficiency(self):
        ...
    @property
    def currentSeasonEfficiencyDiff(self):
        ...
    @property
    def divisionsStats(self):
        ...
    @property
    def hasSettings(self):
        ...
    def clear(self):
        ...
    def getDivisionEfficiencyPercent(self, divisionsID):
        ...
    def __getSeasonDossier(self):
        ...
