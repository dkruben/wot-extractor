# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_modifiers/scripts/client/battle_modifiers/gui/feature/modifiers_data_provider.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
from typing import Tuple as Tuple, Any as Any, TYPE_CHECKING as TYPE_CHECKING
from battle_modifiers_ext.battle_modifiers import BattleModifiers as BattleModifiers
from battle_modifiers_ext.constants_ext import GameplayImpact as GameplayImpact
from battle_modifiers_ext.battle_modifiers import BattleModifier as BattleModifier

class ModifiersDataProvider(object):
    __slots__: tuple
    __modifiers: _Any
    __domains: _Any
    __modifiersByDomain: _Any
    def __init__(self, battleModifiersDescr=...):
        ...
    @classmethod
    def isHiddenModifier(cls, mod):
        ...
    def getDomains(self):
        ...
    def getDomainModifiers(self, domain):
        ...
    def getModifiers(self):
        ...
    def _readClientDomain(self, modifier):
        ...
