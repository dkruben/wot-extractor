# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_control/screencast_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from gui.battle_control.arena_info.interfaces import IArenaVehiclesController as IArenaVehiclesController
from gui.shared.utils import getPlayerDatabaseID as getPlayerDatabaseID
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from skeletons.gui.game_control import IScreenCastController as IScreenCastController

class ScreenCastController(IScreenCastController, IArenaVehiclesController):
    __slots__: tuple
    sessionProvider: Any
    _isSet: Any
    _isBattleCtrlInit: Any
    _dbID: Any
    def __init__(self):
        ...
    def fini(self):
        ...
    def onAvatarBecomePlayer(self):
        ...
    def onAccountBecomePlayer(self):
        ...
    def invalidateArenaInfo(self):
        ...
    def invalidateVehiclesInfo(self, _):
        ...
    def onLobbyInited(self, event):
        ...
    def onDisconnected(self):
        ...
    def __checkDbID(self):
        ...
    def __update(self):
        ...
