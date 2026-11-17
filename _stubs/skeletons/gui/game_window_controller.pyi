# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/skeletons/gui/game_window_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from adisp import adisp_process as adisp_process, adisp_async as adisp_async
from gui.game_control.links import URLMacros as URLMacros
from helpers import dependency as dependency
from skeletons.gui.game_control import IGameWindowController as IGameWindowController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.server_events import IEventsCache as IEventsCache

class GameWindowController(IGameWindowController):
    eventsCache: Any
    lobbyContext: Any
    _isLobbyInited: Any
    __urlMacros: Any
    def __init__(self):
        ...
    def fini(self):
        ...
    def onLobbyInited(self, event):
        ...
    def onAvatarBecomePlayer(self):
        ...
    def onDisconnected(self):
        ...
    def hideWindow(self):
        ...
    def showWindow(self, url=None, invokedFrom=None):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def getUrl(self, callback=...):
        ...
    def _addListeners(self):
        ...
    def _removeListeners(self):
        ...
    def _onSyncCompleted(self, *_):
        ...
    # decorador original: @adisp_process
    def _showWindow(self, url, invokedFrom=None):
        ...
    def _openWindow(self, url, invokedFrom=None):
        ...
