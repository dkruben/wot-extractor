# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/customization/context/styled_mode.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from adisp import adisp_async as adisp_async, adisp_process as adisp_process
from constants import CLIENT_COMMAND_SOURCES as CLIENT_COMMAND_SOURCES
from gui.Scaleform.daapi.view.lobby.customization.context.customization_mode import CustomizationMode as CustomizationMode
from gui.Scaleform.daapi.view.lobby.customization.shared import OutfitInfo as OutfitInfo, customizationSlotIdToUid as customizationSlotIdToUid, CustomizationSlotUpdateVO as CustomizationSlotUpdateVO, getStylePurchaseItems as getStylePurchaseItems, removeItemFromEditableStyle as removeItemFromEditableStyle, fitOutfit as fitOutfit, getCurrentVehicleAvailableRegionsMap as getCurrentVehicleAvailableRegionsMap, getEditableStyleOutfitDiff as getEditableStyleOutfitDiff, getStyledModeRequestData as getStyledModeRequestData
from gui.customization.shared import C11nId as C11nId
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.gui_items.processors.common import CustomizationsSeller as CustomizationsSeller, OutfitApplier as OutfitApplier
from gui.shared.gui_items.processors.vehicle import VehicleAutoStyleEquipProcessor as VehicleAutoStyleEquipProcessor
from gui.shared.utils.decorators import adisp_process as wrappedProcess
from items.components.c11n_constants import SeasonType as SeasonType
from items.customizations import CustomizationOutfit as CustomizationOutfit
from vehicle_outfit.outfit import Area as Area, Outfit as Outfit
from helpers import dependency as dependency
from account_helpers.settings_core.settings_constants import OnceOnlyHints as OnceOnlyHints
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from tutorial.hints_manager import HINT_SHOWN_STATUS as HINT_SHOWN_STATUS
from vehicle_systems.camouflages import getStyleProgressionOutfit as getStyleProgressionOutfit
from items.customizations import parseCompDescr as parseCompDescr
from items.customizations import SerializableComponent as SerializableComponent
from gui.customization.shared import PurchaseItem as PurchaseItem
from gui.shared.gui_items.customization.c11n_items import Style as Style, Customization as Customization
from gui.Scaleform.daapi.view.lobby.customization.context.context import CustomizationContext as CustomizationContext
_logger: Any

class StyledMode(CustomizationMode):
    STYLE_SLOT: Any
    _settingsCore: Any
    __originalStyle: Any
    __modifiedStyle: Any
    __prolongRent: Any
    __autoRentEnabled: Any
    __autoRentChangeSource: Any
    __is3DMode: Any
    _autoRentEnabled: Any
    _modifiedOutfits: Any
    def __init__(self, ctx, is3DMode):
        ...
    @property
    def originalStyle(self):
        ...
    @property
    def modifiedStyle(self):
        ...
    def isAutoRentEnabled(self):
        ...
    def changeAutoRent(self, source=...):
        ...
    def getStyleInfo(self):
        ...
    def getPurchaseItems(self):
        ...
    def getDependenciesData(self):
        ...
    def removeStyle(self, intCD, refresh=True):
        ...
    def prolongRent(self, style):
        ...
    def changeStyleProgressionLevel(self, toLevel):
        ...
    def getStyleProgressionLevel(self):
        ...
    def clearStyle(self):
        ...
    def _onStart(self):
        ...
    def _fillOutfits(self):
        ...
    def _selectItem(self, intCD, progressionLevel=0):
        ...
    def _installItem(self, intCD, slotId, season=None, component=None):
        ...
    def _removeItem(self, slotId, season=None):
        ...
    def _cancelChanges(self):
        ...
    def _getRequestData(self, purchaseItems):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def _applyItems(self, purchaseItems, callback):
        ...
    # decorador original: @adisp_async
    # decorador original: @wrappedProcess(...)
    def _sellItem(self, item, count, callback):
        ...
    def _getAppliedItems(self, isOriginal=True):
        ...
    def _isOutfitsEmpty(self):
        ...
    def _isOutfitsModified(self):
        ...
    def _getAnchorVOs(self):
        ...
    def _onVehicleChangeStarted(self):
        ...
