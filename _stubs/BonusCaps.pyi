# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/BonusCaps.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from typing import Dict as Dict, Optional as Optional, Set as Set, FrozenSet as FrozenSet

class BonusCapsConst(object):
    CONFIG_NAME = 'bonus_caps_override_config'
    REMOVE = 'remove'
    ADD = 'add'
    OVERRIDE = 'override'

class BonusCapsConfig(object):
    __slots__: set
    __OPERATIONS: dict
    __config: Any
    def __init__(self, config=None):
        ...
    def __performOperations(self, arenaBonusType, defaultBonusCaps):
        ...
    def getModifiedBonusCaps(self, arenaBonusType, defaultBonusCaps):
        ...
