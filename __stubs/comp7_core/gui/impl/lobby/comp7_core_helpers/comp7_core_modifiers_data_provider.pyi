# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_core/scripts/client/comp7_core/gui/impl/lobby/comp7_core_helpers/comp7_core_modifiers_data_provider.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
from typing import Tuple as Tuple, Any as Any, List as List
from battle_modifiers.gui.feature.modifiers_data_provider import ModifiersDataProvider as ModifiersDataProvider
from battle_modifiers_ext.constants_ext import GameplayImpact as GameplayImpact

class Comp7CoreModifiersDataProvider(ModifiersDataProvider):
    __slots__: tuple
    _domain: _Any
    def __init__(self, domain, modifiers=...):
        ...
    @classmethod
    def isHiddenModifier(cls, mod):
        ...
    def _readClientDomain(self, modifier):
        ...

class Comp7CoreSubModifiers(object):
    __slots__: tuple
    __subModesProviders: _Any
    def __init__(self, subModifiers=...):
        ...
    @property
    def providers(self):
        ...
