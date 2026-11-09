# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/nation_change/nation_change_screen.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import SoundGroups as SoundGroups
import WWISE as WWISE
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from account_helpers.AccountSettings import NATION_CHANGE_VIEWED as NATION_CHANGE_VIEWED, AccountSettings as AccountSettings
from frameworks.wulf import ViewSettings as ViewSettings
from frameworks.wulf import ViewStatus as ViewStatus
from gui import SystemMessages as SystemMessages
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.impl import backport as backport
from gui.impl.backport.backport_tooltip import TooltipData as TooltipData, BackportTooltipWindow as BackportTooltipWindow
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.nation_change.nation_change_device_model import NationChangeDeviceModel as NationChangeDeviceModel
from gui.impl.gen.view_models.views.lobby.nation_change.nation_change_screen_model import NationChangeScreenModel as NationChangeScreenModel
from gui.impl.gen.view_models.views.lobby.nation_change.nation_change_shell_model import NationChangeShellModel as NationChangeShellModel
from gui.impl.gen.view_models.views.lobby.nation_change.nation_change_supply_model import NationChangeSupplyModel as NationChangeSupplyModel
from gui.impl.gen.view_models.views.lobby.nation_change.nation_change_tankman_model import NationChangeTankmanModel as NationChangeTankmanModel
from gui.impl.gen.view_models.views.lobby.nation_change.nation_change_tank_setup_model import NationChangeTankSetupModel as NationChangeTankSetupModel
from gui.impl.pub import ViewImpl as ViewImpl
from gui.shared import event_dispatcher as event_dispatcher
from gui.shared.gui_items.Vehicle import getNationLessName as getNationLessName, getIconResourceName as getIconResourceName, sortCrew as sortCrew
from gui.shared.gui_items.processors.common import VehicleChangeNation as VehicleChangeNation
from gui.shared.utils import decorators as decorators
from gui.shared.utils.functions import getVehTypeIconName as getVehTypeIconName
from gui.shared.utils.role_presenter_helper import getRoleUserName as getRoleUserName
from helpers import int2roman as int2roman
from helpers.dependency import descriptor as descriptor
from helpers.server_settings import serverSettingsChangeListener as serverSettingsChangeListener
from items.components.crew_skins_constants import NO_CREW_SKIN_ID as NO_CREW_SKIN_ID
from nation_change.nation_change_helpers import iterVehTypeCDsInNationGroup as iterVehTypeCDsInNationGroup
from post_progression_common import SERVER_SETTINGS_KEY as SERVER_SETTINGS_KEY, SWITCH_LAYOUT_CAPACITY as SWITCH_LAYOUT_CAPACITY
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache

class NationChangeScreen(ViewImpl):
    __itemsCache: Any
    __lobbyContext: Any
    __appLoader: Any
    _DOG_SOUND = 'rudy'
    _HANGAR_SOUND_FILTERED_STATE_NAME = 'STATE_hangar_filtered'
    _HANGAR_SOUND_FILTERED_STATE_ON = 'STATE_hangar_filtered_on'
    _HANGAR_SOUND_FILTERED_STATE_OFF = 'STATE_hangar_filtered_off'
    __LAYOUTS_IN_SETUP = 4
    __slots__: tuple
    __icons: Any
    __currentVehicle: Any
    __targetVehicle: Any
    def __init__(self, viewKey, ctx=None):
        ...
    @property
    def viewModel(self):
        ...
    def createToolTip(self, event):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def __getBackportTooltipData(self, event):
        ...
    def __updateTankSlot(self, tankSlotVM, vehicle):
        ...
    def __setSetupData(self, setupModel, guiVh, layoutIndexes):
        ...
    def __setCrewViewModelData(self, tankSlotVM, guiVh):
        ...
    def __setEquipmentViewModelData(self, slotVM, guiVh, layoutIdx):
        ...
    def __setDevicesViewModelData(self, slotVM, guiVh, layoutIdx):
        ...
    def __setShellsViewModelData(self, slotVM, guiVh, layoutIdx):
        ...
    def __setInstructionViewModelData(self, slotVM, guiVh, layoutIdx):
        ...
    def __playAnimation(self):
        ...
    def __setViewed(self):
        ...
    def __addListeners(self):
        ...
    def __removeListeners(self):
        ...
    # decorador original: @serverSettingsChangeListener(...)
    def __onServerSettingsChange(self, diff):
        ...
    def __onVehiclesInInventoryUpdate(self, diff):
        ...
    def __onWindowClose(self):
        ...
    def __onHangarBtnClick(self):
        ...
    def __onDogClick(self):
        ...
    # decorador original: @decorators.adisp_process(...)
    def __onSwitchBtnClick(self):
        ...
    def __onCancelBtnClick(self):
        ...
