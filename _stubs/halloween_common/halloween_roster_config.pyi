# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/common/halloween_common/halloween_roster_config.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from UnitRoster import BaseUnitRoster as BaseUnitRoster, BaseUnitRosterLimits as BaseUnitRosterLimits
from unit_roster_config import RosterSlot10 as RosterSlot10

class HalloweenRoster(BaseUnitRoster):
    MAX_SLOTS = 5
    MAX_EMPTY_SLOTS = 4
    SLOT_TYPE = RosterSlot10
    DEFAULT_SLOT_PACK: Any
    LIMITS_TYPE = BaseUnitRosterLimits
