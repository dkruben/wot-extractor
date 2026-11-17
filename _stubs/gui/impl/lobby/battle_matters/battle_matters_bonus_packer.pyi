# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/battle_matters/battle_matters_bonus_packer.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import logging as logging
from constants import PREMIUM_ENTITLEMENTS as PREMIUM_ENTITLEMENTS
from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK as ACHIEVEMENT_BLOCK
from gui import GUI_NATIONS_ORDER_INDEX as GUI_NATIONS_ORDER_INDEX
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.battle_pass.battle_pass_bonuses_packers import ExtendedItemBonusUIPacker as ExtendedItemBonusUIPacker
from gui.impl.auxiliary.rewards_helper import BlueprintBonusTypes as BlueprintBonusTypes
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.Scaleform.genConsts.SLOT_HIGHLIGHT_TYPES import SLOT_HIGHLIGHT_TYPES as SLOT_HIGHLIGHT_TYPES
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.impl.gen.view_models.common.missions.bonuses.icon_bonus_model import IconBonusModel as IconBonusModel
from gui.impl.gen.view_models.views.lobby.battle_matters.battle_matters_vehicle_model import BattleMattersVehicleModel as BattleMattersVehicleModel
from gui.impl.gen.view_models.views.lobby.battle_matters.battle_matters_main_view_model import BattleMattersMainViewModel as BattleMattersMainViewModel
from gui.selectable_reward.constants import SELECTABLE_BONUS_NAME as SELECTABLE_BONUS_NAME
from gui.selectable_reward.bonus_packers import SelectableBonusPacker as SelectableBonusPacker
from gui.shared.missions.packers.bonus import DossierBonusUIPacker as DossierBonusUIPacker, VehiclesBonusUIPacker as VehiclesBonusUIPacker, getDefaultBonusPackersMap as getDefaultBonusPackersMap, BonusUIPacker as BonusUIPacker, BlueprintBonusUIPacker as BlueprintBonusUIPacker
from gui.shared.gui_items.Vehicle import getIconResourceName as getIconResourceName
from gui.shared.gui_items.Vehicle import getNationLessName as getNationLessName
from gui.shared.money import Currency as Currency
from gui.server_events.bonuses import VehiclesBonus as VehiclesBonus, BlueprintsBonusSubtypes as BlueprintsBonusSubtypes
from nations import NONE_INDEX as NONE_INDEX
from helpers import dependency as dependency
from skeletons.gui.battle_matters import IBattleMattersController as IBattleMattersController
from shared_utils import first as first
from gui.shared.missions.packers.bonus import BaseBonusUIPacker as BaseBonusUIPacker
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
from gui.impl.gen.view_models.views.lobby.battle_pass.reward_item_model import RewardItemModel as RewardItemModel
_logger: Any
_REWARDS_ORDER: tuple
_CUSTOMIZATIONS_ORDER: tuple
_DEVICES_TYPES_ORDER: tuple
_ITEMS_TYPES_ORDER: tuple
_CUSTOM_SORT_KEY: dict

class BattleMattersBlueprintBonusUIPacker(BlueprintBonusUIPacker):
    @classmethod
    def _pack(cls, bonus):
        ...
    @classmethod
    def _getNationalLbl(cls, bonus):
        ...

class BattleMattersTokenBonusUIPacker(SelectableBonusPacker):
    __battleMattersController: Any
    @classmethod
    def _packSingleBonus(cls, bonus):
        ...
    @classmethod
    def _getToolTip(cls, bonus):
        ...
    @classmethod
    def __isVehicleReceived(cls):
        ...
    @classmethod
    def _makeRewardItemModel(cls):
        ...
    @classmethod
    def _getTooltipSpecialAlias(cls):
        ...

class BattleMattersVehiclesBonusUIPacker(VehiclesBonusUIPacker):
    @classmethod
    def _packVehicleBonusModel(cls, bonus, vehInfo, isRent, vehicle):
        ...

class BattleMattersEntitlementsBonusUIPacker(BaseBonusUIPacker):
    _ITEMS_TO_SKIP: set
    @classmethod
    def _pack(cls, bonus):
        ...

class BattleMattersDossierBonusUIPacker(DossierBonusUIPacker):
    _ITEMS_TO_SKIP: set
    @classmethod
    def _packAchievements(cls, bonus):
        ...

def _vehiclesSortKey(model):
    ...
def _customizationsSortKey(model):
    ...
def _itemsSortKey(model):
    ...
def battleMattersSortKey(rewardType):
    ...
def bonusesSortKey(bonus):
    ...
def indexesSortKey(sequence, bonusName):
    ...
def blueprintsSortKey(bonus):
    ...
def _blueprintsNationSortKey(bonus):
    ...
def getBattleMattersBonusPacker():
    ...
