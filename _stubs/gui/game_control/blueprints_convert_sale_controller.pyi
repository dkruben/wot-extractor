# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_control/blueprints_convert_sale_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import Enum as Enum
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import BLUEPRINTS_CONVERT_SALE_STARTED_SEEN as BLUEPRINTS_CONVERT_SALE_STARTED_SEEN
from helpers import dependency as dependency, isPlayerAccount as isPlayerAccount
from messenger.m_constants import SCH_CLIENT_MSG_TYPE as SCH_CLIENT_MSG_TYPE
from skeletons.gui.game_control import IBlueprintsConvertSaleController as IBlueprintsConvertSaleController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.server_events import IEventsCache as IEventsCache
from skeletons.gui.system_messages import ISystemMessages as ISystemMessages
_ACTION_POSTFIX = '_BCS'

class BCSActionState(Enum):
    STARTED = 'begin'
    PAUSED = 'pause'
    RESTORE = 'restore'
    END = 'end'

class BlueprintsConvertSaleController(IBlueprintsConvertSaleController):
    __slots__: tuple
    _lobbyContext: Any
    _systemMessages: Any
    _eventsCache: Any
    _isEnabled: Any
    _isStarted: Any
    def __init__(self):
        ...
    def onLobbyStarted(self, ctx):
        ...
    def fini(self):
        ...
    def onDisconnected(self):
        ...
    def onAvatarBecomePlayer(self):
        ...
    def __stop(self):
        ...
    def __onSettingsChanged(self, diff):
        ...
    def __onEventsCacheSyncCompleted(self, *_):
        ...
    def __updateActionState(self):
        ...
    def __showNotification(self, state):
        ...
