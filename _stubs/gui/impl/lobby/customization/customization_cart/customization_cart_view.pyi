# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/customization/customization_cart/customization_cart_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
import logging as logging
import typing as typing
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings
from adisp import adisp_process as adisp_process
from wg_async import wg_async as wg_async, wg_await as wg_await
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from frameworks.wulf import WindowFlags as WindowFlags
from gui import DialogsInterface as DialogsInterface
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.shared.view_helpers.blur_manager import CachedBlur as CachedBlur
from gui.customization.constants import CustomizationModes as CustomizationModes
from gui.impl.dialogs import dialogs as dialogs
from gui.impl.dialogs.builders import ResSimpleDialogBuilder as ResSimpleDialogBuilder
from gui.impl.gen.view_models.constants.dialog_presets import DialogPresets as DialogPresets
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.gen.view_models.views.lobby.customization.customization_cart.cart_model import CartModel as CartModel
from gui.impl.gen.view_models.views.lobby.customization.customization_cart.cart_slot_model import CartSlotModel as CartSlotModel
from gui.impl.gen.view_models.views.lobby.customization.customization_cart.cart_season_model import CartSeasonModel as CartSeasonModel
from gui.Scaleform.daapi.view.dialogs.ExchangeDialogMeta import InfoItemBase as InfoItemBase
from gui.shop import showBuyGoldForCustomization as showBuyGoldForCustomization
from gui.customization.processors.cart import SeparateItemsProcessor as SeparateItemsProcessor, StyleItemsProcessor as StyleItemsProcessor, EditableStyleItemsProcessor as EditableStyleItemsProcessor
from gui.customization.processors.cart import ProcessorSelector as ProcessorSelector, ItemsType as ItemsType
from gui.customization.shared import SEASON_TYPE_TO_NAME as SEASON_TYPE_TO_NAME, SEASONS_ORDER as SEASONS_ORDER, MoneyForPurchase as MoneyForPurchase, getTotalPurchaseInfo as getTotalPurchaseInfo
from gui.customization.shared import containsVehicleBound as containsVehicleBound, getPurchaseMoneyState as getPurchaseMoneyState, isTransactionValid as isTransactionValid
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.Scaleform.daapi.view.dialogs.ExchangeDialogMeta import ExchangeCreditsSingleItemMeta as ExchangeCreditsSingleItemMeta
from gui.Scaleform.daapi.view.dialogs.ExchangeDialogMeta import ExchangeCreditsMultiItemsMeta as ExchangeCreditsMultiItemsMeta
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE, GUI_ITEM_TYPE_NAMES as GUI_ITEM_TYPE_NAMES
from gui.shared.gui_items.customization import CustomizationTooltipContext as CustomizationTooltipContext
from shared_utils import first as first
from vehicle_outfit.outfit import Area as Area
from gui.shared.money import Currency as Currency
from gui.shared.utils.graphics import isRendererPipelineDeferred as isRendererPipelineDeferred
from items.components.c11n_constants import SeasonType as SeasonType
from helpers import dependency as dependency, uniprof as uniprof
from skeletons.gui.customization import ICustomizationService as ICustomizationService
from skeletons.gui.game_control import IWalletController as IWalletController
from skeletons.gui.impl import IGuiLoader as IGuiLoader
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from account_helpers.settings_core.settings_constants import OnceOnlyHints as OnceOnlyHints
from gui.impl.backport import createTooltipData as createTooltipData, BackportTooltipWindow as BackportTooltipWindow
from gui.impl.gen import R as R
from tutorial.hints_manager import HINT_SHOWN_STATUS as HINT_SHOWN_STATUS
from gui.impl.gen.view_models.views.lobby.customization.customization_cart.cart_seasons_model import CartSeasonsModel as CartSeasonsModel
_logger: Any
_SelectItemData: Any

class CartExchangeCreditsInfoItem(InfoItemBase):
    @property
    def itemTypeName(self):
        ...
    @property
    def userName(self):
        ...
    @property
    def itemTypeID(self):
        ...
    def getExtraIconInfo(self):
        ...
    def getGUIEmblemID(self):
        ...

class CustomizationCartView(ViewImpl):
    __slots__: tuple
    __lobbyContext: Any
    __itemsCache: Any
    __service: Any
    __settingsCore: Any
    __guiLoader: Any
    __wallet: Any
    __ctx: Any
    __purchaseItems: Any
    __mode: Any
    __items: Any
    __counters: Any
    __moneyState: Any
    __blur: Any
    __isProlongStyleRent: Any
    __c11nView: Any
    def __init__(self, layoutID, ctx=None):
        ...
    def createToolTip(self, event):
        ...
    @property
    def viewModel(self):
        ...
    # decorador original: @uniprof.regionDecorator(...)
    def _onLoading(self):
        ...
    # decorador original: @uniprof.regionDecorator(...)
    def _onLoaded(self, *args, **kwargs):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def __updateMoney(self, *_):
        ...
    def __setTotalData(self, model):
        ...
    def __addListeners(self):
        ...
    def __removeListeners(self):
        ...
    def __onWindowClose(self):
        ...
    def __onSelectItem(self, args=None):
        ...
    def __refreshPurchaseItems(self, indices, selected):
        ...
    def __refreshStrictlyDependantItems(self, targetItemData, selected):
        ...
    def __setItemsNCounters(self, itemDescriptors):
        ...
    def __setItemsData(self, model, itemDescriptors):
        ...
    # decorador original: @wg_async
    def __onBuy(self):
        ...
    # decorador original: @adisp_process
    def __showExchangeDialog(self):
        ...
    def __onTutorialClose(self):
        ...
    # decorador original: @adisp_process
    def __onBuyConfirmed(self, isOk):
        ...
    def __onSelectAutoRent(self, _=None):
        ...
    def __setBonuses(self, seasons):
        ...
    @staticmethod
    def __fillItemsListModel(listModel, items):
        ...
    def __getCamoBonusValue(self, item):
        ...
    def __onVehicleChanged(self):
        ...
    def __hasOpenedChildWindow(self):
        ...

class _BaseUIDataPacker(object):
    def __call__(self, desc):
        ...

class _ItemUIDataPacker(_BaseUIDataPacker):
    def __call__(self, desc):
        ...

class _StubUIDataPacker(_BaseUIDataPacker):
    def __call__(self, desc):
        ...

class _SeparateUIDataPacker(_ItemUIDataPacker):
    def __call__(self, desc):
        ...

class _StyleUIDataPacker(_ItemUIDataPacker):
    def __call__(self, desc):
        ...

class _EditableStyleItemUIDataPacker(_SeparateUIDataPacker):
    def __call__(self, desc):
        ...

def _getSeasonModel(seasonType, seasons):
    ...
def _getProcessorsMap():
    ...
