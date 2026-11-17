# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/impl/lobby/widgets/ls_loadout.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from constants import LoadoutParams as LoadoutParams
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.impl.backport import BackportTooltipWindow as BackportTooltipWindow
from gui.impl.backport import TooltipData as TooltipData
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.base_setup_model import BaseSetupModel as BaseSetupModel
from gui.impl.gen.view_models.views.lobby.tank_setup.tank_setup_constants import TankSetupConstants as TankSetupConstants
from gui.impl.lobby.hangar.presenters.consumables_presenter import ConsumablesPresenter as ConsumablesPresenter
from gui.impl.lobby.hangar.presenters.equipments_presenter import EquipmentsPresenter as EquipmentsPresenter
from gui.impl.lobby.hangar.presenters.instructions_presenter import InstructionsPresenter as InstructionsPresenter
from gui.impl.lobby.hangar.presenters.loadout_presenter import _LoadoutStatesObserver as _LoadoutStatesObserver, LoadoutPresenter as LoadoutPresenter
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from last_stand.gui.impl.gen.view_models.views.lobby.ext_ammo_panel_view import ExtAmmoPanelView as ExtAmmoPanelView
from gui.impl.lobby.hangar.presenters.loadout_presenter_base import LoadoutEntityProvider as LoadoutEntityProvider
from gui.impl.lobby.hangar.presenters.shells_presenter import ShellsPresenter as ShellsPresenter
from gui.impl.lobby.tank_setup.configurations.consumable import ConsumableTabs as ConsumableTabs
from gui.impl.gen.view_models.views.lobby.loadout.panel.ammunition.ammunition_panel_model import AmmunitionPanelModel as AmmunitionPanelModel
from last_stand.gui.impl.lobby.hangar_ammunition_panel_view import LSHangarAmmunitionGroupsController as LSHangarAmmunitionGroupsController
from last_stand.gui.impl.lobby.tank_setup import LSTankSetupConstants as LSTankSetupConstants
from last_stand.gui.impl.lobby.tank_setup.array_provider import LSConsumableProvider as LSConsumableProvider
from last_stand.gui.impl.lobby.tank_setup.interactor import LSConsumableInteractor as LSConsumableInteractor
from last_stand.gui.ls_account_settings import getSettings as getSettings, AccountSettingsKeys as AccountSettingsKeys
from last_stand.gui.ls_gui_constants import AmmoPanelSwitchPreset as AmmoPanelSwitchPreset, LS_ABILITY_TOOLTIP as LS_ABILITY_TOOLTIP, LS_MAIN_SHELL as LS_MAIN_SHELL
from last_stand.gui.shared.event_dispatcher import showModuleInfo as showModuleInfo
from last_stand.gui.sounds import playSound as playSound
from last_stand.gui.sounds.sound_constants import CONSUMABLES_VIEW_ENTER as CONSUMABLES_VIEW_ENTER, CONSUMABLES_VIEW_EXIT as CONSUMABLES_VIEW_EXIT
from gui.impl.common.ammunition_panel.ammunition_groups_controller import AmmunitionGroupsController as AmmunitionGroupsController
_TOOLTIPS_OVERRIDES: dict
_PRESET_GROUP_SECTIONS: dict

class _LastStandLoadoutStatesObserver(_LoadoutStatesObserver):
    @property
    def _stateID(self):
        ...
    def onEnterState(self, state, event):
        ...
    def onStateChanged(self, state, stateEntered, event=None):
        ...

class LastStandLoadoutPresenter(LoadoutPresenter):
    _VIEW_MODEL = AmmunitionPanelModel
    _STATES_OBSERVER = _LastStandLoadoutStatesObserver
    def createToolTip(self, event):
        ...
    def _createAmmunitionGroupsController(self, vehicle):
        ...
    def _getChildComponents(self):
        ...

# base nao representavel no stub: ViewComponent[...]
class LastStandPresetSwitcher:
    __groupController: Any
    __panelViewModel: Any
    def __init__(self, groupController=None, panelViewModel=None):
        ...
    def _getEvents(self):
        ...
    def __onSwitch(self):
        ...

class LastStandConsumablesPresenter(ConsumablesPresenter):
    _sectionName: Any
    _provider: Any
    def __init__(self, interactingItem):
        ...
    def createSlotActions(self):
        ...
    def _onShowItemInfo(self, args):
        ...
    def _getCallbacks(self):
        ...
    def _onLSInventoryUpdate(self, invDiff):
        ...
    def _createProvider(self, vehInteractingItem):
        ...

def getCurrentPreset():
    ...
