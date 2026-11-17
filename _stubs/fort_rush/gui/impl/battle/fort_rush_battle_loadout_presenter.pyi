# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/client/fort_rush/gui/impl/battle/fort_rush_battle_loadout_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import json as json
import logging as logging
from typing import List as List, Callable as Callable, Optional as Optional
import BigWorld as BigWorld
from Vehicle import Vehicle as Vehicle
from gui.battle_control import avatar_getter as avatar_getter
from gui.impl.gen import R as R
from gui.impl.gen.view_models.constants.item_highlight_types import ItemHighlightTypes as ItemHighlightTypes
from gui.impl.gen.view_models.views.lobby.loadout.consumables.consumables_model import ConsumablesModel as ConsumablesModel
from gui.impl.gen.view_models.views.lobby.loadout.equipments.equipments_model import EquipmentsModel as EquipmentsModel
from gui.impl.gen.view_models.views.lobby.loadout.panel.ammunition.ammunition_panel_model import AmmunitionPanelModel as AmmunitionPanelModel
from gui.impl.gen.view_models.views.lobby.loadout.shells.shell_model import ShellModel as ShellModel
from gui.impl.gen.view_models.views.lobby.loadout.shells.shells_model import ShellsModel as ShellsModel
from gui.impl.gen.view_models.views.lobby.tank_setup.common.ammunition_items_group import AmmunitionItemsGroup as AmmunitionItemsGroup
from gui.impl.gen.view_models.views.lobby.tank_setup.common.ammunition_items_section import AmmunitionItemsSection as AmmunitionItemsSection
from gui.impl.gen.view_models.views.lobby.tank_setup.common.ammunition_setup_selector import SetupStates as SetupStates
from gui.impl.gen.view_models.views.lobby.tank_setup.common.base_ammunition_slot import BaseAmmunitionSlot as BaseAmmunitionSlot
from gui.impl.gen.view_models.views.lobby.tank_setup.common.opt_device_ammunition_slot import OptDeviceAmmunitionSlot as OptDeviceAmmunitionSlot
from gui.impl.gen.view_models.views.lobby.tank_setup.common.shell_ammunition_slot import ShellAmmunitionSlot as ShellAmmunitionSlot
from gui.impl.gen.view_models.views.lobby.tank_setup.common.specialization_model import SpecializationModel as SpecializationModel
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.consumable_slot_model import ConsumableSlotModel as ConsumableSlotModel
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.opt_device_slot_model import OptDeviceSlotModel as OptDeviceSlotModel
from gui.impl.gen.view_models.views.lobby.tank_setup.tank_setup_constants import TankSetupConstants as TankSetupConstants
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.shared.gui_items.artefacts import Equipment as Equipment, OptionalDevice as OptionalDevice
from gui.shared.gui_items.vehicle_equipment import _EquipmentsSetupGroups as _EquipmentsSetupGroups
from helpers import dependency as dependency
from post_progression_common import TankSetupGroupsId as TankSetupGroupsId
from skeletons.gui.shared import IItemsCache as IItemsCache
_logger: Any
_GROUP_ID_EQUIPMENT_AND_SHELLS = TankSetupGroupsId.EQUIPMENT_AND_SHELLS
_GROUP_ID_OPT_DEVICES = TankSetupGroupsId.OPTIONAL_DEVICES_AND_BOOSTERS

class FortRushBattleLoadoutPresenter(ViewComponent):
    _itemsCache: Any
    _vehicleItem: Any
    _onSwitchCallback: Any
    def __init__(self, vehicleItem):
        ...
    def updateVehicle(self, vehicleItem):
        ...
    def _updateChildrenVehicle(self, vehicleItem):
        ...
    def setOnSwitchCallback(self, callback):
        ...
    @property
    def viewModel(self):
        ...
    def _getChildComponents(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _onChangeSetupIndex(self, args):
        ...
    def _getGroupCapacity(self, setupLayouts, groupId):
        ...
    def _getLayoutIndex(self, setupLayouts, groupId):
        ...
    def _createSection(self, sectionType):
        ...
    def _setupSlotBasics(self, slot, idx, item):
        ...
    def _setGroupSections(self, group, sections):
        ...
    def _setSelector(self, group, groupId, totalSetups, applySetupStates=False):
        ...
    def _createAmmunitionGroup(self, groupId, setupIdx, totalSetups, applySetupStates=False):
        ...
    def _buildShellsAndConsumablesGroup(self, setupLayouts):
        ...
    def _buildOptDevicesAndBoostersGroup(self, setupLayouts):
        ...
    def _buildShellsSection(self):
        ...
    def _buildConsumablesSection(self):
        ...
    def _buildOptDevicesSection(self):
        ...
    def _setupOptDeviceOverlay(self, slot, device):
        ...
    def _setupOptDeviceSpecializations(self, slot, idx, device):
        ...
    def _buildBoostersSection(self):
        ...
    def _setupBoosterOverlay(self, slot, booster):
        ...
    def _updateModel(self):
        ...

class _FortRushBattleConsumablesPresenter(ViewComponent):
    _itemsCache: Any
    _vehicleItem: Any
    def __init__(self, vehicleItem):
        ...
    def updateVehicle(self, vehicleItem):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _updateModel(self):
        ...

class _FortRushBattleShellsPresenter(ViewComponent):
    _itemsCache: Any
    _vehicleItem: Any
    def __init__(self, vehicleItem):
        ...
    def updateVehicle(self, vehicleItem):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _updateModel(self):
        ...

class _FortRushBattleEquipmentsPresenter(ViewComponent):
    _itemsCache: Any
    _vehicleItem: Any
    def __init__(self, vehicleItem):
        ...
    def updateVehicle(self, vehicleItem):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _updateModel(self):
        ...

def _computeSetupStates(vehicle, totalSetups):
    ...
