# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/trainings/states.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from gui.Scaleform.framework.entities.View import ViewKey as ViewKey
from gui.Scaleform.genConsts.PREBATTLE_ALIASES import PREBATTLE_ALIASES as PREBATTLE_ALIASES
from gui.impl import backport as backport
from gui.impl.gen.resources import R as R
from gui.lobby_state_machine.states import SubScopeSubLayerState as SubScopeSubLayerState, SFViewLobbyState as SFViewLobbyState, LobbyStateDescription as LobbyStateDescription
from gui.prb_control import prbEntityProperty as prbEntityProperty
from gui.prb_control.entities.base.legacy.ctx import SetPlayerStateCtx as SetPlayerStateCtx
from gui.prb_control.entities.training.legacy.entity import TrainingEntity as TrainingEntity

# decorador original: @SubScopeSubLayerState.parentOf
class TrainingListState(SFViewLobbyState):
    STATE_ID = PREBATTLE_ALIASES.TRAINING_LIST_VIEW_PY
    VIEW_KEY: Any
    def getNavigationDescription(self):
        ...

# decorador original: @SubScopeSubLayerState.parentOf
class TrainingRoomState(SFViewLobbyState):
    STATE_ID = PREBATTLE_ALIASES.TRAINING_ROOM_VIEW_PY
    VIEW_KEY: Any
    # decorador original: @prbEntityProperty
    def prbEntity(self):
        ...
    def _onEntered(self, event):
        ...
    def _onExited(self):
        ...
    def getNavigationDescription(self):
        ...

def registerStates(machine):
    ...
def registerTransitions(machine):
    ...
