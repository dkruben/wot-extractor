# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_pass/battle_pass_bonuses_helper.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from future.utils import viewitems as viewitems
from battle_pass_common import BATTLE_PASS_TOKEN_BLUEPRINT_GIFT_OFFER as BATTLE_PASS_TOKEN_BLUEPRINT_GIFT_OFFER
from gui.battle_pass.battle_pass_constants import BonusesLayoutConsts as BonusesLayoutConsts
from gui.battle_pass.battle_pass_helpers import getOfferTokenByGift as getOfferTokenByGift
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.server_events.recruit_helper import getRecruitInfo as getRecruitInfo
from gui import makeHtmlString as makeHtmlString
from gui.server_events.bonuses import IntelligenceBlueprintBonus as IntelligenceBlueprintBonus, NationalBlueprintBonus as NationalBlueprintBonus, DossierBonus as DossierBonus
from gui.shared.formatters import icons as icons, text_styles as text_styles
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.money import Currency as Currency
from gui.shared.utils.requesters.blueprints_requester import getVehicleCDForIntelligence as getVehicleCDForIntelligence, getVehicleCDForNational as getVehicleCDForNational
from helpers import i18n as i18n, int2roman as int2roman, dependency as dependency
from items.tankmen import RECRUIT_TMAN_TOKEN_PREFIX as RECRUIT_TMAN_TOKEN_PREFIX
from shared_utils import first as first
from skeletons.gui.offers import IOffersDataProvider as IOffersDataProvider
from gui.server_events.bonuses import SimpleBonus as SimpleBonus, VehicleBlueprintBonus as VehicleBlueprintBonus, ItemsBonus as ItemsBonus, CurrenciesBonus as CurrenciesBonus, CustomizationsBonus as CustomizationsBonus, BattlePassSelectTokensBonus as BattlePassSelectTokensBonus, BattlePassStyleProgressTokenBonus as BattlePassStyleProgressTokenBonus, TokensBonus as TokensBonus, TmanTemplateTokensBonus as TmanTemplateTokensBonus
_logger: Any
_SUB_TYPE_GETTERS_MAP: dict
_VALUE_GETTERS_MAP: dict
_TEXT_GETTERS_MAP: dict

class BonusesHelper(object):
    @classmethod
    def getParameter(cls, bonus, source, parameter):
        ...
    @classmethod
    def getTextStrings(cls, bonus):
        ...
    @classmethod
    def __getSubType(cls, bonus):
        ...
    @classmethod
    def __getValue(cls, bonus, source):
        ...
    @staticmethod
    def __selectGetter(bonus, getters):
        ...

class _BaseSubTypeGetter(object):
    @staticmethod
    def getSubType(_):
        ...

class _ItemsSubTypeGetter(_BaseSubTypeGetter):
    @staticmethod
    def getSubType(bonus):
        ...

class _CustomizationSubTypeGetter(_BaseSubTypeGetter):
    @staticmethod
    def getSubType(bonus):
        ...

class _CurrenciesSubTypeGetter(_BaseSubTypeGetter):
    @staticmethod
    def getSubType(bonus):
        ...

class _RewardSelectSubTypeGetter(_BaseSubTypeGetter):
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

class _StyleProgressTokenValueGetter(_BaseValueGetter):
    @classmethod
    def getValue(cls, bonus, _):
        ...

class _VehiclesValueGetter(_BaseValueGetter):
    @classmethod
    def getValue(cls, bonus, _):
        ...

class _TokenValueGetter(_BaseValueGetter):
    @classmethod
    def getValue(cls, bonus, _):
        ...

class _TankmanValueGetter(_BaseValueGetter):
    @classmethod
    def getValue(cls, bonus, _):
        ...

class _BaseTextGetter(object):
    @staticmethod
    def getItems(bonus):
        ...
    @classmethod
    def getText(cls, item):
        ...

class _HtmlTextGetter(_BaseTextGetter):
    @classmethod
    def getText(cls, item):
        ...
    @staticmethod
    def _getPath():
        ...
    @staticmethod
    def _getKey(_):
        ...
    @staticmethod
    def _getContext(_):
        ...

class _CrewBookTextGetter(_HtmlTextGetter):
    @staticmethod
    def getItems(bonus):
        ...
    @staticmethod
    def _getKey(_):
        ...
    @staticmethod
    def _getContext(crewBook):
        ...

class _CrewSkinTextGetter(_HtmlTextGetter):
    @staticmethod
    def getItems(bonus):
        ...
    @staticmethod
    def _getKey(_):
        ...
    @staticmethod
    def _getContext(item):
        ...

class _DossierTextGetter(_HtmlTextGetter):
    @staticmethod
    def getItems(bonus):
        ...
    @staticmethod
    def _getKey(item):
        ...
    @staticmethod
    def _getContext(item):
        ...

class _SelectTokenTextGetter(_BaseTextGetter):
    __offersProvider: Any
    @classmethod
    def getText(cls, item):
        ...
    @classmethod
    def __getRealValue(cls, item):
        ...

class _StyleProgressTokenTextGetter(_BaseTextGetter):
    @classmethod
    def getText(cls, item):
        ...

class _TankmanTokenTextGetter(_BaseTextGetter):
    @classmethod
    def getText(cls, item):
        ...

class _RandomQuestTokenTextGetter(_BaseTextGetter):
    @classmethod
    def getText(cls, item):
        ...

class _LootboxTextGetter(_BaseTextGetter):
    @classmethod
    def getText(cls, item):
        ...

class _EquipCoinTextGetter(_BaseTextGetter):
    @classmethod
    def getText(cls, item):
        ...

class _CurrenciesTextGetter(_BaseTextGetter):
    @classmethod
    def getText(cls, item):
        ...

class _HelperConsts(object):
    HTML_BONUS_PATH = 'html_templates:lobby/quests/bonuses'
    CREW_BOOK_KEY = 'crewBookText'
    CREW_SKIN_KEY = 'crewSkinText'
    ACHIVE_KEY = 'dossierAchive'
    BADGE_KEY = 'dossierBadge'
    ACHIVE_TYPE = 'achive'
    BADGE_TYPE = 'badge'
    OPTIONAL_DEVICE_TYPE = 'optionalDevice'
    TROPHY_DEVICE_TYPE = 'trophyDevice'
    MODERNIZED_DEVICE_TYPE = 'modernizedDevice'
    CONSUMABLE_TYPE = 'consumable'
    CREW_BATTLE_BOOSTER_TYPE = 'crewBattleBooster'
    DEVICE_BATTLE_BOOSTER_TYPE = 'deviceBattleBooster'
    STYLE_3D_TYPE = 'style3D'
    LOCKED_STYLE = 'lockedStyle'
