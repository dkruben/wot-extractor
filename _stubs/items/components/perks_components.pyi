# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/items/components/perks_components.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
from functools import reduce as reduce
import typing as typing
from future.utils import viewitems as viewitems
from past.builtins import xrange as xrange
from items.components.perks_constants import PerkMasks as PerkMasks, PerkTags as PerkTags
from soft_exception import SoftException as SoftException
PerkArgument: Any

class Perk(object):
    __slots__: tuple
    id: Any
    flags: Any
    defaultBlockSettings: Any
    def __init__(self, ID, flags, args):
        ...
    @property
    def isAutoperk(self):
        ...
    def getArgBonusByLevel(self, argName, perkLevel):
        ...

class PerksCashe(dict):
    __slots__: tuple
    def validatePerk(self, perkID):
        ...

def convertPerksListToDict(perksList):
    ...
def convertPerksDictToList(perksDict):
    ...
def packPerk(perkID, level):
    ...
def unpackPerk(val):
    ...
