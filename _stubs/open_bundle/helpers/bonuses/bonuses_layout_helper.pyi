# wot-extractor: STUB (.pyi) gerado a partir de sources/res/open_bundle/scripts/client/open_bundle/helpers/bonuses/bonuses_layout_helper.py (arvore sintatica do codigo descompilado/original).
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
from messenger.formatters.service_channel_helpers import getCustomizationItem as getCustomizationItem
from open_bundle.helpers.bonuses.bonuses_constants import BonusesLayoutAttrs as BonusesLayoutAttrs
from shared_utils import first as first
from typing import Any as Any, Dict as Dict, Optional as Optional, Union as Union
from gui.server_events.bonuses import CustomizationsBonus as CustomizationsBonus, GoodiesBonus as GoodiesBonus, ItemsBonus as ItemsBonus, LootBoxTokensBonus as LootBoxTokensBonus, SimpleBonus as SimpleBonus, TmanTemplateTokensBonus as TmanTemplateTokensBonus, TokensBonus as TokensBonus, VehicleBlueprintBonus as VehicleBlueprintBonus, VehiclesBonus as VehiclesBonus
_logger: _Any
_SUBTYPE_GETTERS: dict
_VALUE_GETTERS: dict

class BonusesHelper(object):
    @classmethod
    def getParameter(cls, bonus, source, parameter):
        ...
    @classmethod
    def __getSubType(cls, bonus):
        ...
    @classmethod
    def __getValue(cls, bonus, source):
        ...
    @staticmethod
    def __selectGetter(bonus, getters, default):
        ...

class _HelperTypes(str, Enum):
    RENT = 'rent'
    LOCKED_3D_STYLE = 'locked3DStyle'
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

class _BaseSubTypeGetter(object):
    @staticmethod
    def getSubType(bonus):
        ...

class _VehiclesSubTypeGetter(_BaseSubTypeGetter):
    @staticmethod
    def getSubType(bonus):
        ...

class _CustomizationSubTypeGetter(_BaseSubTypeGetter):
    @staticmethod
    def getSubType(bonus):
        ...

class _GoodiesSubTypeGetter(_BaseSubTypeGetter):
    @staticmethod
    def getSubType(bonus):
        ...

class _ItemsSubTypeGetter(_BaseSubTypeGetter):
    @staticmethod
    def getSubType(bonus):
        ...

class _TankmanSubTypeGetter(_BaseSubTypeGetter):
    @staticmethod
    def getSubType(bonus):
        ...

class _CurrenciesSubTypeGetter(_BaseSubTypeGetter):
    @staticmethod
    def getSubType(bonus):
        ...

class _BaseValueGetter(object):
    @classmethod
    def getValue(cls, bonus, _):
        ...

class _IntCDValueGetter(_BaseValueGetter):
    @classmethod
    def getValue(cls, bonus, _):
        ...

class _BlueprintValueGetter(_BaseValueGetter):
    @classmethod
    def getValue(cls, bonus, source):
        ...
    @staticmethod
    def __transformKey(key, bonus):
        ...

class _CustomizationValueGetter(_BaseValueGetter):
    @classmethod
    def getValue(cls, bonus, _):
        ...

class _VehiclesValueGetter(_BaseValueGetter):
    @classmethod
    def getValue(cls, bonus, _):
        ...

class _TankmanValueGetter(_BaseValueGetter):
    @classmethod
    def getValue(cls, bonus, _):
        ...

class _TokenValueGetter(_BaseValueGetter):
    @classmethod
    def getValue(cls, bonus, _):
        ...

class _LootBoxValueGetter(_BaseValueGetter):
    @classmethod
    def getValue(cls, bonus, _):
        ...
