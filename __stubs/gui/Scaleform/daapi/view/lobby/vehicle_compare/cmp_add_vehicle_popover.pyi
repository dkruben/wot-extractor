# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/vehicle_compare/cmp_add_vehicle_popover.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.daapi.view.lobby.popover.vehicle_select_popover_base import VehicleSelectPopoverBase as VehicleSelectPopoverBase
from gui.Scaleform.daapi.view.lobby.vehicle_compare.formatters import packHeaderColumnData as packHeaderColumnData
from gui.Scaleform.daapi.view.lobby.vehicle_selector_base import VehicleSelectorBase as VehicleSelectorBase
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.Scaleform.locale.VEH_COMPARE import VEH_COMPARE as VEH_COMPARE
from gui.game_control.veh_comparison_basket import MAX_VEHICLES_TO_COMPARE_COUNT as MAX_VEHICLES_TO_COMPARE_COUNT, getVehicleCriteriaForComparing as getVehicleCriteriaForComparing
from gui.shared.formatters import text_styles as text_styles
from gui.shared.gui_items.Vehicle import getSmallIconPath as getSmallIconPath, getTypeSmallIconPath as getTypeSmallIconPath
from helpers import dependency as dependency
from helpers.i18n import makeString as _ms
from skeletons.gui.game_control import IVehicleComparisonBasket as IVehicleComparisonBasket
from skeletons.gui.shared import IItemsCache as IItemsCache

class VehicleCompareAddVehiclePopover(VehicleSelectPopoverBase, VehicleSelectorBase):
    itemsCache: Any
    comparisonBasket: Any
    def initFilters(self):
        ...
    def applyFilters(self, nation, vehicleType, level, isMain, hangarOnly):
        ...
    def updateData(self, allVehicles=None):
        ...
    def setVehicleSelected(self, dbID, autoClose):
        ...
    def updateAddButtonLabel(self):
        ...
    def addButtonClicked(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _makeVehicleVOAction(self, vehicle):
        ...
    def __onVehCmpBasketStateChanged(self):
        ...
    def __initControls(self):
        ...

def _makeVehicleCmpVO(vehicle):
    ...
