# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/controllers/battle_notifier_ctrl.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from PlayerEvents import g_playerEvents as g_playerEvents
from gui.battle_control.battle_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from gui.battle_control.view_components import ViewComponentsController as ViewComponentsController
from helpers import dependency as dependency
from messenger.proto.events import g_messengerEvents as g_messengerEvents
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
_logger: Any

class IBattleNotifierListener(object):
    def resultsNotificationReceived(self, results):
        ...

class BattleNotifierController(ViewComponentsController):
    __slots__: tuple
    sessionProvider: Any
    __enabled: Any
    def __init__(self, setup):
        ...
    def getControllerID(self):
        ...
    def startControl(self):
        ...
    def stopControl(self):
        ...
    def __onRoundFinished(self, winningTeam, reason):
        ...
    def __onChatMessage(self, clientID, message):
        ...

def createBattleNotifierController(setup):
    ...
