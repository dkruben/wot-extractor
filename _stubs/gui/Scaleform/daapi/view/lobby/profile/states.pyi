# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/profile/states.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.framework.entities.View import ViewKey as ViewKey
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.lobby_state_machine.states import SFViewLobbyState as SFViewLobbyState, SubScopeSubLayerState as SubScopeSubLayerState, LobbyStateDescription as LobbyStateDescription
from helpers import dependency as dependency
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from gui.Scaleform.daapi.view.lobby.profile.ProfilePage import ProfilePage as ProfilePage

# decorador original: @SubScopeSubLayerState.parentOf
class ServiceRecordState(SFViewLobbyState):
    STATE_ID = VIEW_ALIAS.LOBBY_PROFILE
    VIEW_KEY: Any
    __appLoader: Any
    def registerTransitions(self):
        ...
    def serializeParams(self):
        ...
    def getNavigationDescription(self):
        ...

def registerStates(machine):
    ...
def registerTransitions(machine):
    ...
