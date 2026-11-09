# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/pet_system/pet_house_marker_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from Event import Event as Event
from frameworks_common.state_machine import BaseStateObserver as BaseStateObserver
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings, WindowLayer as WindowLayer, WindowStatus as WindowStatus
from gui.Scaleform.lobby_entry import getLobbyStateMachine as getLobbyStateMachine
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.pet_system.pet_house_marker_model import PetHouseMarkerModel as PetHouseMarkerModel
from gui.impl.pub import ViewImpl as ViewImpl
from gui.lobby_state_machine.states import LobbyStateFlags as LobbyStateFlags
from gui.pet_system.pet_item_helper import PetItem as PetItem
from gui.pet_system.pet_ui_settings import PetUISettings as PetUISettings
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared import events as events_constants
from helpers import dependency as dependency
from pet_system_common import pet_constants as pet_constants
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.pet_system import IPetSystemController as IPetSystemController
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.impl import IGuiLoader as IGuiLoader
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.prb_control.dispatcher import g_prbLoader as g_prbLoader
from gui.Scaleform.genConsts.PREBATTLE_ALIASES import PREBATTLE_ALIASES as PREBATTLE_ALIASES
from gui.prb_control.entities.maps_training.pre_queue.entity import MapsTrainingEntity as MapsTrainingEntity
from gui.Scaleform.framework.entities.sf_window import SFWindow as SFWindow

class HangarMarkerStatesObserver(BaseStateObserver):
    _state: Any
    onMarkerState: Any
    def __init__(self):
        ...
    def isObservingState(self, state):
        ...
    def onEnterState(self, state, event):
        ...
    def onExitState(self, state, event):
        ...
    @property
    def currentState(self):
        ...

class PetHangarMarkerView(ViewImpl):
    __guiLoader: Any
    _settingsCore: Any
    __LAYERS_WITHOUT_MARKERS: set
    __ALIASES_WITHOUT_MARKERS: set
    __ACTIVE_WINDOW_STATUSES: tuple
    _statesObserver: Any
    def __init__(self, settings):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _setMarkerVisible(self, value):
        ...
    def _canShowMarkers(self):
        ...
    def _updateMarkerVisibility(self, *args, **kwargs):
        ...
    def __onWindowStatusChanged(self, uniqueID, newStatus):
        ...

class PetHouseMarkerView(PetHangarMarkerView):
    __petController: Any
    __lobbyContext: Any
    def __init__(self, *args, **kwargs):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _getEvents(self):
        ...
    def _getListeners(self):
        ...
    @property
    def viewModel(self):
        ...
    def _setMarkerVisible(self, isVisible):
        ...
    def __update(self, *_):
        ...
    def __onServerSettingsChanged(self, diff):
        ...
