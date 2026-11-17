# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gameplay/delegator.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from frameworks_common.state_machine import StringEvent as StringEvent
from frameworks_common.state_machine import StateMachine as StateMachine
from frameworks_common.state_machine import BaseStateObserver as BaseStateObserver
from frameworks_common.state_machine import OneshotStateIdsObserver as OneshotStateIdsObserver
from gameplay import listeners as listeners
from gameplay.blockers import BlockingStateMixin as BlockingStateMixin
from helpers import dependency as dependency
from skeletons.connection_mgr import IConnectionManager as IConnectionManager, DisconnectReason as DisconnectReason
from skeletons.gui.login_manager import ILoginManager as ILoginManager
from skeletons.gameplay import IGameplayLogic as IGameplayLogic, PlayerEventID as PlayerEventID

class GameplayLogic(IGameplayLogic):
    __slots__: tuple
    connectionMgr: Any
    loginMgr: Any
    __machine: Any
    __adaptor: Any
    def __init__(self, machine):
        ...
    def start(self):
        ...
    def stop(self):
        ...
    def addStateObserver(self, observer):
        ...
    def addOneshotObserver(self, gameplayStateIDs, observerLifetimeObj, enterFn=None, exitFn=None):
        ...
    def removeStateObserver(self, observer):
        ...
    def postStateEvent(self, eventID, **kwargs):
        ...
    def tick(self):
        ...
    def addStateEnterBlocker(self, stateID, event):
        ...
    def addStateExitBlocker(self, stateID, event):
        ...
    def goToLoginByRQ(self):
        ...
    def goToLoginByDisconnectRQ(self):
        ...
    def goToLoginByEvent(self):
        ...
    def goToLoginByKick(self, reason, kickReasonType, expiryTime):
        ...
    def goToLoginByError(self, reason):
        ...
    @staticmethod
    def quitFromGame():
        ...
