# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/customization/popovers/style_popover.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from gui import makeHtmlString as makeHtmlString
from gui.Scaleform.daapi.view.lobby.customization.shared import TYPES_ORDER as TYPES_ORDER
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.Scaleform.daapi.view.meta.CustomizationKitPopoverMeta import CustomizationKitPopoverMeta as CustomizationKitPopoverMeta
from gui.Scaleform.framework.entities.DAAPIDataProvider import SortableDAAPIDataProvider as SortableDAAPIDataProvider
from gui.customization.shared import SEASON_TYPE_TO_NAME as SEASON_TYPE_TO_NAME, SEASONS_ORDER as SEASONS_ORDER, SeasonType as SeasonType
from gui.shared.formatters import text_styles as text_styles
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from helpers import dependency as dependency
from skeletons.gui.customization import ICustomizationService as ICustomizationService
POPOVER_SEASONS_ORDER: Any

class StylePopover(CustomizationKitPopoverMeta):
    __service: Any
    __ctx: Any
    __style: Any
    _assignedDP: Any
    def __init__(self, ctx=None):
        ...
    def onWindowClose(self):
        ...
    def removeCustomizationKit(self):
        ...
    def updateAutoProlongation(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __setHeader(self):
        ...
    def __setRent(self):
        ...
    def __setClearMessage(self):
        ...
    def __update(self, *_):
        ...

class StylePopoverDataProvider(SortableDAAPIDataProvider):
    __service: Any
    _list: Any
    __ctx: Any
    def __init__(self):
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
    def buildList(self):
        ...
    def rebuildList(self):
        ...
    def __getSeasonItemsData(self, style, season, vehicleDescriptor):
        ...
    @staticmethod
    def __makeItemDataVO(item):
        ...
    @staticmethod
    def __orderKey(item):
        ...
    def __getModifiedOutfit(self, season, style, vehicleCD=''):
        ...
