# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/awards/packers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from adisp import adisp_async as adisp_async, adisp_process as adisp_process
from constants import RentType as RentType, OFFER_TOKEN_PREFIX as OFFER_TOKEN_PREFIX
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.impl import backport as backport
from gui.impl.backport import createTooltipData as createTooltipData, TooltipData as TooltipData
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.awards.reward_model import RewardModel as RewardModel, RentTypeEnum as RentTypeEnum
from gui.impl.lobby.awards import SupportedTokenTypes as SupportedTokenTypes
from gui.impl.lobby.awards.prefetch import TokenDataPrefetcher as TokenDataPrefetcher
from gui.impl.lobby.awards.tooltip import VEH_FOR_CHOOSE_ID as VEH_FOR_CHOOSE_ID
from gui.server_events.recruit_helper import getRecruitInfo as getRecruitInfo
from gui.shared.gui_items.Vehicle import getNationLessName as getNationLessName, getIconResourceName as getIconResourceName
from gui.shared.missions.packers.bonus import VehiclesBonusUIPacker as VehiclesBonusUIPacker, getDefaultBonusPackersMap as getDefaultBonusPackersMap, BaseBonusUIPacker as BaseBonusUIPacker, AsyncBonusUIPacker as AsyncBonusUIPacker, BACKPORT_TOOLTIP_CONTENT_ID as BACKPORT_TOOLTIP_CONTENT_ID, Customization3Dand2DbonusUIPacker as Customization3Dand2DbonusUIPacker, CustomizationBonusUIPacker as CustomizationBonusUIPacker, BonusUIPacker as BonusUIPacker
from gui.shared.utils.functions import makeTooltip as makeTooltip
from helpers import dependency as dependency, int2roman as int2roman
from items import tankmen as tankmen
from skeletons.gui.offers import IOffersDataProvider as IOffersDataProvider
from skeletons.gui.platform.catalog_service_controller import IPurchaseCache as IPurchaseCache
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui.platform.catalog_service.controller import _PurchaseDescriptor as _PurchaseDescriptor
from gui.server_events.bonuses import VehiclesBonus as VehiclesBonus, TokensBonus as TokensBonus, TmanTemplateTokensBonus as TmanTemplateTokensBonus
from gui.server_events.recruit_helper import _BaseRecruitInfo as _BaseRecruitInfo
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
from typing import Optional as Optional, Callable as Callable
VEH_COMP_R_ID: Any
_GAMEPLAY_TO_UI_RENT_MAPPING: dict
_LOCAL_FOLDER_NAME = 'multiple_awards'
_logger: Any

class _MultiProductAwardTokenBonusUIPacker(BaseBonusUIPacker):
    __offersProvider: Any
    __purchaseCache: Any
    __itemsCache: Any
    __productID: Any
    def __init__(self, productID):
        ...
    def isAsync(self):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def asyncPack(self, bonus, callback=None):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def asyncGetToolTip(self, bonus, callback=None):
        ...
    @classmethod
    def _getContentId(cls, bonus):
        ...

class MultiAwardVehiclesBonusUIPacker(VehiclesBonusUIPacker):
    _SPECIAL_ALIAS = TOOLTIPS_CONSTANTS.EXTENDED_AWARD_VEHICLE
    @classmethod
    def _packVehicleBonusModel(cls, bonus, vInfo, isRent, vehicle):
        ...
    @classmethod
    def _getContentId(cls, bonus):
        ...
    @classmethod
    def _getVehicleCompensationTooltipContent(cls):
        ...
    @classmethod
    def _packCompensationTooltip(cls, bonusComp, vehicle):
        ...
    @classmethod
    def _packTooltip(cls, bonus, vehicle, vehInfo):
        ...
    @classmethod
    def __convertCompensationTooltip(cls, bonusComp, vehicle, tooltipData):
        ...

class _TmanTemplateProductBonusPacker(BaseBonusUIPacker):
    __isBigImageUsed = False
    __productID: Any
    def __init__(self, productID):
        ...
    def isAsync(self):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def asyncPack(self, bonus, callback=None):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def asyncGetToolTip(self, bonus, callback=None):
        ...
    @classmethod
    def _getContentId(cls, bonus):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def _packTmanTemplateToken(self, tokenID, bonus, callback=None):
        ...
    @classmethod
    def _packTmanLocalTemplateToken(cls, tokenID):
        ...
    @classmethod
    def _getProductToken(cls, tokenName):
        ...
    @classmethod
    def __getBonusImageName(cls, recruitInfo):
        ...

class _AdditionalCustomizationBonusUIPacker(CustomizationBonusUIPacker):
    @classmethod
    def _packSingleBonus(cls, bonus, item, label):
        ...

def _convertRentType(gpRentType):
    ...
def _getOffersTokenStateData(offers):
    ...
def getVehicleUIData(vehicle):
    ...
def getMultipleProductAwardsBonusPacker(productCode):
    ...
def getAdditionalAwardsBonusPacker():
    ...
