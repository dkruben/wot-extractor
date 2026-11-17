# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/SystemMessagesInterface.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import time as time
import account_helpers as account_helpers
from MemoryCriticalController import g_critMemHandler as g_critMemHandler
from PlayerEvents import g_playerEvents as g_playerEvents
from debug_utils import LOG_DEBUG as LOG_DEBUG, LOG_ERROR as LOG_ERROR
from gui import GUI_SETTINGS as GUI_SETTINGS
from gui.SystemMessages import SM_TYPE as SM_TYPE
from gui.Scaleform.daapi.view.dialogs.SystemMessageMeta import SESSION_CONTROL_TYPE as SESSION_CONTROL_TYPE, SessionControlAuxData as SessionControlAuxData
from helpers import i18n as i18n, dependency as dependency
from messenger.m_constants import PROTO_TYPE as PROTO_TYPE
from messenger.m_constants import SCH_CLIENT_MSG_TYPE as SCH_CLIENT_MSG_TYPE
from messenger.proto import proto_getter as proto_getter
from skeletons.connection_mgr import IConnectionManager as IConnectionManager
from skeletons.gui.game_control import IEventsNotificationsController as IEventsNotificationsController, IAOGASController as IAOGASController, IGameSessionController as IGameSessionController
from skeletons.gui.shared import IItemsCache as IItemsCache
from skeletons.gui.system_messages import ISystemMessages as ISystemMessages
from helpers import getClientLanguage as getClientLanguage
KOREA_TIME_TILL_MIDNIGHT = 7200

class SystemMessagesInterface(ISystemMessages):
    __CMD_BLOCK_PREFIX = 'cmd_'
    __PROMO_BLOCK_PREFIX = 'promo_'
    itemsCache: Any
    aogas: Any
    gameSession: Any
    eventsNotification: Any
    connectionMgr: Any
    __expirationShown: Any
    def init(self):
        ...
    def destroy(self):
        ...
    # decorador original: @proto_getter(...)
    def proto(self):
        ...
    def pushMessage(self, text, type, priority=None, messageData=None, savedData=None):
        ...
    def pushI18nMessage(self, key, *args, **kwargs):
        ...
    def __onAccountShowGUI(self, ctx):
        ...
    def __onAvatarBecomePlayer(self):
        ...
    def __clearLobbyListeners(self):
        ...
    def __onConnected(self):
        ...
    def __checkPremiumAccountExpiry(self, ctx=None):
        ...
    def __onMemoryCritical(self, message):
        ...
    def __AOGAS_onNotifyAccount(self, message):
        ...
    def __gameSession_onClientNotify(self, sessionDuration, timeTillMidnight, playTimeLeft):
        ...
    def __onReceiveEventNotification(self, added, removed):
        ...
    def __processNotifications(self, notifications, state):
        ...
