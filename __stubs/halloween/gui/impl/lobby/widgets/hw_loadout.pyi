# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/impl/lobby/widgets/hw_loadout.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from account_helpers.settings_core.options import KeyboardSetting as KeyboardSetting
from account_helpers.settings_core.settings_constants import CONTROLS as CONTROLS
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from constants import LoadoutParams as LoadoutParams
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.impl import backport as backport
from gui.impl.auxiliary.tooltips.simple_tooltip import createSimpleTooltip as createSimpleTooltip
from gui.impl.backport import BackportTooltipWindow as BackportTooltipWindow
from gui.impl.backport import TooltipData as TooltipData
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.base_setup_model import BaseSetupModel as BaseSetupModel
from gui.impl.gen.view_models.views.lobby.tank_setup.tank_setup_constants import TankSetupConstants as TankSetupConstants
from gui.impl.lobby.hangar.presenters.consumables_presenter import ConsumablesPresenter as ConsumablesPresenter
from gui.impl.lobby.hangar.presenters.equipments_presenter import EquipmentsPresenter as EquipmentsPresenter
from gui.impl.lobby.hangar.presenters.instructions_presenter import InstructionsPresenter as InstructionsPresenter
from gui.impl.lobby.hangar.presenters.loadout_presenter import _LoadoutStatesObserver as _LoadoutStatesObserver, LoadoutPresenter as LoadoutPresenter
from gui.impl.lobby.hangar.presenters.loadout_presenter_base import LoadoutEntityProvider as LoadoutEntityProvider
from gui.impl.lobby.hangar.presenters.shells_presenter import ShellsPresenter as ShellsPresenter
from gui.impl.lobby.tank_setup.configurations.consumable import ConsumableTabs as ConsumableTabs
from gui.impl.pub import ToolTipWindow as ToolTipWindow
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from halloween.gui.halloween_account_settings import getSettings as getSettings, AccountSettingsKeys as AccountSettingsKeys
from halloween.gui.halloween_gui_constants import AmmoPanelSwitchPreset as AmmoPanelSwitchPreset, HALLOWEEN_ABILITY_TOOLTIP as HALLOWEEN_ABILITY_TOOLTIP, HALLOWEEN_MAIN_SHELL as HALLOWEEN_MAIN_SHELL
from halloween.gui.impl.gen.view_models.views.lobby.ext_ammo_panel_view import ExtAmmoPanelView as ExtAmmoPanelView
from halloween.gui.impl.lobby.hw_ammunition_panel_view import HWHangarAmmunitionGroupsController as HWHangarAmmunitionGroupsController, _CMD_ACCELERATION_ABILITY_KEY as _CMD_ACCELERATION_ABILITY_KEY
from halloween.gui.impl.lobby.hw_helpers.anomalies_helpers import isAnomaliesSystemAvailable as isAnomaliesSystemAvailable
from halloween.gui.impl.lobby.tank_setup import HWTankSetupConstants as HWTankSetupConstants
from halloween.gui.impl.lobby.tank_setup.array_provider import HalloweenConsumableProvider as HalloweenConsumableProvider
from halloween.gui.impl.lobby.tank_setup.interactor import HalloweenInteractor as HalloweenInteractor
from halloween.gui.impl.lobby.tooltips.ability_tooltip import AbilityTooltipView as AbilityTooltipView
from halloween.gui.impl.lobby.tooltips.anomalies_entry_point_tooltip import AnomaliesEntryPointTooltipView as AnomaliesEntryPointTooltipView
from halloween.gui.shared.event_dispatcher import showModuleInfo as showModuleInfo
from halloween_common.halloween_constants import HW_BUILT_IN_EQUIPMENT as HW_BUILT_IN_EQUIPMENT
from helpers import dependency as dependency
from items import vehicles as vehicles
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from gui.impl.common.ammunition_panel.ammunition_groups_controller import AmmunitionGroupsController as AmmunitionGroupsController
_TOOLTIPS_OVERRIDES: dict
_PRESET_GROUP_SECTIONS: dict

class _HalloweenLoadoutStatesObserver(_LoadoutStatesObserver):
    _GROUP_SECTIONS_NAMES: Any
    @property
    def _stateID(self):
        ...
    def onEnterState(self, state, event):
        ...

class HalloweenLoadoutPresenter(LoadoutPresenter):
    __settingsCore: Any
    _VIEW_MODEL = ExtAmmoPanelView
    _STATES_OBSERVER = _HalloweenLoadoutStatesObserver
    def createToolTip(self, event):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _createAmmunitionGroupsController(self, vehicle):
        ...
    def _onLoading(self, *args):
        ...
    def _getEvents(self):
        ...
    def __onSettingsApplied(self, diff):
        ...
    def _getChildComponents(self):
        ...

# base nao representavel no stub: ViewComponent[...]
class HalloweenPresetSwitcher:
    __groupController: Any
    __panelViewModel: Any
    def __init__(self, groupController=None, panelViewModel=None):
        ...
    def _getEvents(self):
        ...
    def __onSwitch(self):
        ...

class HalloweenConsumablesPresenter(ConsumablesPresenter):
    _sectionName: Any
    _provider: Any
    def __init__(self, interactingItem):
        ...
    def createSlotActions(self):
        ...
    def _onShowItemInfo(self, args):
        ...
    def _createProvider(self, vehInteractingItem):
        ...

def getCurrentPreset():
    ...
