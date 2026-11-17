# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/customization/customization_carousel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from collections import defaultdict as defaultdict, namedtuple as namedtuple, OrderedDict as OrderedDict
from functools import reduce as reduce
from itertools import chain as chain
import typing as typing
from future.utils import iteritems as iteritems, lfilter as lfilter, viewitems as viewitems, viewvalues as viewvalues
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from cache import cached_property as cached_property
from gui.Scaleform.daapi.view.lobby.customization.shared import CustomizationTabs as CustomizationTabs, TYPES_ORDER as TYPES_ORDER, isStatTrackerTabEnabled as isStatTrackerTabEnabled, isItemLimitReached as isItemLimitReached, isItemUsedUp as isItemUsedUp, vehicleHasSlot as vehicleHasSlot
from gui.Scaleform.framework.entities.DAAPIDataProvider import SortableDAAPIDataProvider as SortableDAAPIDataProvider
from gui.customization.constants import CustomizationModes as CustomizationModes
from gui.customization.shared import getBaseStyleItems as getBaseStyleItems, C11N_ITEM_TYPE_MAP as C11N_ITEM_TYPE_MAP, getInheritors as getInheritors, getAncestors as getAncestors, getGroupHelper as getGroupHelper
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA, RequestCriteria as RequestCriteria
from helpers import dependency as dependency
from items.components.c11n_constants import SeasonType as SeasonType, ProjectionDecalFormTags as ProjectionDecalFormTags, ItemTags as ItemTags, EMPTY_ITEM_ID as EMPTY_ITEM_ID, Rarity as Rarity
from items import vehicles as vehicles
from skeletons.gui.customization import ICustomizationService as ICustomizationService
from skeletons.gui.server_events import IEventsCache as IEventsCache
from skeletons.gui.shared import IItemsCache as IItemsCache
from uilogging.customization_3d_objects.logger import CustomizationFilterLogger as CustomizationFilterLogger
from uilogging.customization_3d_objects.logging_constants import CustomizationViewKeys as CustomizationViewKeys
from gui.shared.gui_items.customization.c11n_items import Customization as Customization
_logger: Any
CustomizationBookmarkVO: Any
CustomizationArrowVO: Any
SelectedItem: Any

class ItemsData(object):
    items: Any
    groups: Any
    def __init__(self, items=None, groups=None):
        ...
    # decorador original: @cached_property
    def hasUsedUpItems(self):
        ...
    # decorador original: @cached_property
    def hasProgressiveItems(self):
        ...
    # decorador original: @cached_property
    def hasQuestProgressItems(self):
        ...

class CarouselData(object):
    __slots__: tuple
    items: Any
    sizes: Any
    bookmarks: Any
    arrows: Any
    showSeparators: Any
    def __init__(self):
        ...

class CarouselCache(object):
    __itemsCache: Any
    __service: Any
    __eventsCache: Any
    __itemsData: Any
    __carouselData: Any
    __createFilterCriteria: Any
    __createSortCriteria: Any
    __cachedEditableStyleId: Any
    __ctx: Any
    def __init__(self, createFilterCriteria, createSortCriteria):
        ...
    def fini(self):
        ...
    def getVisibleTabs(self):
        ...
    def getEnabledTabs(self):
        ...
    def getItemsData(self, season=None, modeId=None, tabId=None):
        ...
    def getCarouselData(self, season=None, modeId=None, tabId=None):
        ...
    def invalidateItemsData(self):
        ...
    def invalidateCarouselData(self):
        ...
    def __initCache(self):
        ...
    def __getCarouselData(self, season=None, modeId=None, tabId=None):
        ...
    def __initItemsData(self):
        ...
    def __initEditableStyleItemsData(self):
        ...
    def __invalidateEditableStyleCache(self):
        ...

class CustomizationCarouselDataProvider(SortableDAAPIDataProvider):
    __service: Any
    __ctx: Any
    __selectedItem: Any
    __selectedGroup: Any
    __carouselFilters: Any
    __appliedItems: Any
    __baseStyleItems: Any
    __appliedInAnySeason: Any
    __dependentItems: Any
    __carouselData: Any
    __carouselCache: Any
    __uiLogger: Any
    def __init__(self, carouselItemWrapper):
        ...
    def _dispose(self):
        ...
    @property
    def collection(self):
        ...
    @property
    def sortedCollection(self):
        ...
    @property
    def itemCount(self):
        ...
    @property
    def totalItemCount(self):
        ...
    def pyGetSelectedIdx(self):
        ...
    def getItemIndexHandler(self, fieldName, value):
        ...
    def emptyItem(self):
        ...
    def refresh(self):
        ...
    def buildList(self):
        ...
    def getVisibleTabs(self):
        ...
    def getEnabledTabs(self):
        ...
    def getItemsData(self, season=None, modeId=None, tabId=None):
        ...
    def getCarouselData(self, season=None, modeId=None, tabId=None):
        ...
    def getAppliedItems(self):
        ...
    def getBaseStyleItems(self):
        ...
    def getItemSizeData(self):
        ...
    def getBookmarskData(self):
        ...
    def getArrowsData(self):
        ...
    def getShowSeparatorsData(self):
        ...
    def getDependentItems(self):
        ...
    def processDependentParams(self, item):
        ...
    def onModeChanged(self, modeId, prevModeId):
        ...
    def hasAppliedFilter(self):
        ...
    def selectItem(self, item=None):
        ...
    def getNextItem(self, reverse):
        ...
    def getFilterData(self):
        ...
    def clearFilter(self):
        ...
    def invalidateItems(self):
        ...
    def invalidateFilteredItems(self):
        ...
    def updateSelectedGroup(self, index, isReset=False):
        ...
    def updateCarouselFilter(self, filterType, value, *alias):
        ...
    def isFilterApplied(self, filterType, *alias):
        ...
    def __initFilters(self):
        ...
    def __getSelectedGroupIdx(self):
        ...
    def __setSelectedGroupIdx(self, index=None):
        ...
    def __createFilterCriteria(self):
        ...
    def __createSortCriteria(self):
        ...
    def __updateCarouselData(self):
        ...
    def __updateSwitchers(self):
        ...
    def __updateSelection(self, intCD):
        ...

class FilterTypes(object):
    HISTORIC = 1
    INVENTORY = 2
    APPLIED = 3
    USED_UP = 4
    EDITABLE_STYLES = 5
    PROGRESSION = 6
    FORMFACTORS = 7
    RARITY = 8

class FilterAliases(object):
    HISTORIC = 'historic'
    NON_HISTORIC = 'nonHistoric'
    FANTASTICAL = 'fantastical'
    EDITABLE_STYLES = 'editableStyles'
    NON_EDITABLE_STYLES = 'nonEditableStyles'
    LOCKED = 'locked'

class FilterAttributes(object):
    RARITY = 'rarity'

class SimpleCarouselFilter(object):
    __applied: Any
    __criteria: Any
    __inverse: Any
    __requirements: Any
    def __init__(self, criteria, requirements=None, inverse=False):
        ...
    def fini(self):
        ...
    @property
    def isAvailable(self):
        ...
    @property
    def isInverse(self):
        ...
    @property
    def criteria(self):
        ...
    def isApplied(self):
        ...
    def isEnabled(self):
        ...
    def update(self, value):
        ...
    def clear(self):
        ...

class DisjunctionCarouselFilter(object):
    __applied: Any
    __criteria: Any
    __requirements: Any
    def __init__(self, criteria, requirements=None):
        ...
    def fini(self):
        ...
    @property
    def isAvailable(self):
        ...
    @property
    def criteria(self):
        ...
    def isApplied(self, alias=None):
        ...
    def isEnabled(self, alias=None):
        ...
    def update(self, value, alias):
        ...
    def clear(self):
        ...

class FormfactorsCarouselFilter(SimpleCarouselFilter):
    __formfactors: Any
    def __init__(self, requirements=None):
        ...
    def fini(self):
        ...
    @property
    def formfactors(self):
        ...
    def update(self, value):
        ...
    def clear(self):
        ...

class AttributeCarouselFilter(SimpleCarouselFilter):
    __values: Any
    __attribute: Any
    def __init__(self, attribute, requirements=None):
        ...
    def fini(self):
        ...
    @property
    def attribute(self):
        ...
    @property
    def values(self):
        ...
    def update(self, value):
        ...
    def clear(self):
        ...

def comparisonKey(item):
    ...
