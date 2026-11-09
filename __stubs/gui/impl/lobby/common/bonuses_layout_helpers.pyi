# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/common/bonuses_layout_helpers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
import logging as logging
from enum import Enum as Enum
from typing import TYPE_CHECKING as TYPE_CHECKING
from gui.server_events.bonuses import IntelligenceBlueprintBonus as IntelligenceBlueprintBonus, NationalBlueprintBonus as NationalBlueprintBonus
from gui.server_events.recruit_helper import getRecruitInfo as getRecruitInfo
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.utils.requesters.blueprints_requester import getVehicleCDForIntelligence as getVehicleCDForIntelligence, getVehicleCDForNational as getVehicleCDForNational
from shared_utils import first as first
from typing import Any as Any, Dict as Dict, Optional as Optional, Union as Union
from gui.server_events.bonuses import CustomizationsBonus as CustomizationsBonus, GoodiesBonus as GoodiesBonus, ItemsBonus as ItemsBonus, LootBoxTokensBonus as LootBoxTokensBonus, SimpleBonus as SimpleBonus, TmanTemplateTokensBonus as TmanTemplateTokensBonus, TokensBonus as TokensBonus, VehicleBlueprintBonus as VehicleBlueprintBonus, VehiclesBonus as VehiclesBonus
_logger: _Any

class BonusesLayoutAttrs(object):
    BONUSES = 'bonuses'
    DEFAULT = 'default'
    PRIORITY = 'priority'
    VISIBILITY = 'isVisible'
    OVERRIDE = 'override'
    RARITY = 'rarity'
    ID = 'id'
    MAIN: tuple

class _HelperTypes(str, Enum):
    RENT = 'rent'
    LOCKED_STYLE = 'lockedStyle'
    STYLE_3D = 'style3D'
    TROPHY_DEVICE = 'trophyDevice'
    MODERNIZED_DEVICE = 'modernizedDevice'
    IMPROVED_DEVICE = 'improvedDevice'
    OPTIONAL_DEVICE = 'optionalDevice'
    CREW_BATTLE_BOOSTER = 'crewBattleBooster'
    DEVICE_BATTLE_BOOSTER = 'deviceBattleBooster'
    CONSUMABLE = 'consumable'
    STIMULATOR = 'stimulator'
    DEMOUNT_KIT = 'demountKit'
    RECERTIFICATION_FORM = 'recertificationForm'
    MENTORING_LICENSE = 'mentoringLicense'
    TANKWOMAN = 'tankwoman'

class BonusesLayoutHelper(object):
    @classmethod
    def getParameter(cls, bonus, source, parameter, subTypeGetter=None, valueGetter=None):
        ...
    @classmethod
    def __getSubType(cls, bonus, subTypeGetter):
        ...
    @classmethod
    def __getValue(cls, bonus, source, valueGetter):
        ...
    @staticmethod
    def __selectGetter(bonus, getters, default):
        ...

class BaseSubTypeGetter(object):
    @staticmethod
    def getSubType(bonus):
        ...

class VehiclesSubTypeGetter(BaseSubTypeGetter):
    @staticmethod
    def getSubType(bonus):
        ...

class CustomizationSubTypeGetter(BaseSubTypeGetter):
    @staticmethod
    def getSubType(bonus):
        ...

class GoodiesSubTypeGetter(BaseSubTypeGetter):
    @staticmethod
    def getSubType(bonus):
        ...

class ItemsSubTypeGetter(BaseSubTypeGetter):
    @staticmethod
    def getSubType(bonus):
        ...

class TankmanSubTypeGetter(BaseSubTypeGetter):
    @staticmethod
    def getSubType(bonus):
        ...

class CurrenciesSubTypeGetter(BaseSubTypeGetter):
    @staticmethod
    def getSubType(bonus):
        ...

class BaseValueGetter(object):
    @classmethod
    def getValue(cls, bonus, _):
        ...

class IntCDValueGetter(BaseValueGetter):
    @classmethod
    def getValue(cls, bonus, _):
        ...

class BlueprintValueGetter(BaseValueGetter):
    @classmethod
    def getValue(cls, bonus, source):
        ...
    @staticmethod
    def __transformKey(key, bonus):
        ...

class CustomizationValueGetter(BaseValueGetter):
    @classmethod
    def getValue(cls, bonus, _):
        ...

class VehiclesValueGetter(BaseValueGetter):
    @classmethod
    def getValue(cls, bonus, _):
        ...

class TankmanValueGetter(BaseValueGetter):
    @classmethod
    def getValue(cls, bonus, _):
        ...

class TokenValueGetter(BaseValueGetter):
    @classmethod
    def getValue(cls, bonus, _):
        ...

class LootBoxValueGetter(BaseValueGetter):
    @classmethod
    def getValue(cls, bonus, _):
        ...

def getDefaultValueGetter():
    ...
def getDefaultSubTypeGetter():
    ...
