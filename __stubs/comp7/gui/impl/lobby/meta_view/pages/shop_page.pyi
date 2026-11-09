# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/meta_view/pages/shop_page.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from future.utils import viewitems as viewitems
from functools import partial as partial
from gui.Scaleform.lobby_entry import getLobbyStateMachine as getLobbyStateMachine
from shared_utils import first as first, findFirst as findFirst
from CurrentVehicle import g_currentPreviewVehicle as g_currentPreviewVehicle, g_currentVehicle as g_currentVehicle
from comp7.gui.game_control.comp7_shop_controller import ShopControllerStatus as ShopControllerStatus
from comp7.gui.impl.gen.view_models.views.lobby.base_product_model import ProductTypes as ProductTypes, ProductState as ProductState
from comp7.gui.impl.gen.view_models.views.lobby.enums import MetaRootViews as MetaRootViews, Rank as Rank
from comp7.gui.impl.gen.view_models.views.lobby.meta_view.pages.rank_discount_model import RankDiscountModel as RankDiscountModel
from comp7.gui.impl.gen.view_models.views.lobby.meta_view.pages.shop_model import ShopModel as ShopModel, ShopState as ShopState
from comp7.gui.impl.lobby.comp7_helpers import comp7_model_helpers as comp7_model_helpers, comp7_shared as comp7_shared
from comp7.gui.impl.lobby.meta_view.meta_view_helper import setDivisionData as setDivisionData, setRankData as setRankData, getRankDivisions as getRankDivisions
from comp7.gui.impl.lobby.meta_view.pages import PageSubModelPresenter as PageSubModelPresenter
from comp7.gui.impl.lobby.meta_view.products_helper import packProduct as packProduct, getItemType as getItemType, getVehicleCDAndStyle as getVehicleCDAndStyle, addSeenProduct as addSeenProduct
from comp7.gui.impl.lobby.meta_view.rotatable_view_helper import RotatableViewHelper as RotatableViewHelper, Comp7Cameras as Comp7Cameras
from comp7.gui.impl.lobby.tooltips.fifth_rank_tooltip import FifthRankTooltip as FifthRankTooltip
from comp7.gui.impl.lobby.tooltips.general_rank_tooltip import GeneralRankTooltip as GeneralRankTooltip
from comp7.gui.impl.lobby.tooltips.sixth_rank_tooltip import SixthRankTooltip as SixthRankTooltip
from comp7.gui.shared import event_dispatcher as comp7_events
from comp7.skeletons.gui.game_control import IComp7ShopController as IComp7ShopController
from frameworks.wulf.view.array import fillViewModelsArray as fillViewModelsArray
from gui.Scaleform.Waiting import Waiting as Waiting
from gui.Scaleform.daapi.view.lobby.customization.shared import CustomizationTabs as CustomizationTabs
from gui.Scaleform.daapi.view.lobby.vehicle_compare.formatters import resolveStateTooltip as resolveStateTooltip
from gui.Scaleform.daapi.view.lobby.vehicle_preview.configurable_vehicle_preview import OptionalBlocks as OptionalBlocks
from gui.Scaleform.genConsts.STORAGE_CONSTANTS import STORAGE_CONSTANTS as STORAGE_CONSTANTS
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.Scaleform.locale.VEH_COMPARE import VEH_COMPARE as VEH_COMPARE
from gui.customization.constants import CustomizationModes as CustomizationModes
from gui.hangar_cameras.hangar_camera_common import CameraRelatedEvents as CameraRelatedEvents
from gui.impl.backport import BackportTooltipWindow as BackportTooltipWindow
from gui.impl.backport.backport_tooltip import TooltipData as TooltipData
from gui.impl.gen import R as R
from gui.impl.gui_decorators import args2params as args2params
from gui.impl.lobby.tooltips.vehicle_role_descr_view import VehicleRolesTooltipView as VehicleRolesTooltipView
from gui.shared import g_eventBus as g_eventBus
from gui.shared.event_dispatcher import showStorage as showStorage
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.items_cache import CACHE_SYNC_REASON as CACHE_SYNC_REASON
from gui.shared.view_helpers.blur_manager import CachedBlur as CachedBlur
from helpers import dependency as dependency
from items import customizations as customizations
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from skeletons.gui.customization import ICustomizationService as ICustomizationService
from skeletons.gui.game_control import IComp7Controller as IComp7Controller, IVehicleComparisonBasket as IVehicleComparisonBasket
from skeletons.gui.shared import IItemsCache as IItemsCache
from skeletons.gui.shared.gui_items import IGuiItemsFactory as IGuiItemsFactory
from skeletons.gui.shared.utils import IHangarSpace as IHangarSpace
from typing import Dict as Dict
from comp7.helpers.comp7_server_settings import Comp7RanksConfig as Comp7RanksConfig
from comp7.gui.game_control.comp7_shop_controller import ShopPageProductInfo as ShopPageProductInfo
from gui.platform.products_fetcher.fetch_result import ResponseStatus as ResponseStatus
from gui.Scaleform.framework.application import AppEntry as AppEntry
_logger: Any
_PRODUCT_TYPE_ORDER: list
_SHOP_BACKGROUND_ALPHA = 0.0

class ShopPage(PageSubModelPresenter):
    __slots__: tuple
    __appLoader: Any
    __comp7Controller: Any
    __comp7ShopController: Any
    __hangarSpace: Any
    __c11nService: Any
    __itemsCache: Any
    __comparisonBasket: Any
    __guiItemsFactory: Any
    __DEFAULT_PRODUCT_SELECTOR_NAME = 'default'
    __BLUR_INTENSITY = 0.5
    __currentItemCD: Any
    __blur: Any
    __rotationHelper: Any
    __switchCameraToDefault: Any
    __switchVehicleToDefault: Any
    __productSelectorMethods: Any
    __productSetterMethods: Any
    __productCdToCode: Any
    __requestStatus: Any
    __products: Any
    __hangarVehId: Any
    __productItems: Any
    def __init__(self, viewModel, parentView):
        ...
    @property
    def pageId(self):
        ...
    @property
    def viewModel(self):
        ...
    @property
    def ranksConfig(self):
        ...
    @property
    def currentItemCD(self):
        ...
    def createToolTip(self, event):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def initialize(self, **params):
        ...
    def finalize(self):
        ...
    def __isRefferalStateLoaded(self):
        ...
    def _getEvents(self):
        ...
    def __disableBackgroundAlpha(self):
        ...
    def __updateData(self, *_, **__):
        ...
    def __processData(self):
        ...
    def __onSyncCompleted(self, reason, *_):
        ...
    def __onShopStateChanged(self):
        ...
    def __switchToErrorState(self):
        ...
    def __switchToSuccessState(self):
        ...
    def __showWaiting(self):
        ...
    def __hideWaiting(self):
        ...
    def __onDataUpdated(self, status):
        ...
    def __updateProductsData(self, shopModel):
        ...
    def __selectInitialItem(self):
        ...
    def __updateProductDiscounts(self):
        ...
    def __sortingKey(self, product):
        ...
    def __goToPreview(self):
        ...
    def __goToVehicle(self):
        ...
    def __goToStyle(self):
        ...
    def __openPurchaseView(self):
        ...
    def __openRestoreView(self):
        ...
    # decorador original: @args2params(...)
    def __onProductSelect(self, cd):
        ...
    # decorador original: @args2params(...)
    def __onProductSeen(self, cd):
        ...
    def __onAddToVehicleCompare(self):
        ...
    def __switchComparisonBasketState(self, _):
        ...
    def __getStartProductCD(self, products):
        ...
    def __getFirstNotPurchasedProduct(self, products):
        ...
    def __selectProduct(self):
        ...
    def __selectVehicle(self):
        ...
    def __onHeroStateChanged(self):
        ...
    def __checkComparisonBasketState(self, model):
        ...
    def __selectStyle(self):
        ...
    def __selectEquipment(self):
        ...

# decorador original: @dependency.replace_none_kwargs(...)
def _onCustomizationLoadedCallback(styleCD, service=None, hangarSpace=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def __onVehicleLoadFinished(ctxEvent, service=None, hangarSpace=None):
    ...
