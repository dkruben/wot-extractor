# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/missions/regular/states.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks_common.state_machine.transitions import TransitionType as TransitionType
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.framework.entities.View import ViewKey as ViewKey
from gui.Scaleform.genConsts.QUESTS_ALIASES import QUESTS_ALIASES as QUESTS_ALIASES
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.lobby_state_machine.states import SubScopeSubLayerState as SubScopeSubLayerState, ViewLobbyState as ViewLobbyState, LobbyStateDescription as LobbyStateDescription
from gui.shared.event_dispatcher import showHangar as showHangar
from helpers import dependency as dependency
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from skeletons.gui.battle_matters import IBattleMattersController as IBattleMattersController

# decorador original: @SubScopeSubLayerState.parentOf
class MissionsState(ViewLobbyState):
    STATE_ID = 'missions'
    VIEW_KEY: Any
    __appLoader: Any
    __battleMattersController: Any
    def registerTransitions(self):
        ...
    def getNavigationDescription(self):
        ...
    def getBackNavigationDescription(self, params):
        ...
    def serializeParams(self):
        ...
    def _onEntered(self, event):
        ...

def registerStates(machine):
    ...
def registerTransitions(machine):
    ...
