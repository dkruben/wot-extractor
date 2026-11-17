# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/customization/customization_cm_handlers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from adisp import adisp_process as adisp_process
from Event import Event as Event
from gui import DialogsInterface as DialogsInterface
from gui.Scaleform.daapi.view.dialogs.confirm_customization_item_dialog_meta import ConfirmC11nBuyMeta as ConfirmC11nBuyMeta, ConfirmC11nSellMeta as ConfirmC11nSellMeta
from gui.Scaleform.daapi.view.lobby.customization.shared import isItemUsedUp as isItemUsedUp
from gui.Scaleform.framework.managers.context_menu import AbstractContextMenuHandler as AbstractContextMenuHandler
from gui.Scaleform.locale.MENU import MENU as MENU
from gui.customization.constants import CustomizationModes as CustomizationModes, CustomizationModeSource as CustomizationModeSource
from gui.customization.shared import SEASON_TYPE_TO_NAME as SEASON_TYPE_TO_NAME, EDITABLE_STYLE_IRREMOVABLE_TYPES as EDITABLE_STYLE_IRREMOVABLE_TYPES
from gui.shared.formatters import getItemPricesVO as getItemPricesVO
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.gui_items.gui_item_economics import ITEM_PRICE_EMPTY as ITEM_PRICE_EMPTY
from gui.shared.tooltips import ACTION_TOOLTIPS_TYPE as ACTION_TOOLTIPS_TYPE
from gui.shared.tooltips.formatters import packActionTooltipData as packActionTooltipData
from helpers import dependency as dependency
from items.components.c11n_constants import SeasonType as SeasonType
from shared_utils import first as first
from skeletons.gui.customization import ICustomizationService as ICustomizationService
from skeletons.gui.shared import IItemsCache as IItemsCache
from CurrentVehicle import g_currentVehicle as g_currentVehicle
_logger: Any

class CustomizationOptions(object):
    BUY = 'buy'
    BUY_MORE = 'buyMore'
    SELL = 'sell'
    REMOVE_FROM_TANK = 'removeFromTank'
    PROLONGATION_ON = 'autoprolongationOn'
    PROLONGATION_OFF = 'autoprolongationOff'
    STYLE_INFO = 'styleInfo'
    EDIT_STYLE = 'editStyle'
    BASE_STYLE = 'baseStyle'

class CustomizationItemCMHandler(AbstractContextMenuHandler):
    itemsCache: Any
    service: Any
    _intCD: Any
    onSelected: Any
    _item: Any
    __ctx: Any
    def __init__(self, cmProxy, ctx=None):
        ...
    def changeAutoRent(self):
        ...
    def fini(self):
        ...
    # decorador original: @adisp_process
    def buyItem(self):
        ...
    # decorador original: @adisp_process
    def sellItem(self):
        ...
    def removeItemFromTank(self):
        ...
    def showStyleInfo(self):
        ...
    def enterEditMode(self):
        ...
    def clearStyle(self):
        ...
    def _generateOptions(self, ctx=None):
        ...
    def _initFlashValues(self, ctx):
        ...
    def __separateItem(self, item):
        ...
    def __getStyleInfoBtn(self, item):
        ...
    def __getEditStyleBtn(self, item):
        ...
    def __getClearStyleBtn(self, item):
        ...
    def __getBuyBtn(self, item):
        ...
    def __getRentBtn(self, item):
        ...
    def __getSellBtn(self, item):
        ...
    def __getRemoveBtn(self, item):
        ...
