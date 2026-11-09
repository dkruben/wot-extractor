# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/battle_results_shared.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import struct as struct
from builtins import zip as zip
from future.utils import viewitems as viewitems
from past.builtins import xrange as xrange
from constants import PREMIUM_TYPE as PREMIUM_TYPE, PREM_BONUS_TYPES as PREM_BONUS_TYPES
VEH_INTERACTION_DETAILS: tuple
VEH_INTERACTION_DETAILS_NAMES: list
VEH_INTERACTION_DETAILS_MAX_VALUES: Any
VEH_INTERACTION_DETAILS_INIT_VALUES: list
VEH_INTERACTION_DETAILS_LAYOUT: Any
VEH_INTERACTION_DETAILS_INDICES: Any
VEH_INTERACTION_DETAILS_TYPES: Any
VEH_INTERACTIVE_STATS: tuple
VEH_INTERACTIVE_STATS_INDICES: Any
AVATAR_PRIVATE_STATS: tuple
AVATAR_PRIVATE_STATS_INDICES: Any
_PREM_TYPE_TO_FACTOR100_NAMES: dict

class UNIT_CLAN_MEMBERSHIP(object):
    NONE = 0
    ANY = 1
    SAME = 2

class _VehicleInteractionDetailsItem(object):
    __values: Any
    __offset: Any
    @staticmethod
    def __fmt2py(format):
        ...
    def __init__(self, values, offset):
        ...
    def __getitem__(self, key):
        ...
    def __setitem__(self, key, value):
        ...
    def __str__(self):
        ...
    def __iter__(self):
        ...

class VehicleInteractionDetails(object):
    __uniqueVehIDs: Any
    __values: Any
    __offsets: Any
    def __init__(self, uniqueVehIDs, values):
        ...
    @staticmethod
    def fromPacked(packed):
        ...
    def __getitem__(self, uniqueVehID):
        ...
    def __contains__(self, uniqueVehID):
        ...
    def __str__(self):
        ...
    def pack(self):
        ...
    def toDict(self):
        ...

def dictToList(indices, d):
    ...
def listToDict(names, l):
    ...
