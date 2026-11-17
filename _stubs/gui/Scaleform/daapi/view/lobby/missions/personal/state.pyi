# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/missions/personal/state.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.framework.entities.View import ViewKey as ViewKey
from gui.Scaleform.genConsts.PERSONAL_MISSIONS_ALIASES import PERSONAL_MISSIONS_ALIASES as PERSONAL_MISSIONS_ALIASES
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.lobby_state_machine.states import SubScopeSubLayerState as SubScopeSubLayerState, ViewLobbyState as ViewLobbyState

# decorador original: @SubScopeSubLayerState.parentOf
class PersonalMissionsAwardsState(ViewLobbyState):
    STATE_ID = PERSONAL_MISSIONS_ALIASES.PERSONAL_MISSIONS_AWARDS_VIEW_ALIAS
    VIEW_KEY: Any
    def registerTransitions(self):
        ...
    def getBackNavigationDescription(self, params):
        ...

# decorador original: @SubScopeSubLayerState.parentOf
class PersonalMissionsPageState(ViewLobbyState):
    STATE_ID = PERSONAL_MISSIONS_ALIASES.PERSONAL_MISSIONS_PAGE_ALIAS
    VIEW_KEY: Any
    @classmethod
    def goTo(cls, operationID=None, branch=None, chainID=None, missionID=None):
        ...
    def registerTransitions(self):
        ...
    def _getViewLoadCtx(self, event):
        ...
    def getBackNavigationDescription(self, params):
        ...

def registerStates(machine):
    ...
def registerTransitions(machine):
    ...
