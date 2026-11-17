# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/managers/battle_input.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import Keys as Keys
from AvatarInputHandler import aih_global_binding as aih_global_binding
from aih_constants import CTRL_MODE_NAME as CTRL_MODE_NAME
from gui.battle_control import avatar_getter as avatar_getter
from gui.battle_control import event_dispatcher as event_dispatcher
from helpers import dependency as dependency, isPlayerAvatar as isPlayerAvatar
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from skeletons.gui.game_control import ICommendationsController as ICommendationsController
from soft_exception import SoftException as SoftException
import CommandMapping as CommandMapping

class BattleGUIKeyHandler(object):
    def handleEscKey(self, isDown):
        ...

class BattleGameInputMgr(object):
    __slots__: tuple
    __ctrlModeName: Any
    guiSessionProvider: Any
    commendationsCtrl: Any
    __consumers: Any
    __keyHandlers: Any
    def __init__(self):
        ...
    def start(self):
        ...
    def stop(self):
        ...
    def enterGuiControlMode(self, consumerID, cursorVisible=True, enableAiming=True, stopVehicle=False):
        ...
    def leaveGuiControlMode(self, consumerID):
        ...
    def hasGuiControlModeConsumers(self, *consumersIDs):
        ...
    def registerGuiKeyHandler(self, handler):
        ...
    def unregisterGuiKeyHandler(self, handler):
        ...
    def handleKey(self, isDown, key, mods):
        ...
