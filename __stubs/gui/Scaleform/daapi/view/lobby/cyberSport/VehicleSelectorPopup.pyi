# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/cyberSport/VehicleSelectorPopup.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from account_helpers.AccountSettings import AccountSettings as AccountSettings
from constants import VEHICLE_CLASSES as VEHICLE_CLASSES, BATTLE_MODE_VEHICLE_TAGS as BATTLE_MODE_VEHICLE_TAGS
from gui.Scaleform.daapi.view.lobby.vehicle_selector_base import VehicleSelectorBase as VehicleSelectorBase
from gui.Scaleform.daapi.view.lobby.rally.vo_converters import makeVehicleVO as makeVehicleVO
from gui.Scaleform.daapi.view.meta.VehicleSelectorPopupMeta import VehicleSelectorPopupMeta as VehicleSelectorPopupMeta
from gui.Scaleform.genConsts.VEHICLE_SELECTOR_CONSTANTS import VEHICLE_SELECTOR_CONSTANTS as VEHICLE_SELECTOR_CONSTANTS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS as TOOLTIPS
from gui.shared.events import CSVehicleSelectEvent as CSVehicleSelectEvent, HideWindowEvent as HideWindowEvent
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache

class VehicleSelectorPopup(VehicleSelectorPopupMeta, VehicleSelectorBase):
    itemsCache: Any
    _levelsRange: Any
    __isMultiSelect: Any
    _infoText: Any
    __componentsOffset: Any
    _titleText: Any
    _selectButton: Any
    _cancelButton: Any
    _compatibleOnlyLabel: Any
    __section: Any
    _vehicles: Any
    __selectedVehicles: Any
    __vehicleTypes: Any
    _filterVisibility: Any
    showNotReadyVehicles: Any
    only_: Any
    def __init__(self, ctx=None):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def onWindowForceClose(self, _):
        ...
    def onWindowClose(self):
        ...
    def onSelectVehicles(self, items):
        ...
    def onFiltersUpdate(self, nation, vehicleType, isMain, level, compatibleOnly):
        ...
    def initFilters(self):
        ...
    def updateData(self):
        ...
    def setListData(self, vehicleVOs, selected):
        ...
    def selectClick(self):
        ...
    def _makeVehicleVOAction(self, vehicle):
        ...
