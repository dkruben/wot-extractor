# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/player_ranks.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from collections import namedtuple as namedtuple
from future.utils import viewitems as viewitems
from typing import NamedTuple as NamedTuple, Type as Type
from enum import Enum as Enum, unique as unique
import ResMgr as ResMgr
from constants import PLAYER_RANK as PLAYER_RANK, ARENA_BONUS_TYPE as ARENA_BONUS_TYPE
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS as ARENA_BONUS_TYPE_CAPS
from ResMgr import DataSection as DataSection
_CONFIG_FILE = 'scripts/item_defs/player_ranks.xml'
BonusSettings: Any
PlayerRanksSettings: Any
ALGORITHM_NAME_TO_SETTINGS: dict
ARENA_BONUS_TYPE_TO_SETTINGS_NAME: dict
g_cache = None

# decorador original: @unique
class ALGORITHM_NAMES(Enum):
    BASIC_THRESHOLD = 'BasicThreshold'
    NONE = 'None'

# decorador original: @unique
class SETTINGS_NAMES(Enum):
    DEFAULT = 'DEFAULT'
    NONE = 'None'
    @classmethod
    def hasValue(cls, value):
        ...

class AlgorithmSettings(object):
    initialRank: Any
    name: Any
    _initialRank: Any
    _name: Any
    def __init__(self, initialRank, section=None):
        ...

class BasicThresholdSettings(AlgorithmSettings):
    _BasicThresholdRankSettings: Any
    ranks: Any
    byOrder: Any
    byRank: Any
    orderByRank: Any
    def _readBasicThresholdRankSettings(self, section, order):
        ...
    def __init__(self, initialRank, section):
        ...

def makeBonusSettings(section=None):
    ...
def makePlayerRankSettings(section=None):
    ...
def init():
    ...
def parseRankFromSectionName(name, checkInPlayerRanks=True):
    ...
def getSettingsForBonusType(bonusType=None):
    ...
def getSettings(settingsName=...):
    ...
def getTresholdForRanks():
    ...
def getRank(progressValue):
    ...
