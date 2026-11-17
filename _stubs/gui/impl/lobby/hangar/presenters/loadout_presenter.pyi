# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/hangar/presenters/loadout_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import json as json
import logging as logging
import typing as typing
import Event as Event
import adisp as adisp
from PlayerEvents import g_playerEvents as g_playerEvents
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from constants import LoadoutParams as LoadoutParams
from frameworks_common.state_machine import BaseStateObserver as BaseStateObserver, visitor as visitor
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.Scaleform.lobby_entry import getLobbyStateMachine as getLobbyStateMachine
from gui.game_control.loadout_controller import updateInteractor as updateInteractor
from gui.impl.backport import BackportTooltipWindow as BackportTooltipWindow
from gui.impl.common.ammunition_panel.ammunition_groups_controller import GROUPS_MAP as GROUPS_MAP
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.loadout.panel.ammunition.ammunition_panel_model import AmmunitionPanelModel as AmmunitionPanelModel
from gui.impl.lobby.hangar.presenters.consumables_presenter import ConsumablesPresenter as ConsumablesPresenter
from gui.impl.lobby.hangar.presenters.equipments_presenter import EquipmentsPresenter as EquipmentsPresenter
from gui.impl.lobby.hangar.presenters.instructions_presenter import InstructionsPresenter as InstructionsPresenter
from gui.impl.lobby.hangar.presenters.shells_presenter import ShellsPresenter as ShellsPresenter
from gui.impl.lobby.tank_setup.ammunition_panel.groups_controller import HangarAmmunitionGroupsController as HangarAmmunitionGroupsController
from gui.impl.lobby.tank_setup.backports.tooltips import getSlotSpecTooltipData as getSlotSpecTooltipData, getSlotTooltipData as getSlotTooltipData
from gui.impl.lobby.tank_setup.interactors.base import InteractingItem as InteractingItem
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.prb_control import prbDispatcherProperty as prbDispatcherProperty
from gui.shared import events as events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.gui_items.items_actions import factory as ActionsFactory
from gui.shared.items_cache import CACHE_SYNC_REASON as CACHE_SYNC_REASON
from helpers import dependency as dependency
from post_progression_common import TankSetupGroupsId as TankSetupGroupsId
from skeletons.gui.game_control import ILoadoutController as ILoadoutController, IPlatoonController as IPlatoonController
from skeletons.gui.shared import IItemsCache as IItemsCache
from soft_exception import SoftException as SoftException
from wg_async import wg_async as wg_async
from gui.impl.common.ammunition_panel.ammunition_groups_controller import AmmunitionGroupsController as AmmunitionGroupsController
from gui.lobby_state_machine.lobby_state_machine import LobbyStateMachine as LobbyStateMachine
from frameworks_common.state_machine import StateEvent as StateEvent, State as State
from gui.shared.events import NavigationEvent as NavigationEvent
_logger: Any

class _LoadoutStatesObserver(BaseStateObserver):
    __loadoutController: Any
    __manager: Any
    onPanelSlotSelect: Any
    def __init__(self):
        ...
    def clear(self):
        ...
    def isObservingState(self, state):
        ...
    def onStateChanged(self, state, stateEntered, event=None):
        ...
    def onEnterState(self, state, event):
        ...
    @property
    def _stateID(self):
        ...

# base nao representavel no stub: ViewComponent[...]
class LoadoutPresenter:
    _VIEW_MODEL = AmmunitionPanelModel
    _STATES_OBSERVER = _LoadoutStatesObserver
    __itemsCache: Any
    __loadoutController: Any
    __platoonCtrl: Any
    _vehInteractingItem: Any
    __ammunitionGroupsController: Any
    __currentGroupId: Any
    __currentSectionName: Any
    __currentSlotIndex: Any
    __slotSelectionObserver: Any
    def __init__(self):
        ...
    def getSlotSelectionObserver(self):
        ...
    def createToolTip(self, event):
        ...
    # decorador original: @prbDispatcherProperty
    def prbDispatcher(self):
        ...
    def _getChildComponents(self):
        ...
    @property
    def _getGroupController(self):
        ...
    def _getEvents(self):
        ...
    def _getListeners(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _getBackportTooltipData(self, event):
        ...
    def __createVehicleCopy(self):
        ...
    def __createVehicleItem(self):
        ...
    def __updateModel(self, recreate=False, sectionName=None):
        ...
    def __canChangeVehicle(self):
        ...
    def __onAcceptComplete(self):
        ...
    def __onRevert(self, *args):
        ...
    def __onCacheResync(self, reason, diff):
        ...
    def __onItemUpdated(self, sectionName):
        ...
    def __getVehicle(self):
        ...
    def __onVehicleChanged(self):
        ...
    def __onDoLeaveAction(self, _):
        ...
    def __onKickedFromPrebattle(self, _):
        ...
    def __onPrebattleLeft(self):
        ...
    def __onMembersUpdate(self):
        ...
    def _recreateVehicleSetups(self):
        ...
    def _getEquipmentsPairs(self, groupID):
        ...
    def _createAmmunitionGroupsController(self, vehicle):
        ...
    def _updateAmmunitionGroupsController(self, recreate=False, sectionName=None):
        ...
    @staticmethod
    def __isAmmunitionPanelDisabled():
        ...
    def __setCurrentSection(self, selectedSection):
        ...
    def __isNewSetupLayoutIndexValid(self, hudGroupID, newLayoutIdx):
        ...
    # decorador original: @wg_async
    def __onChangeSetupIndex(self, args):
        ...
    # decorador original: @adisp.adisp_process
    def __doChangeSetupIndex(self, groupId, currentIndex):
        ...
    # decorador original: @adisp.adisp_process
    def __onSpecializationSelect(self, args=None):
        ...
    def __onPanelSlotSelect(self, groupId, sectionName, slotIndex):
        ...
