# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/customization/popovers/custom_popover.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from builtins import filter as filter
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from gui.Scaleform.daapi.view.lobby.customization.popovers import orderKey as orderKey, C11nPopoverItemData as C11nPopoverItemData
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.Scaleform.daapi.view.lobby.customization.shared import ITEM_TYPE_TO_SLOT_TYPE as ITEM_TYPE_TO_SLOT_TYPE, getSlotDataFromSlot as getSlotDataFromSlot
from gui.Scaleform.daapi.view.meta.CustomizationItemsPopoverMeta import CustomizationItemsPopoverMeta as CustomizationItemsPopoverMeta
from gui.Scaleform.framework.entities.DAAPIDataProvider import SortableDAAPIDataProvider as SortableDAAPIDataProvider
from gui.customization.shared import SEASONS_ORDER as SEASONS_ORDER, isOutfitVisuallyEmpty as isOutfitVisuallyEmpty, SEASON_TYPE_TO_NAME as SEASON_TYPE_TO_NAME, C11nId as C11nId
from gui.shared.formatters import text_styles as text_styles, getItemPricesVO as getItemPricesVO
from helpers import dependency as dependency
from gui import makeHtmlString as makeHtmlString
from items.components.c11n_constants import CustomizationDisplayType as CustomizationDisplayType, SeasonType as SeasonType
from skeletons.gui.customization import ICustomizationService as ICustomizationService
POPOVER_SEASONS_ORDER: Any

class CustomPopover(CustomizationItemsPopoverMeta):
    __service: Any
    __isHistoric: Any
    __isNonHistoric: Any
    __isFantastical: Any
    __ctx: Any
    _assignedDP: Any
    def __init__(self, ctx=None):
        ...
    def onWindowClose(self):
        ...
    def remove(self, intCD, slotIds, season):
        ...
    def removeAll(self):
        ...
    def onFilterChanged(self, showHistoric, showNonHistoric, showFantastic):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __setHeader(self):
        ...
    def __update(self, *_):
        ...

class CustomPopoverDataProvider(SortableDAAPIDataProvider):
    __service: Any
    _list: Any
    __ctx: Any
    __isHistoric: Any
    __isNonHistoric: Any
    __isFantastical: Any
    def __init__(self, isHistoric, isNonHistoric, isFantastical):
        ...
    @property
    def collection(self):
        ...
    def emptyItem(self):
        ...
    def clear(self):
        ...
    def fini(self):
        ...
    def setHistoric(self, isHistoric):
        ...
    def setNonHistoric(self, isNonHistoric):
        ...
    def setFantastical(self, isFantastical):
        ...
    def buildList(self):
        ...
    def rebuildList(self):
        ...
    def __getModifiedItemsData(self, season=None):
        ...
    def __getOriginalItemsData(self, season):
        ...
    def isSkipItem(self, item):
        ...
    @staticmethod
    def __makeItemDataVO(itemData, isModified):
        ...
    @staticmethod
    def __getSeasonGroupVO(season):
        ...
    def __getNotModifiedItems(self, season):
        ...
