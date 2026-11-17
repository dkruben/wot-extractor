# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/gui_items/loot_box.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from enum import Enum as Enum
from future.utils import iteritems as iteritems
from past.builtins import cmp as cmp
from typing import TYPE_CHECKING as TYPE_CHECKING
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.lootbox_system.base.common import getTextResource as getTextResource
from gui.shared.gui_items.gui_item import GUIItem as GUIItem
from helpers import dependency as dependency
from shared_utils import CONST_CONTAINER as CONST_CONTAINER
from skeletons.gui.game_control import ILootBoxSystemController as ILootBoxSystemController
from typing import Dict as Dict, Optional as Optional, Tuple as Tuple
_logger: Any
ALL_LUNAR_NY_LOOT_BOX_TYPES: tuple
LUNAR_NY_LOOT_BOXES_CATEGORIES = 'LunarNY'
SENIORITY_AWARDS_LOOT_BOXES_TYPE = 'seniorityAwards'

class NewYearLootBoxes(CONST_CONTAINER):
    PREMIUM = 'newYear_premium'

class WTLootBoxes(CONST_CONTAINER):
    WT_HUNTER = 'wt_hunter'
    WT_BOSS = 'wt_boss'
    WT_SPECIAL = 'wt_special'

class LunarNYLootBoxTypes(Enum):
    BASE = 'lunar_base'
    SIMPLE = 'lunar_simple'
    SPECIAL = 'lunar_special'

class LootBox(GUIItem):
    __slots__: tuple
    __lootBoxSystem: Any
    __id: Any
    __invCount: Any
    __isEnabled: Any
    __type: Any
    __category: Any
    __bonus: Any
    __statsName: Any
    __historyName: Any
    __guaranteedFrequencyName: Any
    __guaranteedFrequency: Any
    __probabilityBonusName: Any
    __probabilityBonusLimit: Any
    __rerollCurrency: Any
    __rerollPrices: Any
    __rerollMaxAttempts: Any
    __bonuses: Any
    def __init__(self, lootBoxID, lootBoxConfig, invCount):
        ...
    def __repr__(self):
        ...
    def updateCount(self, invCount):
        ...
    def update(self, lootBoxConfig):
        ...
    def getInventoryCount(self):
        ...
    def isEnabled(self):
        ...
    def getID(self):
        ...
    def getUserName(self):
        ...
    def getType(self):
        ...
    def getCategory(self):
        ...
    def isFree(self):
        ...
    def getBonusInfo(self):
        ...
    def getGuaranteedFrequency(self):
        ...
    def getGuaranteedFrequencyName(self):
        ...
    def getProbabilityBonusLimit(self):
        ...
    def getProbabilityBonusLimitName(self):
        ...
    def getHistoryName(self):
        ...
    def getStatsName(self):
        ...
    def getUseStats(self):
        ...
    def getRerollCurrency(self):
        ...
    def getRerollPrices(self):
        ...
    def getRerollMaxAttempts(self):
        ...
    def isRerollable(self):
        ...
    def _compare(self, other):
        ...
    def getBonuses(self):
        ...
    def __updateByConfig(self, lootBoxConfig):
        ...
    @staticmethod
    def __readProbabilityBonusLimit(limitsCfg):
        ...
    @staticmethod
    def __readFrequencyLimit(limitsCfg):
        ...
    @staticmethod
    def __readRerolls(rerollCfg):
        ...
