# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/uilogging/customization_3d_objects/logger.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from typing import TYPE_CHECKING as TYPE_CHECKING
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.Scaleform.daapi.view.common.common_constants import FILTER_POPOVER_SECTION as FILTER_POPOVER_SECTION
from gui.Scaleform.daapi.view.common.shared import isVehicleFilterNew as isVehicleFilterNew
from gui.Scaleform.daapi.view.lobby.customization.shared import CustomizationTabs as CustomizationTabs, vehicleHasSlot as vehicleHasSlot
from gui.shared.utils.requesters.ItemsRequester import REQ_CRITERIA as REQ_CRITERIA
from helpers import dependency as dependency
from skeletons.gui.customization import ICustomizationService as ICustomizationService
from uilogging.base.logger import MetricsLogger as MetricsLogger, ifUILoggingEnabled as ifUILoggingEnabled
from uilogging.customization_3d_objects.logging_constants import ATTACHMENT_TYPE_MAPPING as ATTACHMENT_TYPE_MAPPING, CUSTOMIZATION_CAROUSEL_MODE_MAPPING as CUSTOMIZATION_CAROUSEL_MODE_MAPPING, CUSTOMIZATION_CAROUSEL_TAB_MAPPING as CUSTOMIZATION_CAROUSEL_TAB_MAPPING, FEATURE as FEATURE, VEHICLE_CUSTOMIZATION_FILTER_MAPPING as VEHICLE_CUSTOMIZATION_FILTER_MAPPING, CustomizationActions as CustomizationActions, CustomizationCarouselStates as CustomizationCarouselStates, CustomizationChamomileButtons as CustomizationChamomileButtons, CustomizationFilterButtons as CustomizationFilterButtons, CustomizationTutorialStates as CustomizationTutorialStates, CustomizationFilterTypes as CustomizationFilterTypes, CustomizationViewKeys as CustomizationViewKeys
from wotdecorators import noexcept as noexcept
from typing import Optional as Optional, Union as Union, Dict as Dict
from uilogging.types import ItemType as ItemType, InfoType as InfoType, ItemStateType as ItemStateType, ParentScreenType as ParentScreenType
from uilogging.customization_3d_objects.logging_constants import CustomizationButtons as CustomizationButtons
from items.components.c11n_constants import Rarity as Rarity
from gui.customization.shared import C11nId as C11nId
from gui.Scaleform.daapi.view.common.vehicle_carousel.carousel_environment import ICarouselEnvironment as ICarouselEnvironment
from gui.Scaleform.daapi.view.lobby.customization.context.context import CustomizationContext as CustomizationContext
from gui.Scaleform.daapi.view.lobby.customization.customization_carousel import CarouselCache as CarouselCache

class CustomizationMetricsLogger(MetricsLogger):
    __slots__: tuple
    _parentScreen: Any
    def __init__(self, parentScreen=None):
        ...
    def _logAction(self, action, item, itemState=None, parentScreen=None, info=None):
        ...
    def onViewOpen(self, view, itemState=None, parentScreen=None, info=None):
        ...
    def onViewClose(self, view, itemState=None, parentScreen=None, info=None):
        ...
    def onClick(self, item, itemState=None, parentScreen=None, info=None):
        ...

class _TutorialMixin(object):
    __slots__: tuple
    def onHintButtonClick(self, button, isTutorial, parentScreen=None, info=None):
        ...
    def _getTutorialState(self, isTutorial):
        ...

class CustomizationMainViewLogger(CustomizationMetricsLogger):
    __slots__: tuple
    # decorador original: @noexcept
    def onAnchorClick(self, slotId, parentScreen=None):
        ...

class CustomizationPropertySheetLogger(CustomizationMetricsLogger):
    __slots__: tuple
    def onChamomileClick(self, button, slotId):
        ...
    # decorador original: @noexcept
    def onScaleClick(self, scaleIndex, slotId):
        ...
    def __needToLogForSlot(self, slotId):
        ...

class CustomizationAmmunitionPanelLogger(CustomizationMetricsLogger, _TutorialMixin):
    __slots__: tuple

class CustomizationBottomPanelLogger(CustomizationMetricsLogger, _TutorialMixin):
    __slots__: tuple
    __service: Any
    __ctx: Any
    def __init__(self, parentScreen=None):
        ...
    # decorador original: @noexcept
    # decorador original: @ifUILoggingEnabled(...)
    def onTabOpened(self, tabId):
        ...
    # decorador original: @noexcept
    # decorador original: @ifUILoggingEnabled(...)
    def onViewOpen(self, view):
        ...
    # decorador original: @noexcept
    # decorador original: @ifUILoggingEnabled(...)
    def onViewClose(self, view):
        ...
    # decorador original: @noexcept
    # decorador original: @ifUILoggingEnabled(...)
    def onButtonClick(self, button):
        ...
    # decorador original: @noexcept
    # decorador original: @ifUILoggingEnabled(...)
    def onHintButtonClick(self, button, isTutorial):
        ...
    # decorador original: @noexcept
    def onPrimaryFilterClick(self, index):
        ...
    def __getCarouselState(self, tabId):
        ...
    def __needToLogFilterClick(self):
        ...

class VehicleSidebarLogger(CustomizationMetricsLogger):
    __slots__: tuple

class CustomizationFilterLogger(CustomizationMetricsLogger):
    __slots__: tuple
    __service: Any
    __ctx: Any
    def __init__(self, parentScreen=None):
        ...
    # decorador original: @noexcept
    def onViewOpen(self, view, parentScreen=None):
        ...
    # decorador original: @noexcept
    def onViewClose(self, view, parentScreen=None):
        ...
    # decorador original: @noexcept
    def onFilterClick(self, button, parentScreen=None):
        ...
    # decorador original: @noexcept
    def onPrimaryFilterClick(self, button):
        ...
    # decorador original: @noexcept
    def onRarityFilterClick(self, rarity):
        ...
    # decorador original: @noexcept
    def onGroupFilterClick(self, carouselCache, groupIndex, parentScreen=None, isReset=False):
        ...
    def __needToLogFilterClick(self):
        ...

class CustomizationHangarVehicleFilterLogger(CustomizationMetricsLogger, _TutorialMixin):
    __slots__: tuple
    # decorador original: @noexcept
    # decorador original: @ifUILoggingEnabled(...)
    def onFilterButtonClick(self, carousel, mapping, sectionId, itemId):
        ...

class CustomizationRarityRewardViewLogger(CustomizationMetricsLogger):
    __slots__: tuple
