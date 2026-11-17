# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/cyberSport/RosterSlotSettingsWindow.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from account_helpers.AccountSettings import AccountSettings as AccountSettings
from gui.Scaleform.daapi.view.lobby.vehicle_selector_base import VehicleSelectorBase as VehicleSelectorBase
from gui.Scaleform.daapi.view.lobby.rally.vo_converters import makeVehicleVO as makeVehicleVO, makeFiltersVO as makeFiltersVO, makeVehicleBasicVO as makeVehicleBasicVO
from gui.Scaleform.daapi.view.meta.RosterSlotSettingsWindowMeta import RosterSlotSettingsWindowMeta as RosterSlotSettingsWindowMeta
from gui.Scaleform.genConsts.CYBER_SPORT_ALIASES import CYBER_SPORT_ALIASES as CYBER_SPORT_ALIASES
from gui.Scaleform.locale.CYBERSPORT import CYBERSPORT as CYBERSPORT
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS as TOOLTIPS
from gui.shared.events import CSRosterSlotSettingsWindow as CSRosterSlotSettingsWindow
from gui.shared.formatters import text_styles as text_styles, icons as icons
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from helpers import dependency as dependency
from nation_change.nation_change_helpers import iterVehTypeCDsInNationGroup as iterVehTypeCDsInNationGroup
from skeletons.gui.shared import IItemsCache as IItemsCache
VEHICLE_SELECTOR_TAB_ID = 'vehicleSelectorTab'
RANGE_SELECTOR_TAB_ID = 'rangeSelectorTab'
TAB_ORDER: list
TAB_DATA_MAP: dict

class RosterSlotSettingsWindow(RosterSlotSettingsWindowMeta, VehicleSelectorBase):
    itemsCache: Any
    _levelsRange: Any
    __section: Any
    __levelsLimits: Any
    __vehicleTypes: Any
    __flashSlots: Any
    __currentSlot: Any
    def __init__(self, ctx=None):
        ...
    def updateSlots(self, slots):
        ...
    def onFiltersUpdate(self, nation, vehicleType, isMain, level, compatibleOnly):
        ...
    def updateData(self):
        ...
    def requestVehicleFilters(self):
        ...
    def submitButtonHandler(self, value):
        ...
    def cancelButtonHandler(self):
        ...
    def onWindowClose(self):
        ...
    def _populate(self):
        ...
    def setLimits(self):
        ...
    def _dispose(self):
        ...
    def _makeVehicleVOAction(self, vehicle):
        ...
    def __packStaticData(self):
        ...
    def __packTabsData(self):
        ...
    def __setSelection(self, tabID):
        ...
    def __makeInitialSlotData(self, currentSlotSetting):
        ...
    def __convertLevelsRange(self, levels):
        ...
    def __getSlotsSettings(self):
        ...
    def __addAditionalSlot(self, slotSettins):
        ...
