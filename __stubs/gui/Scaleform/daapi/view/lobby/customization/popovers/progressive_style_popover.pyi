# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/customization/popovers/progressive_style_popover.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from gui import makeHtmlString as makeHtmlString
from gui.Scaleform.daapi.view.lobby.customization.customization_carousel import DisjunctionCarouselFilter as DisjunctionCarouselFilter, FilterAliases as FilterAliases
from gui.Scaleform.daapi.view.lobby.customization.popovers import C11nPopoverItemData as C11nPopoverItemData, orderKey as orderKey
from gui.Scaleform.daapi.view.lobby.customization.shared import getCurrentVehicleAvailableRegionsMap as getCurrentVehicleAvailableRegionsMap, fitOutfit as fitOutfit, ITEM_TYPE_TO_SLOT_TYPE as ITEM_TYPE_TO_SLOT_TYPE, removePartsFromOutfit as removePartsFromOutfit
from gui.Scaleform.daapi.view.meta.CustomizationProgressiveKitPopoverMeta import CustomizationProgressiveKitPopoverMeta as CustomizationProgressiveKitPopoverMeta
from gui.customization.shared import SEASONS_ORDER as SEASONS_ORDER, SEASON_TYPE_TO_NAME as SEASON_TYPE_TO_NAME, EDITABLE_STYLE_IRREMOVABLE_TYPES as EDITABLE_STYLE_IRREMOVABLE_TYPES, C11nId as C11nId
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.formatters import text_styles as text_styles, getItemPricesVO as getItemPricesVO
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from helpers import dependency as dependency
from items.components.c11n_components import getItemSlotType as getItemSlotType
from items.components.c11n_constants import SeasonType as SeasonType
from skeletons.gui.customization import ICustomizationService as ICustomizationService
POPOVER_SEASONS_ORDER: Any

class FilterTypes(object):
    HISTORIC = 1
    NON_HISTORIC = 2
    FANTASTICAL = 3
    LOCKED = 4

class ProgressiveStylePopover(CustomizationProgressiveKitPopoverMeta):
    __service: Any
    __ctx: Any
    __style: Any
    __filters: Any
    __itemsList: Any
    def __init__(self, ctx=None):
        ...
    def onWindowClose(self):
        ...
    def remove(self, intCD, slotIds, season):
        ...
    def removeAll(self):
        ...
    def setToDefault(self):
        ...
    def onFilterChanged(self, showHistoric, showNonHistoric, showFantastic, showProgressiveLocked):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __update(self, *_):
        ...
    def __setHeader(self):
        ...
    def __setClearMessage(self):
        ...
    def __buildList(self):
        ...
    def __getSeasonItemsData(self, season, purchaseItems, availableRegionsMap, vehicleDescriptor):
        ...
    def __makeItemDataVO(self, itemData):
        ...
    @staticmethod
    def __getSeasonGroupVO(season):
        ...
    def __initFilters(self):
        ...
    def __getFilterReq(self):
        ...
    def __hasIsRemovable(self):
        ...
    def __getBaseOutfit(self, season, vehicleCD=''):
        ...
