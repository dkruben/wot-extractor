# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/fortifications/fort_vehicle_select_popover.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui import makeHtmlString as makeHtmlString
from gui.Scaleform import MENU as MENU
from gui.Scaleform import getButtonsAssetPath as getButtonsAssetPath
from gui.Scaleform.daapi.view.lobby.vehicle_compare.formatters import packHeaderColumnData as packHeaderColumnData
from gui.Scaleform.daapi.view.lobby.vehicle_selector_base import VehicleSelectorBase as VehicleSelectorBase
from gui.Scaleform.daapi.view.meta.FortVehicleSelectPopoverMeta import FortVehicleSelectPopoverMeta as FortVehicleSelectPopoverMeta
from gui.Scaleform.locale.CYBERSPORT import CYBERSPORT as CYBERSPORT
from gui.Scaleform.locale.FORTIFICATIONS import FORTIFICATIONS as FORTIFICATIONS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS as TOOLTIPS
from gui.Scaleform.locale.VEH_COMPARE import VEH_COMPARE as VEH_COMPARE
from gui.clans.stronghold_event_requester import FrozenVehiclesConstants as FrozenVehiclesConstants
from gui.prb_control.entities.base.unit.listener import IUnitListener as IUnitListener
from gui.shared.events import CSVehicleSelectEvent as CSVehicleSelectEvent, StrongholdEvent as StrongholdEvent
from gui.shared.formatters import text_styles as text_styles
from gui.shared.gui_items.Vehicle import VEHICLE_TYPES_ORDER as VEHICLE_TYPES_ORDER, getSmallIconPath as getSmallIconPath, Vehicle as Vehicle, getTypeSmallIconPath as getTypeSmallIconPath
from gui.shared.utils.functions import makeTooltip as makeTooltip
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from helpers import dependency as dependency
from helpers.i18n import makeString as makeString
from skeletons.gui.shared import IItemsCache as IItemsCache
_IGNORED_VEHICLE_STATES: tuple

class FortVehicleSelectPopover(FortVehicleSelectPopoverMeta, VehicleSelectorBase, IUnitListener):
    itemsCache: Any
    _classFilters: Any
    _isHideFrozen: Any
    _showMainBtn: Any
    _slotIndex: Any
    _levelsRange: Any
    _selectedVehicles: Any
    _isStronghold: Any
    def __init__(self, ctx=None):
        ...
    def setVehicleSelected(self, dbID, autoClose):
        ...
    def updateAddButtonLabel(self):
        ...
    def applyFilters(self, nation, vehicleType, level, isMain, hangarOnly):
        ...
    def onFrozenChange(self, value):
        ...
    def onFilterChange(self, index, value):
        ...
    def initFilters(self):
        ...
    def updateData(self):
        ...
    def addButtonClicked(self):
        ...
    def _populate(self):
        ...
    def _getHeader(self):
        ...
    def _parseFilters(self):
        ...
    def _initFilter(self, nation=-1, vehicleType='none', isMain=False, level=-1, compatibleOnly=False):
        ...
    def _dispose(self):
        ...
    def _makeVehicleVOAction(self, vehicle):
        ...
    def _isSelected(self, entry):
        ...
    def __initControls(self):
        ...
    def __getAssetPath(self, assetType, extension='.png'):
        ...
    def __getIsVehicleFrozen(self, vehicle):
        ...
    def __getIsVehicleReady(self, vehicle):
        ...
    def __createFilterToggles(self):
        ...

def convertState(vState):
    ...
def getVehicleCriteria(levelsRange, inHangar=False, isHideFrozen=False, checkIsFrozen=None):
    ...
