# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/customization/popovers/editable_style_popover.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from gui import makeHtmlString as makeHtmlString
from gui.Scaleform.daapi.view.lobby.customization.popovers import C11nPopoverItemData as C11nPopoverItemData, orderKey as orderKey
from gui.Scaleform.daapi.view.lobby.customization.shared import ITEM_TYPE_TO_SLOT_TYPE as ITEM_TYPE_TO_SLOT_TYPE, fitOutfit as fitOutfit, getCurrentVehicleAvailableRegionsMap as getCurrentVehicleAvailableRegionsMap, isStyleEditedForCurrentVehicle as isStyleEditedForCurrentVehicle
from gui.Scaleform.daapi.view.meta.CustomizationEditedKitPopoverMeta import CustomizationEditedKitPopoverMeta as CustomizationEditedKitPopoverMeta
from gui.customization.constants import CustomizationModes as CustomizationModes
from gui.customization.shared import SEASONS_ORDER as SEASONS_ORDER, SEASON_TYPE_TO_NAME as SEASON_TYPE_TO_NAME, C11nId as C11nId, EDITABLE_STYLE_IRREMOVABLE_TYPES as EDITABLE_STYLE_IRREMOVABLE_TYPES, C11N_ITEM_TYPE_MAP as C11N_ITEM_TYPE_MAP
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.formatters import text_styles as text_styles, getItemPricesVO as getItemPricesVO
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from helpers import dependency as dependency
from items.components.c11n_components import getItemSlotType as getItemSlotType
from items.components.c11n_constants import SeasonType as SeasonType, CustomizationType as CustomizationType
from skeletons.gui.customization import ICustomizationService as ICustomizationService
POPOVER_SEASONS_ORDER: Any

class EditableStylePopover(CustomizationEditedKitPopoverMeta):
    __service: Any
    __ctx: Any
    __style: Any
    def __init__(self, ctx=None):
        ...
    def onWindowClose(self):
        ...
    def remove(self, intCD, slotIds, season):
        ...
    def setToDefault(self):
        ...
    def removeAll(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __setHeader(self):
        ...
    def __setClearMessage(self):
        ...
    def __update(self, *_):
        ...
    def __updateClearStyleButton(self):
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
    def __getBaseOutfit(self, season, vehicleCD=''):
        ...
