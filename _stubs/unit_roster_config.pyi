# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/unit_roster_config.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from UnitRoster import BaseUnitRoster as BaseUnitRoster, BaseUnitRosterSlot as BaseUnitRosterSlot, BaseUnitRosterLimits as BaseUnitRosterLimits

class UnitRosterSlot(BaseUnitRosterSlot):
    DEFAULT_LEVELS: tuple

class UnitRoster(BaseUnitRoster):
    MAX_SLOTS = 7
    MAX_CLOSED_SLOTS = 0
    SLOT_TYPE = UnitRosterSlot
    DEFAULT_SLOT_PACK: Any
    MIN_UNIT_POINTS_SUM = 54
    MAX_UNIT_POINTS_SUM = 54
    MAX_UNIT_ASSEMBLER_ARTY = 2
    LIMITS_TYPE = BaseUnitRosterLimits

class RosterSlot6(BaseUnitRosterSlot):
    DEFAULT_LEVELS: tuple

class RosterSlot8(BaseUnitRosterSlot):
    DEFAULT_LEVELS: tuple

class RosterSlot10(BaseUnitRosterSlot):
    DEFAULT_LEVELS: tuple

class RosterSlot11(BaseUnitRosterSlot):
    DEFAULT_LEVELS: tuple

class EpicSlot(BaseUnitRosterSlot):
    DEFAULT_LEVELS: tuple

class Comp7Slot(BaseUnitRosterSlot):
    DEFAULT_LEVELS: tuple

class Comp7LightSlot(BaseUnitRosterSlot):
    DEFAULT_LEVELS: tuple

class SquadRoster(BaseUnitRoster):
    MAX_SLOTS = 3
    MAX_EMPTY_SLOTS = 2
    SLOT_TYPE = RosterSlot11
    DEFAULT_SLOT_PACK: Any
    LIMITS_TYPE = BaseUnitRosterLimits

class SpecRoster(BaseUnitRoster):
    MAX_SLOTS = 15
    MAX_EMPTY_SLOTS = 14
    SLOT_TYPE = RosterSlot11
    DEFAULT_SLOT_PACK: Any
    MAX_UNIT_POINTS_SUM = 150
    LIMITS_TYPE = BaseUnitRosterLimits

class EventRoster(BaseUnitRoster):
    MAX_SLOTS = 5
    MAX_EMPTY_SLOTS = 4
    SLOT_TYPE = RosterSlot10
    DEFAULT_SLOT_PACK: Any
    LIMITS_TYPE = BaseUnitRosterLimits

class EpicRoster(BaseUnitRoster):
    MAX_SLOTS = 3
    MAX_EMPTY_SLOTS = 2
    SLOT_TYPE = EpicSlot
    DEFAULT_SLOT_PACK: Any
    LIMITS_TYPE = BaseUnitRosterLimits
    MIN_VEHICLES = 1
    MAX_VEHICLES = 10000

class BattleRoyaleRoster(BaseUnitRoster):
    MAX_SLOTS = 2
    MAX_EMPTY_SLOTS = 1
    SLOT_TYPE = RosterSlot10
    DEFAULT_SLOT_PACK: Any
    LIMITS_TYPE = BaseUnitRosterLimits

class MapBoxRoster(BaseUnitRoster):
    MAX_SLOTS = 3
    MAX_EMPTY_SLOTS = 2
    SLOT_TYPE = RosterSlot10
    DEFAULT_SLOT_PACK: Any
    LIMITS_TYPE = BaseUnitRosterLimits

class Comp7Roster(BaseUnitRoster):
    MAX_SLOTS = 7
    MAX_EMPTY_SLOTS = 6
    SLOT_TYPE = Comp7Slot
    DEFAULT_SLOT_PACK: Any
    LIMITS_TYPE = BaseUnitRosterLimits
    MAX_VEHICLES = 10000

class Comp7LightRoster(BaseUnitRoster):
    MAX_SLOTS = 7
    MAX_EMPTY_SLOTS = 6
    SLOT_TYPE = Comp7LightSlot
    DEFAULT_SLOT_PACK: Any
    LIMITS_TYPE = BaseUnitRosterLimits
    MAX_VEHICLES = 10000
