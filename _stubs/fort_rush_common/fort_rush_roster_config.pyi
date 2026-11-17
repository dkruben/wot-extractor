# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/common/fort_rush_common/fort_rush_roster_config.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from UnitRoster import BaseUnitRoster as BaseUnitRoster, BaseUnitRosterLimits as BaseUnitRosterLimits
from unit_roster_config import RosterSlot10 as RosterSlot10
from fort_rush_common.fort_rush_constants import MAX_ELIGIBLE_VEHICLES as MAX_ELIGIBLE_VEHICLES

class FortRushRoster(BaseUnitRoster):
    MAX_SLOTS = 3
    MAX_EMPTY_SLOTS = 2
    SLOT_TYPE = RosterSlot10
    DEFAULT_SLOT_PACK: Any
    LIMITS_TYPE = BaseUnitRosterLimits
    MAX_VEHICLES = MAX_ELIGIBLE_VEHICLES
