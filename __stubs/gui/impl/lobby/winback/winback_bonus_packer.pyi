# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/winback/winback_bonus_packer.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
import logging as logging
from collections import defaultdict as defaultdict, OrderedDict as OrderedDict
from copy import deepcopy as deepcopy
import typing as typing
from account_helpers.offers.offer_bonuses import NationalBlueprintOfferBonus as NationalBlueprintOfferBonus
from blueprints.BlueprintTypes import BlueprintTypes as BlueprintTypes
from blueprints.FragmentTypes import getFragmentType as getFragmentType
from goodies.goodie_constants import GOODIE_VARIETY as GOODIE_VARIETY
from gui.impl.auxiliary.rewards_helper import BlueprintBonusTypes as BlueprintBonusTypes
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.winback.discount_vehicle_bonus_model import DiscountVehicleBonusModel as DiscountVehicleBonusModel
from gui.impl.gen.view_models.views.lobby.winback.rent_vehicle_bonus_model import RentVehicleBonusModel as RentVehicleBonusModel, RentType as RentType
from gui.impl.gen.view_models.views.lobby.winback.vehicle_bonus_model import VehicleBonusModel as VehicleBonusModel
from gui.impl.gen.view_models.views.lobby.winback.vehicle_selectable_bonus_model import VehicleSelectableBonusModel as VehicleSelectableBonusModel
from gui.impl.gen.view_models.views.lobby.winback.winback_blueprint_bonus_model import WinbackBlueprintBonusModel as WinbackBlueprintBonusModel
from gui.impl.gen.view_models.views.lobby.winback.winback_reward_view_model import RewardName as RewardName
from gui.impl.lobby.battle_matters.battle_matters_bonus_packer import BattleMattersBlueprintBonusUIPacker as BattleMattersBlueprintBonusUIPacker
from gui.impl.lobby.winback.winback_bonuses import WinbackVehicleBonus as WinbackVehicleBonus, WinbackVehicleDiscountBonus as WinbackVehicleDiscountBonus, WinbackSelectableBonus as WinbackSelectableBonus
from gui.impl.lobby.winback.winback_helpers import getDiscountFromGoody as getDiscountFromGoody, getDiscountFromBlueprint as getDiscountFromBlueprint
from gui.server_events.bonuses import VehiclesBonus as VehiclesBonus, TokensBonus as TokensBonus, GoodiesBonus as GoodiesBonus, getNonQuestBonuses as getNonQuestBonuses
from gui.shared.gui_items.Vehicle import getNationLessName as getNationLessName
from gui.shared.missions.packers.bonus import BaseBonusUIPacker as BaseBonusUIPacker, BlueprintBonusUIPacker as BlueprintBonusUIPacker
from gui.shared.missions.packers.bonus import BonusUIPacker as BonusUIPacker
from gui.shared.missions.packers.bonus import getDefaultBonusPackersMap as getDefaultBonusPackersMap
from helpers import dependency as dependency
from skeletons.gui.game_control import IWinbackController as IWinbackController
from skeletons.gui.goodies import IGoodiesCache as IGoodiesCache
from skeletons.gui.shared import IItemsCache as IItemsCache
from typing import Any as Any, Callable as Callable, Dict as Dict, List as List, Optional as Optional
from frameworks.wulf.view.array import Array as Array
from gui.impl.backport import TooltipData as TooltipData
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
from gui.server_events.bonuses import SimpleBonus as SimpleBonus
_logger: _Any
WINBACK_DISCOUNTS = 'winbackDiscounts'
_BONUS_COUNT = 'count'
_RENT_MAP: dict

class WinbackVehiclesBonusUIPacker(BaseBonusUIPacker):
    _itemsCache: _Any
    @staticmethod
    def packSelectableVehicleReward(bonus):
        ...
    @classmethod
    def packVehicleRewards(cls, bonus):
        ...
    @classmethod
    def getToolTip(cls, bonus):
        ...
    @classmethod
    def _createVehicleModel(cls, vehCD, bonus):
        ...
    @classmethod
    def _getVehicleModel(cls, isRent):
        ...
    @staticmethod
    def _packVehicleModel(vehicle, bonus, model):
        ...
    @staticmethod
    def _packRentData(vehicle, bonus, model):
        ...
    @staticmethod
    def _packDiscountData(vehicle, bonus, model):
        ...
    @classmethod
    def _pack(cls, bonus):
        ...
    @classmethod
    def _getPackMethod(cls, name):
        ...

class WinbackBlueprintUIPacker(BlueprintBonusUIPacker):
    @classmethod
    def _pack(cls, bonus):
        ...
    @classmethod
    def _getBonusModel(cls):
        ...

class WinbackDiscountBonusUIPacker(WinbackVehiclesBonusUIPacker):
    @classmethod
    def _getVehicleModel(cls, _):
        ...
    @staticmethod
    def _packVehicleModel(vehicle, bonus, model):
        ...

def getWinbackMapping():
    ...
def getWinbackBonusPacker():
    ...
def getWinbackBonuses(bonuses, received=False):
    ...
def cutWinbackBonuses(bonusesData, winbackData=None, received=False):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def cutVehDiscountsFromBonuses(bonusesData, winbackData=None, received=False, goodiesCache=None, itemsCache=None):
    ...
def cutWinbackTokens(bonusesData, winbackData=None):
    ...
def cutVehicles(bonusesData, winbackData=None):
    ...
def _getCount(bonusData):
    ...
def handleWinbackBonusesData(bonuses):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def handleWinbackOfferTokens(bonuses, winbackController=None):
    ...
def handleWinbackDiscounts(bonuses):
    ...
def handleVehicleBonuses(bonuses):
    ...
def packWinbackBonusModelAndTooltipData(bonuses, packer, model, tooltipData=None, sort=None):
    ...
