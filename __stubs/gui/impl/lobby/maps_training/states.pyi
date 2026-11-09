# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/maps_training/states.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import WWISE as WWISE
from WeakMethod import WeakMethodProxy as WeakMethodProxy
from frameworks_common.state_machine import StateFlags as StateFlags
from frameworks_common.state_machine.transitions import TransitionType as TransitionType
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.daapi.view.lobby.battle_queue.states import BattleQueueContainerState as BattleQueueContainerState
from gui.Scaleform.framework import ScopeTemplates as ScopeTemplates
from gui.Scaleform.framework.entities.View import ViewKey as ViewKey
from gui.battle_results.service import PostBattleResultsStateMixin as PostBattleResultsStateMixin
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.lobby.maps_training.maps_training_queue_view import MapsTrainingQueueView as MapsTrainingQueueView
from gui.impl.lobby.maps_training.maps_training_view import MapsTrainingView as MapsTrainingView
from gui.impl.lobby.maps_training.sound_constants import MapsTrainingSound as MapsTrainingSound
from gui.lobby_state_machine.states import GuiImplViewLobbyState as GuiImplViewLobbyState, SubScopeSubLayerState as SubScopeSubLayerState, LobbyStateFlags as LobbyStateFlags, LobbyState as LobbyState, LobbyStateDescription as LobbyStateDescription, TopScopeTopLayerState as TopScopeTopLayerState, ViewLobbyState as ViewLobbyState
from gui.lobby_state_machine.transitions import HijackTransition as HijackTransition
from helpers import dependency as dependency
from helpers.time_utils import getCurrentTimestamp as getCurrentTimestamp
from skeletons.gui.game_control import IMapsTrainingController as IMapsTrainingController

# decorador original: @SubScopeSubLayerState.parentOf
class MapsTrainingState(GuiImplViewLobbyState):
    STATE_ID = 'mapsTraining'
    VIEW_KEY: Any
    __mapsTrainingCtrl: Any
    def __init__(self, flags=...):
        ...
    def getNavigationDescription(self):
        ...
    def registerStates(self):
        ...
    def registerTransitions(self):
        ...
    def _onEntered(self, event):
        ...
    def _onExited(self):
        ...
    def __shouldHijack(self, _):
        ...

# decorador original: @MapsTrainingState.parentOf
class EntryState(LobbyState):
    STATE_ID = 'entry'

# decorador original: @MapsTrainingState.parentOf
class SelectedState(LobbyState):
    STATE_ID = 'selected'
    __mapsTrainingCtrl: Any
    def serializeParams(self):
        ...
    def _onEntered(self, event):
        ...
    def _onExited(self):
        ...

# decorador original: @BattleQueueContainerState.parentOf
class MapsTrainingQueueState(GuiImplViewLobbyState):
    STATE_ID = 'mapsTrainingQueue'
    VIEW_KEY: Any
    __createTime: Any
    def __init__(self, flags=...):
        ...
    def getNavigationDescription(self):
        ...
    def serializeParams(self):
        ...
    def _getViewLoadCtx(self, event):
        ...
    def _onEntered(self, event):
        ...
    def _onExited(self):
        ...

# decorador original: @TopScopeTopLayerState.parentOf
class MapsTrainingBattleResultsState(ViewLobbyState, PostBattleResultsStateMixin):
    STATE_ID = VIEW_ALIAS.MAPS_TRAINING_BATTLE_RESULTS
    VIEW_KEY: Any
    def registerTransitions(self):
        ...

def registerStates(machine):
    ...
def registerTransitions(machine):
    ...
