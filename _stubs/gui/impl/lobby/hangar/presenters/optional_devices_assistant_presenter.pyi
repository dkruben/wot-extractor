# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/hangar/presenters/optional_devices_assistant_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
import Event as Event
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from PlayerEvents import g_playerEvents as g_playerEvents
from constants import QUEUE_TYPE as QUEUE_TYPE
from frameworks_common.state_machine import BaseStateObserver as BaseStateObserver, visitor as visitor
from gui.Scaleform.lobby_entry import getLobbyStateMachine as getLobbyStateMachine
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.optional_devices_assistant_model import OptionalDevicesAssistantModel as OptionalDevicesAssistantModel
from gui.impl.lobby.tank_setup.optional_devices_assistant.hangar import OptionalDevicesAssistantView as OptionalDevicesAssistantView
from gui.impl.lobby.tanksetup.tooltips.popular_loadouts_tooltip import PopularLoadoutsTooltip as PopularLoadoutsTooltip
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener
from helpers import dependency as dependency
from renewable_subscription_common.schema import renewableSubscriptionsConfigSchema as renewableSubscriptionsConfigSchema
from skeletons.gui.game_control import IWotPlusController as IWotPlusController
from gui.lobby_state_machine.lobby_state_machine import LobbyStateMachine as LobbyStateMachine
from frameworks_common.state_machine import State as State, StateEvent as StateEvent
from typing import Optional as Optional
_logger: Any

class _OptionalDevicesObserver(BaseStateObserver):
    __manager: Any
    onEquipEntered: Any
    onEquipExited: Any
    def __init__(self):
        ...
    def clear(self):
        ...
    def isObservingState(self, state):
        ...
    def onEnterState(self, state, event):
        ...
    def onExitState(self, state, event):
        ...

# base nao representavel no stub: ViewComponent[...]
class OptionalDevicesAssistantPresenter(IGlobalListener):
    _STATES_OBSERVER = _OptionalDevicesObserver
    _wotPlusController: Any
    _optionalDevicesAssistant: Any
    optionalDevicesAssistantObserver: Any
    __slotSelectionObserver: Any
    def __init__(self):
        ...
    def prepare(self):
        ...
    @property
    def viewModel(self):
        ...
    def _getEvents(self):
        ...
    def _finalize(self):
        ...
    def _createOptionalDevicesAssistantPanel(self):
        ...
    def _removeOptionalDevicesAssistantPanel(self):
        ...
    def __onVehicleChanged(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def __validateWotPlusOptDeviseAssistance(self, userHasSubscription):
        ...
    def __onConfigModelUpdated(self, gpKey):
        ...
    def __onEquipEntered(self):
        ...
