# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/controllers/game_messages_ctrl.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import weakref as weakref
from collections import namedtuple as namedtuple
from PlayerEvents import g_playerEvents as g_playerEvents
from gui.battle_control.battle_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from gui.battle_control.view_components import IViewComponentsController as IViewComponentsController
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider

# base nao representavel no stub: namedtuple(...)
class PlayerMessageData:
    def getDict(self):
        ...

class GameMessagesController(IViewComponentsController):
    sessionProvider: Any
    __arenaVisitor: Any
    __ui: Any
    def __init__(self, setup):
        ...
    def getControllerID(self):
        ...
    def startControl(self):
        ...
    def setViewComponents(self, component):
        ...
    def clearViewComponents(self):
        ...
    def stopControl(self):
        ...
    def __onRoundFinished(self, winningTeam, reason):
        ...

def createGameMessagesController(setup):
    ...
