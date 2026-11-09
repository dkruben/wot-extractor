# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/controllers/arena_load_ctrl.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from gui.battle_control import avatar_getter as avatar_getter
from gui.battle_control.arena_info.interfaces import IArenaVehiclesController as IArenaVehiclesController
from gui.battle_control.battle_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from gui.battle_control.view_components import ViewComponentsController as ViewComponentsController
from helpers import dependency as dependency, uniprof as uniprof
from skeletons.gameplay import IGameplayLogic as IGameplayLogic, PlayerEventID as PlayerEventID
from skeletons.gui.game_control import IGameSessionController as IGameSessionController

class IArenaLoadCtrlListener(object):
    def arenaLoadCompleted(self):
        ...

class ArenaLoadController(IArenaVehiclesController, ViewComponentsController):
    gameSession: Any
    gameplay: Any
    __arenaVisitor: Any
    __isCompleted: Any
    def __init__(self):
        ...
    def getControllerID(self):
        ...
    def startControl(self, battleCtx, arenaVisitor):
        ...
    def stopControl(self):
        ...
    def setViewComponents(self, *components):
        ...
    def spaceLoadStarted(self):
        ...
    def invalidateArenaInfo(self):
        ...
    def spaceLoadCompleted(self):
        ...
    def arenaLoadCompleted(self):
        ...
    def _clear(self):
        ...

class ArenaLoadPlayer(ArenaLoadController):
    def stopControl(self):
        ...

def createArenaLoadController(setup):
    ...
