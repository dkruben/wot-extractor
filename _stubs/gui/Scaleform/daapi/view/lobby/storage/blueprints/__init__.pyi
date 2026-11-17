# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/storage/blueprints/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import iteritems as iteritems
import nations as nations
from account_helpers.AccountSettings import STORAGE_BLUEPRINTS_CAROUSEL_FILTER as STORAGE_BLUEPRINTS_CAROUSEL_FILTER
from gui import GUI_NATIONS_ORDER_INDEX as GUI_NATIONS_ORDER_INDEX
from gui.filters.carousel_filter import BasicCriteriesGroup as BasicCriteriesGroup, CriteriesGroup as CriteriesGroup, EventCriteriesGroup as EventCriteriesGroup
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.daapi.view.lobby.storage.inhangar import StorageCarouselDataProvider as StorageCarouselDataProvider, StorageCarouselFilter as StorageCarouselFilter
from gui.Scaleform.daapi.view.lobby.storage.storage_helpers import getVehicleName as getVehicleName
from gui.Scaleform.daapi.view.lobby.techtree.techtree_dp import g_techTreeDP as g_techTreeDP
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams as SFViewLoadParams
from gui.Scaleform.genConsts.CONTEXT_MENU_HANDLER_TYPE import CONTEXT_MENU_HANDLER_TYPE as CONTEXT_MENU_HANDLER_TYPE
from gui.Scaleform.genConsts.STORAGE_CONSTANTS import STORAGE_CONSTANTS as STORAGE_CONSTANTS
from gui.Scaleform.genConsts.STORE_CONSTANTS import STORE_CONSTANTS as STORE_CONSTANTS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.Scaleform.locale.STORAGE import STORAGE as STORAGE
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared import events as events
from gui.shared.formatters import text_styles as text_styles, icons as icons
from gui.shared.gui_items.Vehicle import getShopVehicleIconPath as getShopVehicleIconPath
from gui.shared.utils.requesters.ItemsRequester import RequestCriteria as RequestCriteria, PredicateCondition as PredicateCondition, REQ_CRITERIA as REQ_CRITERIA
from helpers import dependency as dependency
from helpers.i18n import makeString as makeString
from skeletons.gui.impl import IGuiLoader as IGuiLoader
from skeletons.gui.shared import IItemsCache as IItemsCache

class _BlueprintsCriteriesGroup(CriteriesGroup):
    __itemsCache: Any
    _criteria: Any
    def update(self, filters):
        ...
    @staticmethod
    def isApplicableFor(vehicle):
        ...
    @classmethod
    def getGroupCriteria(cls):
        ...
    @classmethod
    def __hasProgress(cls, vehicle):
        ...

class ExtendedCriteriesGroup(BasicCriteriesGroup):
    __itemsCache: Any
    _criteria: Any
    def update(self, filters):
        ...
    @classmethod
    def __availableToUnlock(cls, vehicle):
        ...
    @classmethod
    def __canConvert(cls, vehicle):
        ...

class BlueprintsStorageCarouselFilter(StorageCarouselFilter):
    _clientSections: Any
    _criteriesGroups: Any
    def __init__(self, criteries=None):
        ...

class BlueprintsStorageCarouselDataProvider(StorageCarouselDataProvider):
    __itemsCache: Any
    __gui: Any
    _baseCriteria: Any
    __filterCallback: Any
    _vehicleItems: Any
    def __init__(self, carouselFilter, itemsCache, filterCallback):
        ...
    def applyFilter(self, forceApply=False):
        ...
    def _filterByIndices(self):
        ...
    def _buildVehicle(self, vehicle):
        ...
    @classmethod
    def _vehicleComparisonKey(cls, vehicle):
        ...
    def __formatFragmentProgress(self, current, total, discount):
        ...
    def __formatFragment(self, count, icon, iconWidth=23):
        ...
    def __formatFragmentsCost(self, intelligenceCost, intelligenceIcon, nationalsCost):
        ...

def blueprintExitEvent():
    ...
