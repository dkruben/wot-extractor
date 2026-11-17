# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client_common/Login.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import BigWorld as BigWorld
from PlayerEvents import g_playerEvents as g_playerEvents
from debug_utils import LOG_DEBUG as LOG_DEBUG
Login = PlayerLogin

class PlayerLogin(BigWorld.Entity):
    def __init__(self):
        ...
    def onBecomePlayer(self):
        ...
    def onBecomeNonPlayer(self):
        ...
    def onKickedFromServer(self, checkoutPeripheryID):
        ...
    def receiveLoginQueueNumber(self, queueNumber):
        ...
    def handleKeyEvent(self, event):
        ...
    def setPeripheryRoutingGroup(self, peripheryRoutingGroup, availableHosts):
        ...
