# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/collection/states.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from typing import Optional as Optional
from frameworks.wulf import ViewStatus as ViewStatus
from gui.shared.event_dispatcher import showHangar as showHangar
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.framework.entities.View import ViewKey as ViewKey
from gui.lobby_state_machine.states import StateFlags as StateFlags, SFViewLobbyState as SFViewLobbyState, SubScopeSubLayerState as SubScopeSubLayerState
from helpers import dependency as dependency
from skeletons.gui.game_control import ICollectionsSystemController as ICollectionsSystemController

# decorador original: @SubScopeSubLayerState.parentOf
class CollectionState(SFViewLobbyState):
    STATE_ID = VIEW_ALIAS.COLLECTIONS_PAGE
    VIEW_KEY: Any
    __collectionsSystem: Any
    __cachedParams: Any
    def __init__(self, flags=...):
        ...
    @classmethod
    def goTo(cls, collectionId, page):
        ...
    def registerTransitions(self):
        ...
    def serializeParams(self):
        ...
    def _onEntered(self, event):
        ...

def registerStates(machine):
    ...
def registerTransitions(machine):
    ...
