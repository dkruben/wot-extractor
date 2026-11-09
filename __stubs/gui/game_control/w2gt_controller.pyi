# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_control/w2gt_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
import logging as logging
from collections import namedtuple as namedtuple
import typing as typing
from BWUtil import AsyncReturn as AsyncReturn
import ArenaType as ArenaType
import BigWorld as BigWorld
from account_helpers.settings_core.ServerSettingsManager import SETTINGS_SECTIONS as SETTINGS_SECTIONS
from account_helpers.settings_core.settings_constants import GAME as GAME, GuiSettingsBehavior as GuiSettingsBehavior
from adisp import adisp_process as adisp_process
from client_request_lib.exceptions import ResponseCodes as ResponseCodes
from constants import Configs as Configs
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.wgcg.requests import WgcgRequestResponse as WgcgRequestResponse
from gui.wgcg.w2gt.contexts import W2gtCtx as W2gtCtx
from helpers import dependency as dependency, server_settings as server_settings, getClientVersion as getClientVersion, time_utils as time_utils
from helpers.caches.w2gt_cache import W2gtCache as W2gtCache
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.game_control import IW2GTGameController as IW2GTGameController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache
from skeletons.gui.web import IWebController as IWebController
from wg_async import wg_async as wg_async, await_callback as await_callback
from helpers.server_settings import _W2GTConfig as _W2GTConfig
from gui.battle_control.controllers.w2gt.w2gt_data_mgr import W2gtProgress as W2gtProgress
from typing import Optional as Optional, Callable as Callable, Any as Any, Dict as Dict
_logger: _Any
_VALIDATE_RESPONSE_FIELDS: tuple
_ETAG_FIELD = 'etag'
_UPDATED_TIME_FIELD = 'Updated'
_NOT_MODIFIED_CODE = 304
_NEW_ACCOUNT_SESSIONS_COUNT = 2
_W2gtResponseData: _Any

class W2GTGameController(IW2GTGameController):
    __itemsCache: _Any
    __settingsCore: _Any
    __lobbyContext: _Any
    __webCtrl: _Any
    __w2gtConfig: _Any
    __isEnabledByPlayer: _Any
    __clientVersion: _Any
    __cache: _Any
    def __init__(self):
        ...
    @property
    def isEnabled(self):
        ...
    @property
    def isEnabledByServer(self):
        ...
    @property
    def w2gtConfig(self):
        ...
    def onConnected(self):
        ...
    def onDisconnected(self):
        ...
    def onAccountBecomePlayer(self):
        ...
    def onLobbyInited(self, event):
        ...
    def saveProgress(self, arenaUniqueID, playerID, progress):
        ...
    def getProgress(self, arenaUniqueID, playerID):
        ...
    # decorador original: @wg_async
    def getTips(self, geometryName, gameplayID, vehRole, vehLevel, team):
        ...
    def __serverTime(self):
        ...
    # decorador original: @adisp_process
    def __requestTips(self, geometryName, gameplayType, vehRole, vehLevel, team, eTag, callback):
        ...
    def __validateResponse(self, data):
        ...
    def __subscribe(self):
        ...
    def __unsubscribe(self):
        ...
    # decorador original: @server_settings.serverSettingsChangeListener(...)
    def __onUpdateW2GTSettings(self, diff):
        ...
    def __onSettingsReady(self):
        ...
    def __applySettingsSection(self):
        ...
    def __onServerSettingsSyncCompleted(self):
        ...
    def __onTokensUpdated(self, diff):
        ...
    def __isPlayerWinbacker(self):
        ...
    def __isVehicleRestricted(self, vehRole, vehLevel):
        ...
    def __clear(self):
        ...
    def __updateConfig(self):
        ...
    def __getFromCache(self, geometryName, gameplayType, vehRole, vehLevel, team):
        ...
    def __addToCache(self, key, eTag, data):
        ...
    def __makeCacheKey(self, *args):
        ...
    def __disposeCache(self):
        ...
    def __writeCache(self):
        ...
    @staticmethod
    def __isNewPlayer():
        ...
