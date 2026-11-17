# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_control/hangar_loading_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import Event as Event
from helpers import dependency as dependency
from skeletons.gui.game_control import IHangarLoadingController as IHangarLoadingController
from skeletons.gui.goodies import IGoodiesCache as IGoodiesCache
from skeletons.gui.shared import IItemsCache as IItemsCache
from skeletons.gui.shared.utils import IHangarSpace as IHangarSpace

class HangarLoadingController(IHangarLoadingController):
    __hangarSpace: Any
    __itemsCache: Any
    __goodiesCache: Any
    onHangarLoadedAfterLogin: Any
    __isConnectedAsAccount: Any
    def __init__(self):
        ...
    def fini(self):
        ...
    def onAvatarBecomePlayer(self):
        ...
    def onConnected(self):
        ...
    def onAccountBecomeNonPlayer(self):
        ...
    def onDisconnected(self):
        ...
    def onLobbyInited(self, event):
        ...
    def __hangarLoadedAfterLoginNotify(self):
        ...
    def isHangarLoadedAfterLogin(self):
        ...
