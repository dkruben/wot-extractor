# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/battle_matters/battle_matters_vehicle_selection_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import OrderedDict as OrderedDict
from functools import partial as partial
from future.utils import iteritems as iteritems, itervalues as itervalues, viewitems as viewitems
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings, ViewStatus as ViewStatus
from gui import GUI_NATIONS_ORDER_INDEX as GUI_NATIONS_ORDER_INDEX, GUI_NATIONS as GUI_NATIONS
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.battle_matters.battle_matters_vehicle_selection_view_model import BattleMattersVehicleSelectionViewModel as BattleMattersVehicleSelectionViewModel
from gui.impl.lobby.battle_matters.popovers.battle_matters_filter_popover_view import BattleMattersFilterPopoverView as BattleMattersFilterPopoverView
from gui.impl.pub import ViewImpl as ViewImpl
from gui.selectable_reward.common import BattleMattersSelectableRewardManager as BattleMattersSelectableRewardManager
from gui.server_events.events_dispatcher import showBattleMatters as showBattleMatters, showBattleMattersMainView as showBattleMattersMainView
from gui.shared.event_dispatcher import showOfferGiftVehiclePreview as showOfferGiftVehiclePreview, showDelayedReward as showDelayedReward, showBonusDelayedConfirmationDialog as showBonusDelayedConfirmationDialog, showHangar as showHangar
from gui.impl.lobby.battle_matters.battle_matters_bonus_packer import BattleMattersVehiclesBonusUIPacker as BattleMattersVehiclesBonusUIPacker
from gui.shared.gui_items.Vehicle import VEHICLE_TYPES_ORDER as VEHICLE_TYPES_ORDER
from helpers import dependency as dependency
from nations import NONE_INDEX as NONE_INDEX
from shared_utils import first as first
from skeletons.gui.battle_matters import IBattleMattersController as IBattleMattersController
from skeletons.gui.game_control import IVehicleComparisonBasket as IVehicleComparisonBasket
from skeletons.gui.shared import IItemsCache as IItemsCache
_NATIONS_KEY_NAME = 'Nations'
_TYPES_KEY_NAME = 'Types'
_TYPES_ORDER: tuple

class BattleMattersVehicleSelectionView(ViewImpl):
    __slots__: tuple
    _battleMattersController: Any
    _comparisonBasket: Any
    _itemsCache: Any
    _selectableBonusManager = BattleMattersSelectableRewardManager
    __selectableBonus: Any
    __vehicles: Any
    __filterPopover: Any
    __filters: Any
    __savedCD: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def createPopOverContent(self, event):
        ...
    def onCompareVehicle(self, event):
        ...
    def onShowVehicle(self, event):
        ...
    def onResetFilter(self):
        ...
    def onUpdateFilter(self, filters=None):
        ...
    def _onLoading(self):
        ...
    def _finalize(self):
        ...
    def _update(self):
        ...
    def _updateVehicles(self, vm):
        ...
    def _getEvents(self):
        ...
    def handleOnStateChanged(self):
        ...
    def __getIdByCD(self, vehCD):
        ...
    def __isFilterEmpty(self, key):
        ...
    def __nationFit(self, vehCD):
        ...
    def __typeFit(self, vehCD):
        ...
    def __resetFilters(self, init=False):
        ...

def _sortByNation(vehicleTuple):
    ...
def _sortByType(vehicleTuple):
    ...
def _sortByName(vehicleTuple):
    ...
def _sortVehicles(vehicles):
    ...
def _onDialogConfirm(result, bonus, giftID):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def _showAwardView(result, bmController=None):
    ...
