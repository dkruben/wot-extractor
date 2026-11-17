# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_control/account_completion.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
import constants as constants
from PlayerEvents import g_playerEvents as g_playerEvents
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import SHOW_DEMO_ACC_REGISTRATION as SHOW_DEMO_ACC_REGISTRATION
from account_helpers.settings_core.ServerSettingsManager import UI_STORAGE_KEYS as UI_STORAGE_KEYS
from gui.platform.base.settings import CONTENT_WAITING as CONTENT_WAITING
from gui.platform.base.statuses.constants import StatusTypes as StatusTypes
from gui.platform.wgnp.steam_account.statuses import SteamAccEmailStatus as SteamAccEmailStatus
from gui.shared.event_dispatcher import showSteamAddEmailOverlay as showSteamAddEmailOverlay, showSteamConfirmEmailOverlay as showSteamConfirmEmailOverlay
from gui.shared.lock_overlays import lockNotificationManager as lockNotificationManager
from helpers import dependency as dependency
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.connection_mgr import IConnectionManager as IConnectionManager
from skeletons.gui.game_control import IOverlayController as IOverlayController, ISteamCompletionController as ISteamCompletionController, IDemoAccCompletionController as IDemoAccCompletionController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.login_manager import ILoginManager as ILoginManager
from skeletons.gui.platform.wgnp_controllers import IWGNPSteamAccRequestController as IWGNPSteamAccRequestController
from skeletons.gui.shared import IItemsCache as IItemsCache
from skeletons.gui.shared.utils import IHangarSpace as IHangarSpace
from wg_async import wg_async as wg_async, wg_await as wg_await

class SteamCompletionController(ISteamCompletionController):
    _loginManager: Any
    _hangarSpace: Any
    _wgnpSteamAccCtrl: Any
    _overlayController: Any
    _lobbyContext: Any
    _itemsCache: Any
    __settingsCore: Any
    __connectionManager: Any
    __isLobbyInited: Any
    def __init__(self):
        ...
    @property
    def isSteamAccount(self):
        ...
    @property
    def isLockNotificationManagerNeeded(self):
        ...
    @property
    def isAddEmailOverlayShown(self):
        ...
    @property
    def isConfirmEmailOverlayAllowed(self):
        ...
    def onLobbyStarted(self, ctx):
        ...
    def onLobbyInited(self, event):
        ...
    def onAvatarBecomePlayer(self):
        ...
    def onDisconnected(self):
        ...
    def __subscribe(self):
        ...
    def __unsubscribe(self):
        ...
    def __clear(self):
        ...
    # decorador original: @wg_async
    def __onSpaceCreate(self):
        ...
    def __canSteamShadeShow(self):
        ...
    def setAddEmailOverlayShown(self):
        ...
    def setConfirmEmailOverlayAllowed(self, isAllowed):
        ...

class DemoAccCompletionController(IDemoAccCompletionController):
    _isDemoAccount: Any
    _isDemoAccountOnce: Any
    _controllerDestroyed: Any
    def __init__(self):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def onDisconnected(self):
        ...
    @property
    def isDemoAccount(self):
        ...
    @property
    def isDemoAccountOnce(self):
        ...
    @property
    def isInDemoAccRegistration(self):
        ...
    @isInDemoAccRegistration.setter
    def isInDemoAccRegistration(self, value):
        ...
    def _onClientUpdate(self, diff, _):
        ...
