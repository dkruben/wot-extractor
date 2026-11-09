# wot-extractor: STUB (.pyi) gerado a partir de sources/res/resource_well/scripts/client/resource_well/gui/shared/event_dispatcher.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from typing import List as List, Tuple as Tuple, Optional as Optional, TYPE_CHECKING as TYPE_CHECKING
from BWUtil import AsyncReturn as AsyncReturn
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.impl.gen import R as R
from gui.impl.pub.notification_commands import WindowNotificationCommand as WindowNotificationCommand
from gui.shared.event_dispatcher import showBrowserOverlayView as showBrowserOverlayView
from helpers import dependency as dependency
from resource_well.gui.feature.constants import PurchaseMode as PurchaseMode
from resource_well.gui.feature.resource_well_helpers import getRewardVehiclesInInventory as getRewardVehiclesInInventory
from skeletons.gui.impl import IGuiLoader as IGuiLoader, INotificationWindowController as INotificationWindowController
from skeletons.gui.resource_well import IResourceWellController as IResourceWellController
from wg_async import wg_await as wg_await, wg_async as wg_async
from frameworks.wulf import Window as Window
_logger: Any

# decorador original: @dependency.replace_none_kwargs(...)
def openInfoPageScreen(resourceWell=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def showMainWindow(resourceWell=None):
    ...
def showResourcesLoadingWindow(rewardID, stopRequesterInDestroy=True):
    ...
# decorador original: @wg_async
def showResourcesLoadingConfirm(rewardID, resources, isReturnOperation):
    ...
# decorador original: @wg_async
def showNextSerialVehiclesConfirm(rewardID):
    ...
def showResourceWellNoVehiclesConfirm(parent=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def showResourceWellAwardWindow(rewardID, serialNumber='', notificationMgr=None):
    ...
def showResourceWellVehiclePreview(vehicleCD, rewardID, style=None, previewStyle=None, topPanelData=None):
    ...
