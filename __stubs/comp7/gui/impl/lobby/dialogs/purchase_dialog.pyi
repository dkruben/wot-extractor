# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/dialogs/purchase_dialog.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import BigWorld as BigWorld
from gui.Scaleform.lobby_entry import getLobbyStateMachine as getLobbyStateMachine
from shared_utils import findFirst as findFirst
from shared_utils import first as first
from Comp7Lighting import Comp7Lighting as Comp7Lighting, Comp7LightingTriggers as Comp7LightingTriggers
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.impl.backport import BackportTooltipWindow as BackportTooltipWindow
from gui.impl.backport.backport_tooltip import createTooltipData as createTooltipData
from gui.impl.lobby.tooltips.vehicle_role_descr_view import VehicleRolesTooltipView as VehicleRolesTooltipView
from comp7.gui.impl.gen.view_models.views.lobby.base_product_model import ProductTypes as ProductTypes
from comp7.gui.impl.gen.view_models.views.lobby.dialogs.purchase_dialog_model import PurchaseDialogModel as PurchaseDialogModel, PageState as PageState
from comp7.gui.impl.gen.view_models.views.lobby.style3d_product_model import Style3dProductModel as Style3dProductModel
from comp7.gui.impl.lobby.comp7_helpers.comp7_lobby_sounds import FlybySounds as FlybySounds, playSound as playSound
from comp7.gui.impl.lobby.meta_view.products_helper import packProduct as packProduct, setProductModelData as setProductModelData
from comp7.gui.impl.lobby.meta_view.rotatable_view_helper import RotatableViewHelper as RotatableViewHelper, Comp7Cameras as Comp7Cameras
from comp7.skeletons.gui.game_control import IComp7ShopController as IComp7ShopController
from frameworks.wulf import WindowFlags as WindowFlags, WindowLayer as WindowLayer
from frameworks.wulf.view.array import fillViewModelsArray as fillViewModelsArray
from gui.impl.gen import R as R
from gui.impl.pub.lobby_window import LobbyNotificationWindow as LobbyNotificationWindow
from gui.shared.items_cache import CACHE_SYNC_REASON as CACHE_SYNC_REASON
from gui.shared.view_helpers.blur_manager import CachedBlur as CachedBlur
from helpers import dependency as dependency
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from skeletons.gui.game_control import IOverlayController as IOverlayController
from skeletons.gui.shared import IItemsCache as IItemsCache
from skeletons.gui.shared.utils import IHangarSpace as IHangarSpace
from wg_async import wg_async as wg_async
from gui.impl.lobby.page.wallet_presenter import WalletPresenter as WalletPresenter, CrystalProvider as CrystalProvider, GoldProvider as GoldProvider, CreditsProvider as CreditsProvider, FreeXpProvider as FreeXpProvider
from gui.impl.pub.view_component import ViewComponent as ViewComponent
_logger: Any

class PurchaseDialog(ViewComponent):
    __overlayCtrl: Any
    __itemsCache: Any
    __comp7ShopController: Any
    __hangarSpace: Any
    __appLoader: Any
    __BLUR_INTENSITY = 0.5
    __productCode: Any
    __rotationHelper: Any
    __prevCameraName: Any
    __blur: Any
    def __init__(self, productCode):
        ...
    @property
    def viewModel(self):
        ...
    def createToolTip(self, event):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _getChildComponents(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _getEvents(self):
        ...
    def __onClose(self):
        ...
    # decorador original: @wg_async
    def __onConfirm(self):
        ...
    def __onItemsCacheSync(self, reason, *_):
        ...
    def __setProducts(self, viewModel):
        ...
    def __updateData(self, *_):
        ...
    def __onCameraSwitched(self, cameraName):
        ...
    def __isCameraFlybyNeeded(self):
        ...
    def __setSuccessPurchaseState(self):
        ...
    def __startCameraFlyby(self):
        ...
    def __onFlybyFinished(self):
        ...
    def __setLightingTrigger(self, trigger):
        ...
    def __onShopStateChanged(self):
        ...

class PurchaseDialogWindow(LobbyNotificationWindow):
    __slots__: tuple
    def __init__(self, productCode, parent=None):
        ...
