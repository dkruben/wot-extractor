# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/common/fun_random_common/fun_roster_config.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from UnitRoster import BaseUnitRoster as BaseUnitRoster, BaseUnitRosterLimits as BaseUnitRosterLimits
from unit_roster_config import RosterSlot11 as RosterSlot11

class FunRandomRoster(BaseUnitRoster):
    MAX_SLOTS = 3
    MAX_EMPTY_SLOTS = 2
    SLOT_TYPE = RosterSlot11
    DEFAULT_SLOT_PACK: Any
    LIMITS_TYPE = BaseUnitRosterLimits
