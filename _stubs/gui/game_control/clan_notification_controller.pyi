# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_control/clan_notification_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from constants import ClansConfig as ClansConfig
from Event import Event as Event
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import CLAN_NOTIFICATION_COUNTERS as CLAN_NOTIFICATION_COUNTERS, CLAN_NEWS_SEEN as CLAN_NEWS_SEEN
from frameworks.wulf import WindowLayer as WindowLayer
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.daapi.view.lobby.clans.clan_helpers import getClanQuestURL as getClanQuestURL
from gui.Scaleform.daapi.view.lobby.clans.browser.web_handlers import createNotificationWebHandlers as createNotificationWebHandlers
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams as SFViewLoadParams
from gui.Scaleform.framework.managers.containers import POP_UP_CRITERIA as POP_UP_CRITERIA
from gui.shared import g_eventBus as g_eventBus, events as events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.utils.MethodsRules import MethodsRules as MethodsRules
from helpers import dependency as dependency
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from skeletons.gui.game_control import IClanNotificationController as IClanNotificationController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.game_window_controller import GameWindowController as GameWindowController
from skeletons.gui.web import IWebController as IWebController
_logger: Any

class ClanNotificationController(GameWindowController, IClanNotificationController, MethodsRules):
    __lobbyContext: Any
    __appLoader: Any
    __clansCtrl: Any
    CLAN_NEWS_ALIAS = 'clanNews'
    DEPRECATED_ALIASES: tuple
    __enabled: Any
    onClanNotificationUpdated: Any
    def __init__(self):
        ...
    @property
    def newsCounter(self):
        ...
    def getCounters(self, aliases=None):
        ...
    # decorador original: @MethodsRules.delayable(...)
    def setCounters(self, alias, count, isIncrement=False):
        ...
    def resetCounters(self):
        ...
    # decorador original: @MethodsRules.delayable(...)
    def onLobbyInited(self, event):
        ...
    def onAvatarBecomePlayer(self):
        ...
    def showWindow(self, url=None, invokedFrom=None):
        ...
    def hideWindow(self):
        ...
    def _getUrl(self):
        ...
    def _openWindow(self, url, _=None):
        ...
    def __getBrowserView(self):
        ...
    def __addListeners(self):
        ...
    def __removeListeners(self):
        ...
    def __onServerSettingsChange(self, diff):
        ...
    def __processClanNewsNotification(self):
        ...
