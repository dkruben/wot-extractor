# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/storage/customization/customization_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import math as math
import typing as typing
from future.utils import viewitems as viewitems, viewvalues as viewvalues
import nations as nations
from adisp import adisp_process as adisp_process
from gui import DialogsInterface as DialogsInterface
from gui.Scaleform.daapi.view.dialogs.confirm_customization_item_dialog_meta import ConfirmC11nSellMeta as ConfirmC11nSellMeta
from gui.Scaleform.daapi.view.lobby.event_boards.event_helpers import LEVELS_RANGE as LEVELS_RANGE
from gui.Scaleform.genConsts.CONTEXT_MENU_HANDLER_TYPE import CONTEXT_MENU_HANDLER_TYPE as CONTEXT_MENU_HANDLER_TYPE
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS as TOOLTIPS
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared import event_dispatcher as event_dispatcher
from helpers import dependency as dependency
from helpers.i18n import makeString as _ms
from gui.Scaleform.daapi.view.lobby.storage.storage_helpers import createStorageDefVO as createStorageDefVO, customizationPreview as customizationPreview, getAvailableForSellCustomizationCount as getAvailableForSellCustomizationCount
from gui.Scaleform.daapi.view.lobby.storage.storage_helpers import isCustomizationAvailableForSell as isCustomizationAvailableForSell
from gui.Scaleform.daapi.view.lobby.customization.shared import getSuitableText as getSuitableText, isC11nEnabled as isC11nEnabled
from gui.Scaleform.daapi.view.meta.StorageCategoryCustomizationViewMeta import StorageCategoryCustomizationViewMeta as StorageCategoryCustomizationViewMeta
from gui.shared.formatters import getItemPricesVO as getItemPricesVO
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.utils.requesters.ItemsRequester import REQ_CRITERIA as REQ_CRITERIA
from gui.shared.utils.functions import makeTooltip as makeTooltip
from skeletons.gui.customization import ICustomizationService as ICustomizationService
from shared_utils import CONST_CONTAINER as CONST_CONTAINER
from typing import Optional as Optional
from gui.shared.gui_items.customization.c11n_items import Customization as Customization
_TYPE_BIT_TO_CUSTOMIZATION_TYPE_MAP: dict
_CUSTOMIZATION_ITEM_TYPES: tuple
_TYPE_FILTER_ITEMS: list
_TABS_SORT_ORDER: dict

class _CustomizationFilterBit(CONST_CONTAINER):
    STYLE = 1
    PAINT = 2
    CAMOUFLAGE = 4
    PROJECTION_DECAL = 8
    EMBLEM = 16
    PERSONAL_NUMBER = 32
    MODIFICATION = 64
    ATTACHMENT = 128
    STAT_TRACKER = 256

class _VehiclesFilter(object):
    __slots__: tuple
    vehicles: Any
    def __init__(self, invVehicles):
        ...
    def getVehicles(self, item):
        ...

class StorageCategoryCustomizationView(StorageCategoryCustomizationViewMeta):
    _service: Any
    filterItems = _TYPE_FILTER_ITEMS
    _currentCount: Any
    _totalCount: Any
    # decorador original: @dependency.replace_none_kwargs(...)
    def navigateToCustomization(self, c11nService=None):
        ...
    # decorador original: @adisp_process
    def sellCustomizationItem(self, itemCD, vehicleCD=None):
        ...
    def __sellItem(self, itemCD, count, vehicle):
        ...
    def previewItem(self, itemCD, vehicleCD):
        ...
    def scrolledToBottom(self):
        ...
    def _getClientSectionKey(self):
        ...
    def _getFilteredCriteria(self):
        ...
    def _getItemTypeID(self):
        ...
    def _getRequestCriteria(self, invVehicles):
        ...
    def _getInvVehicleCriteria(self):
        ...
    def _getVoList(self):
        ...
    def _calcItemsCount(self, itemList):
        ...
    def _getVoListForItem(self, item):
        ...
    def _getVO(self, item, vehicleCD=None):
        ...
    def _getItemSortKey(self, item):
        ...
    def _getSuitableText(self, item, vehicleCD):
        ...

def _getCustomizationCriteria(invVehicles):
    ...
