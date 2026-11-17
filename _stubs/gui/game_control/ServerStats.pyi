# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_control/ServerStats.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
import Event as Event
import constants as constants
from PlayerEvents import g_playerEvents as g_playerEvents
from gui.Scaleform.locale.MENU import MENU as MENU
from gui.impl import backport as backport
from gui.shared.formatters import text_styles as text_styles
from skeletons.gui.game_control import IServerStatsController as IServerStatsController
_STATS_REQUEST_TIMEOUT = 5.0

class STATS_TYPE(object):
    UNAVAILABLE = 'unavailable'
    CLUSTER = 'clusterCCU'
    FULL = 'regionCCU/clusterCCU'

class ServerStats(IServerStatsController):
    __statsCallbackID: Any
    __stats: Any
    onStatsReceived: Any
    def __init__(self):
        ...
    def onLobbyStarted(self, ctx):
        ...
    def onAvatarBecomePlayer(self):
        ...
    def onDisconnected(self):
        ...
    def getFormattedStats(self):
        ...
    def getStats(self):
        ...
    def __stop(self):
        ...
    def __onStatsReceived(self, stats):
        ...
    def __requestServerStats(self):
        ...
    def __loadStatsCallback(self, timeout=None):
        ...
    def __clearStatsCallback(self):
        ...
