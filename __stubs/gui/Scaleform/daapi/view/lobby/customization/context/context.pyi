# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/customization/context/context.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from future.utils import viewvalues as viewvalues
import Event as Event
from CurrentVehicle import g_currentVehicle as g_currentVehicle, g_currentPreviewVehicle as g_currentPreviewVehicle
import adisp as adisp
from gui import g_tankActiveCamouflage as g_tankActiveCamouflage
from gui.Scaleform.daapi.view.lobby.customization.context.custom_mode import CustomMode as CustomMode
from gui.Scaleform.daapi.view.lobby.customization.context.editable_style_mode import EditableStyleMode as EditableStyleMode
from gui.Scaleform.daapi.view.lobby.customization.context.styled_diffs_cache import StyleDiffsCache as StyleDiffsCache
from gui.Scaleform.daapi.view.lobby.customization.context.styled_mode import StyledMode as StyledMode
from gui.Scaleform.daapi.view.lobby.customization.shared import CustomizationTabs as CustomizationTabs, resetC11nItemsNovelty as resetC11nItemsNovelty, getCommonPurchaseItems as getCommonPurchaseItems, vehicleHasSlot as vehicleHasSlot, remove3DStyleIncompatibleCommonItems as remove3DStyleIncompatibleCommonItems, removeUncommonItems as removeUncommonItems
from gui.Scaleform.daapi.view.lobby.customization.vehicle_anchors_updater import VehicleAnchorsUpdater as VehicleAnchorsUpdater
from gui.customization.constants import CustomizationModes as CustomizationModes
from gui.hangar_cameras.c11n_hangar_camera_manager import C11nHangarCameraManager as C11nHangarCameraManager
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.utils.decorators import adisp_process as adisp_process
from functools import partial as partial
from helpers import dependency as dependency
from items.components.c11n_constants import SeasonType as SeasonType
from shared_utils import first as first, nextTick as nextTick
from skeletons.gui.customization import ICustomizationService as ICustomizationService
from skeletons.gui.shared import IItemsCache as IItemsCache
from skeletons.gui.shared.utils import IHangarSpace as IHangarSpace
from soft_exception import SoftException as SoftException
from vehicle_outfit.outfit import Area as Area
from gui.customization.shared import C11nId as C11nId, PurchaseItem as PurchaseItem
from gui.customization.constants import CustomizationModeSource as CustomizationModeSource
_logger: Any

class _CustomizationEvents(object):
    _eventsManager: Any
    onBeforeModeChange: Any
    onModeChanged: Any
    onTabChanged: Any
    onSeasonChanged: Any
    onCacheResync: Any
    onSlotSelected: Any
    onSlotUnselected: Any
    onItemSelected: Any
    onItemUnselected: Any
    onItemInstalled: Any
    onItemsRemoved: Any
    onComponentChanged: Any
    onItemsBought: Any
    onItemSold: Any
    onItemLimitReached: Any
    onChangesCanceled: Any
    onCarouselFiltered: Any
    onFilterPopoverClosed: Any
    onPropertySheetShown: Any
    onPropertySheetHidden: Any
    onAnchorHovered: Any
    onAnchorUnhovered: Any
    onAnchorsStateChanged: Any
    onGetItemBackToHand: Any
    onUpdateSwitchers: Any
    onInstallNextCarouselItem: Any
    onShowStyleInfo: Any
    onHideStyleInfo: Any
    onUpdateStyleInfoDOF: Any
    onEditModeEnabled: Any
    onPersonalNumberCleared: Any
    onProlongStyleRent: Any
    onCloseDialogShown: Any
    onCloseDialogClosed: Any
    def __init__(self):
        ...
    def fini(self):
        ...

class CustomizationContext(object):
    _service: Any
    _itemsCache: Any
    _hangarSpace: Any
    _vehicle: Any
    __season: Any
    __modeId: Any
    __styleModeId: Any
    __modes: Any
    __events: Any
    __isItemsOnAnotherVeh: Any
    __isProgressiveItemsExist: Any
    __isModeChangeInProgress: Any
    __vehicleAnchorsUpdater: Any
    __c11nCameraManager: Any
    __stylesDiffsCache: Any
    __commonOriginalOutfit: Any
    __commonOriginal3DOutfit: Any
    __commonModifiedOutfit: Any
    __commonOutfitStyleId: Any
    __commonOutfitDiff: Any
    __carouselItems: Any
    __initialItemCD: Any
    __applyingItems: Any
    def __init__(self):
        ...
    @property
    def vehicle(self):
        ...
    @property
    def isItemsOnAnotherVeh(self):
        ...
    @property
    def isProgressiveItemsExist(self):
        ...
    def setIsProgressiveItemsExist(self, value):
        ...
    @property
    def carouselItems(self):
        ...
    def setCarouselItems(self, carouselItems):
        ...
    @property
    def events(self):
        ...
    @property
    def season(self):
        ...
    @property
    def modeId(self):
        ...
    @property
    def mode(self):
        ...
    @property
    def styleMode(self):
        ...
    @property
    def vehicleAnchorsUpdater(self):
        ...
    @property
    def c11nCameraManager(self):
        ...
    @property
    def stylesDiffsCache(self):
        ...
    @property
    def commonOriginalOutfit(self):
        ...
    @property
    def commonModifiedOutfit(self):
        ...
    @property
    def isModeChangeInProgress(self):
        ...
    @property
    def applyingItems(self):
        ...
    def setIsItemsOnAnotherVeh(self, value):
        ...
    def init(self, season=None, modeId=None, tabId=None, itemCD=None):
        ...
    def fini(self):
        ...
    def changeMode(self, modeId, tabId=None, source=None):
        ...
    def editStyle(self, intCD, source=None):
        ...
    def canEditStyle(self, itemCD):
        ...
    def changeModeWithProgressionDecal(self, itemCD, scrollToItem=False):
        ...
    def changeSeason(self, season):
        ...
    def selectSlot(self, slotId):
        ...
    def unselectSlot(self):
        ...
    def selectItem(self, intCD, progressionLevel=-1):
        ...
    def unselectItem(self):
        ...
    def cancelChanges(self):
        ...
    def removeOldSeasonPreview(self, season):
        ...
    def getPurchaseItems(self):
        ...
    def getNotModifedCommonItems(self):
        ...
    def updateCommonOutfits(self):
        ...
    def updateOutfits(self):
        ...
    def refreshOutfit(self, season=None):
        ...
    # decorador original: @adisp.adisp_async
    # decorador original: @adisp_process(...)
    def applyItems(self, purchaseItems, callback):
        ...
    def isCommonOutfitModified(self):
        ...
    def isOutfitsModified(self):
        ...
    @staticmethod
    def resetItemsNovelty(items):
        ...
    def returnToStyleMode(self, source=None):
        ...
    def hasCommonItems(self):
        ...
    def isInStyleMode(self, styleModeId):
        ...
    def __onCacheResync(self, reason, items):
        ...
    def __onVehicleChanged(self):
        ...
    def __onPreviewVehicleChanged(self):
        ...
    def __onVehicleChangeStarted(self):
        ...
    def __onOutfitChanged(self):
        ...
    def __getStartSeason(self):
        ...
    def __getStartMode(self, modeId=None, tabId=None):
        ...
    def __getDefaultStartMode(self):
        ...
