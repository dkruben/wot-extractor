# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/lootbox_system/base/views_loaders.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from typing import TYPE_CHECKING as TYPE_CHECKING
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.daapi.view.lobby.customization.context.styled_mode import StyledMode as StyledMode
from gui.customization.constants import CustomizationModes as CustomizationModes
from gui.impl.gen import R as R
from gui.lootbox_system.base.common import ViewID as ViewID, Views as Views
from gui.lootbox_system.base.utils import getIntroVideoUrl as getIntroVideoUrl, getIsShowIntro as getIsShowIntro, getShopOverlayUrl as getShopOverlayUrl, getVehicleForStyle as getVehicleForStyle
from gui.Scaleform.daapi.view.common.battle_royale.br_helpers import currentHangarIsBattleRoyale as currentHangarIsBattleRoyale
from gui.shared.event_dispatcher import hideVehiclePreview as hideVehiclePreview, selectVehicleInHangar as selectVehicleInHangar, showBrowserOverlayView as showBrowserOverlayView, showStylePreview as showStylePreview, showShop as showShop, showVehiclePreviewWithoutBottomPanel as showVehiclePreviewWithoutBottomPanel
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from helpers import dependency as dependency
from shared_utils import first as first
from skeletons.gui.customization import ICustomizationService as ICustomizationService
from skeletons.gui.impl import IGuiLoader as IGuiLoader
from skeletons.gui.shared import IItemsCache as IItemsCache
from soft_exception import SoftException as SoftException
from gui.shared.gui_items.customization.c11n_items import Style as Style
_logger: Any

def showIntro(eventName):
    ...
def showMain(eventName, subViewID=None, category='', count=0, bonuses=None, *args, **kwargs):
    ...
def showInfo(eventName, category=''):
    ...
def showAutoOpen(eventName, rewards, boxes):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def showItemPreview(itemType, itemID, styleID, customization=None, itemsCache=None):
    ...
def hideItemPreview():
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def showCustomizationHangar(style, itemsCache=None, customization=None):
    ...
def showVehicleStylePreview(style):
    ...
def openShop(eventName, parent=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def findActiveWindow(viewID, uiLoader=None):
    ...
def registerViewsLoaders():
    ...
def unregisterViewsLoaders():
    ...
