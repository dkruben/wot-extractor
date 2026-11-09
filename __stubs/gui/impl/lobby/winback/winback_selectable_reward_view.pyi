# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/winback/winback_selectable_reward_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import OrderedDict as OrderedDict
from copy import deepcopy as deepcopy
from logging import getLogger as getLogger
import typing as typing
from AccountCommands import RES_SUCCESS as RES_SUCCESS
from PlayerEvents import g_playerEvents as g_playerEvents
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings, WindowFlags as WindowFlags, ViewStatus as ViewStatus
from gui import GUI_NATIONS as GUI_NATIONS, GUI_NATIONS_ORDER_INDEX as GUI_NATIONS_ORDER_INDEX
from gui.impl.auxiliary.rewards_helper import BlueprintBonusTypes as BlueprintBonusTypes
from gui.impl.backport import BackportTooltipWindow as BackportTooltipWindow, TooltipData as TooltipData
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.winback.winback_reward_view_model import RewardName as RewardName
from gui.impl.gen.view_models.views.lobby.winback.winback_selectable_reward_view_model import WinbackSelectableRewardViewModel as WinbackSelectableRewardViewModel
from gui.impl.lobby.battle_matters.popovers.battle_matters_filter_popover_view import BattleMattersFilterPopoverView as BattleMattersFilterPopoverView
from gui.impl.lobby.winback.tooltips.selectable_reward_tooltip import SelectableRewardTooltip as SelectableRewardTooltip
from gui.impl.lobby.winback.tooltips.selected_rewards_tooltip import SelectedRewardsTooltip as SelectedRewardsTooltip
from gui.impl.lobby.winback.winback_bonus_packer import handleWinbackDiscounts as handleWinbackDiscounts, handleVehicleBonuses as handleVehicleBonuses, cutVehDiscountsFromBonuses as cutVehDiscountsFromBonuses, getWinbackMapping as getWinbackMapping, WinbackBlueprintUIPacker as WinbackBlueprintUIPacker, WINBACK_DISCOUNTS as WINBACK_DISCOUNTS, WinbackDiscountBonusUIPacker as WinbackDiscountBonusUIPacker
from gui.impl.lobby.winback.winback_bonuses import WinbackSelectableBonus as WinbackSelectableBonus
from gui.impl.lobby.winback.winback_helpers import getLevelFromSelectableToken as getLevelFromSelectableToken, SelectableTypes as SelectableTypes, getNonCompensationToken as getNonCompensationToken
from gui.impl.lobby.winback.winback_reward_view import WinbackRewardWindow as WinbackRewardWindow
from gui.impl.pub import ViewImpl as ViewImpl, WindowImpl as WindowImpl
from gui.selectable_reward.common import WinbackSelectableRewardManager as WinbackSelectableRewardManager
from gui.server_events.bonuses import VehiclesBonus as VehiclesBonus
from gui.shared.missions.packers.bonus import packMissionsBonusModelAndTooltipData as packMissionsBonusModelAndTooltipData, BonusUIPacker as BonusUIPacker
from gui.shared.gui_items.Vehicle import VEHICLE_TYPES_ORDER as VEHICLE_TYPES_ORDER, getNationLessName as getNationLessName
from helpers import dependency as dependency
from nations import NONE_INDEX as NONE_INDEX
from shared_utils import first as first
from skeletons.gui.game_control import IWinbackController as IWinbackController
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui.impl.gen.view_models.views.lobby.winback.selectable_reward_category_model import SelectableRewardCategoryModel as SelectableRewardCategoryModel
from frameworks.wulf import Array as Array
from gui.impl.gen.view_models.common.bonus_model import BonusModel as BonusModel
_NATIONS_KEY_NAME = 'Nations'
_TYPES_KEY_NAME = 'Types'
_logger: Any
_TYPES_ORDER: tuple

class WinbackSelectableRewardView(ViewImpl):
    __slots__: tuple
    _selectableRewardManager = WinbackSelectableRewardManager
    _itemsCache: Any
    _winbackController: Any
    _packer: Any
    __bonuses: Any
    __filterPopover: Any
    __filters: Any
    __tooltipData: Any
    __selectedTab: Any
    def __init__(self, selectableTokens=None):
        ...
    @property
    def viewModel(self):
        ...
    def createPopOverContent(self, event):
        ...
    def createToolTip(self, event):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def onUpdateFilter(self, filters=None):
        ...
    def onTabChange(self, event):
        ...
    def onFilterReset(self):
        ...
    def onSelectReward(self, event):
        ...
    def onClaimRewards(self):
        ...
    def _update(self, selectableTokens):
        ...
    def _createTabBonuses(self, level, bonus):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _getEvents(self):
        ...
    def _deselect(self, selectedName):
        ...
    def _select(self, eventIdx, selectedName):
        ...
    def _updateTotalValues(self):
        ...
    def __getSelectedRewards(self):
        ...
    def __getOption(self, bonusType, opt):
        ...
    def __selectTab(self, tabName):
        ...
    def __update(self):
        ...
    def __updateRewards(self):
        ...
    @staticmethod
    def __getSelected(bonuses, options):
        ...
    def __getSelectedCount(self, tabName):
        ...
    @staticmethod
    def __createBlueprintItem(giftId, gift):
        ...
    @staticmethod
    def __createVehicleItem(giftId, opt, name, intCD, vehicle, option):
        ...
    def __isFilterEmpty(self, key):
        ...
    def __nationFit(self, veh):
        ...
    def __typeFit(self, veh):
        ...
    def __resetFilters(self, init=False):
        ...

class WinbackSelectableRewardWindow(WindowImpl):
    __slots__: tuple
    def __init__(self, selectableTokens=None, parent=None):
        ...

def getBonusPacker():
    ...
def _sortByNation(vehicleTuple):
    ...
def _sortByType(vehicleTuple):
    ...
def _sortByName(vehicleTuple):
    ...
def _sortAndClearVehicles(vehicles):
    ...
def _showRewardView(result):
    ...
