# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/common/hangar_marker_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from Event import Event as Event
from frameworks.wulf import WindowLayer as WindowLayer, WindowStatus as WindowStatus
from frameworks_common.state_machine import BaseStateObserver as BaseStateObserver
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.framework.entities.sf_window import SFWindow as SFWindow
from gui.Scaleform.genConsts.PREBATTLE_ALIASES import PREBATTLE_ALIASES as PREBATTLE_ALIASES
from gui.Scaleform.lobby_entry import getLobbyStateMachine as getLobbyStateMachine
from gui.impl.pub import ViewImpl as ViewImpl
from gui.lobby_state_machine.states import LobbyStateFlags as LobbyStateFlags
from gui.prb_control.dispatcher import g_prbLoader as g_prbLoader
from gui.prb_control.entities.maps_training.pre_queue.entity import MapsTrainingEntity as MapsTrainingEntity
from helpers import dependency as dependency
from skeletons.gui.impl import IGuiLoader as IGuiLoader

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

class HangarMarkerView(ViewImpl):
    __guiLoader: Any
    __LAYERS_WITHOUT_MARKERS: set
    __ALIASES_WITHOUT_MARKERS: set
    __ACTIVE_WINDOW_STATUSES: tuple
    __UPDATING_WINDOW_STATUSES: tuple
    _statesObserver: Any
    def __init__(self, settings):
        ...
    @property
    def viewModel(self):
        ...
    def _createStatesObserver(self):
        ...
    def _getEvents(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _canShowMarkers(self):
        ...
    def _setMarkerVisible(self, isVisible):
        ...
    def _updateMarker(self, *args, **kwargs):
        ...
    def _updateMarkerVisibility(self, *args, **kwargs):
        ...
    def __onWindowStatusChanged(self, uniqueID, newStatus):
        ...
