# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/manual/states.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from frameworks_common.state_machine import StateFlags as StateFlags
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.framework.entities.View import ViewKey as ViewKey
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.lobby_state_machine.states import ViewLobbyState as ViewLobbyState, SubScopeTopLayerState as SubScopeTopLayerState, LobbyStateDescription as LobbyStateDescription
from gui.Scaleform.daapi.view.lobby.manual.manual_chapter_view import ManualChapterView as ManualChapterView

# decorador original: @SubScopeTopLayerState.parentOf
class ManualState(ViewLobbyState):
    STATE_ID = VIEW_ALIAS.WIKI_VIEW
    VIEW_KEY: Any
    @classmethod
    def goTo(cls, chapterIndex=None, pageIndex=None):
        ...
    def compareParams(self, params, otherParams):
        ...
    def registerTransitions(self):
        ...
    def getNavigationDescription(self):
        ...
    def _getViewLoadCtx(self, event):
        ...

# decorador original: @SubScopeTopLayerState.parentOf
class ManualChapterState(ViewLobbyState):
    STATE_ID = VIEW_ALIAS.MANUAL_CHAPTER_VIEW
    VIEW_KEY: Any
    __cachedParams: Any
    def __init__(self, flags=...):
        ...
    @classmethod
    def goTo(cls, chapterIndex, pageIndex=None):
        ...
    def registerTransitions(self):
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

def registerStates(machine):
    ...
def registerTransitions(machine):
    ...
