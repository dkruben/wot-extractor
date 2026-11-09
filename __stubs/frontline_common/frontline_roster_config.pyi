# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/common/frontline_common/frontline_roster_config.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from UnitRoster import BaseUnitRoster as BaseUnitRoster, BaseUnitRosterLimits as BaseUnitRosterLimits, BaseUnitRosterSlot as BaseUnitRosterSlot

class EpicSlot(BaseUnitRosterSlot):
    DEFAULT_LEVELS: tuple

class EpicRoster(BaseUnitRoster):
    MAX_SLOTS = 3
    MAX_EMPTY_SLOTS = 2
    SLOT_TYPE = EpicSlot
    DEFAULT_SLOT_PACK: Any
    LIMITS_TYPE = BaseUnitRosterLimits
    MIN_VEHICLES = 1
    MAX_VEHICLES = 10000
