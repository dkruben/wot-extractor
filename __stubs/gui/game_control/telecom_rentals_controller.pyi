# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_control/telecom_rentals_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from gui import SystemMessages as SystemMessages
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.server_events import settings as settings
from helpers import dependency as dependency
from skeletons.gui.game_control import ITelecomRentalsNotificationController as ITelecomRentalsNotificationController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.system_messages import ISystemMessages as ISystemMessages
from telecom_rentals_common import TELECOM_RENTALS_CONFIG as TELECOM_RENTALS_CONFIG, PARTNERSHIP_BLOCKED_TOKEN_NAME as PARTNERSHIP_BLOCKED_TOKEN_NAME

class TelecomRentalsNotificationController(ITelecomRentalsNotificationController):
    _lobbyContext: Any
    def __init__(self):
        ...
    def onLobbyStarted(self, ctx):
        ...
    def onAccountBecomeNonPlayer(self):
        ...
    def onDisconnected(self):
        ...
    def processSwitchNotifications(self):
        ...
    def _showNotification(self, msgType, title, body):
        ...
    def _onServerSettingsChange(self, diff):
        ...
    def __onTokensUpdate(self, diff):
        ...
