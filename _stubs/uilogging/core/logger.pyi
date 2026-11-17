# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/uilogging/core/logger.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import BattleReplay as BattleReplay
from gui.shared.utils import getPlayerDatabaseID as getPlayerDatabaseID
from helpers import dependency as dependency
from helpers.log.adapters import getWithContext as getWithContext
from skeletons.connection_mgr import IConnectionManager as IConnectionManager
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.ui_logging import IUILoggingCore as IUILoggingCore
from PlayerEvents import g_playerEvents as playerEvents
from wotdecorators import noexcept as noexcept
from uilogging.constants import DEFAULT_LOGGER_NAME as DEFAULT_LOGGER_NAME, LogLevels as LogLevels
from uilogging.core.common import convertEnum as convertEnum
from uilogging.core.core_constants import ENSURE_SESSION_TICK as ENSURE_SESSION_TICK
from uilogging.core.log import LogRecord as LogRecord
from uilogging.core.handler import LogHandler as LogHandler, Delayer as Delayer
from uilogging.types import FeatureType as FeatureType, GroupType as GroupType, ActionType as ActionType, LogLevelType as LogLevelType

class UILoggingCore(IUILoggingCore):
    _connectionMgr: Any
    _lobbyContext: Any
    _handler: Any
    _started: Any
    _ensureSession: Any
    _sessionKeeper: Any
    _logger: Any
    def __init__(self):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def ensureSession(self):
        ...
    def isFeatureEnabled(self, feature):
        ...
    # decorador original: @noexcept
    def log(self, feature, group, action, loglevel=..., **params):
        ...
    # decorador original: @noexcept
    def logImmediately(self, feature, group, action, loglevel=..., **params):
        ...
    @property
    def _disabled(self):
        ...
    def _createLogRecord(self, feature, group, action, loglevel, **params):
        ...
    @property
    def _isEnabled(self):
        ...
    # decorador original: @noexcept
    def start(self, ensureSession=False):
        ...
    # decorador original: @noexcept
    def send(self):
        ...
    def _start(self, *args, **kwargs):
        ...
    def _stop(self, *args, **kwargs):
        ...
    def _shutdown(self):
        ...
    def _getSessionLifetime(self):
        ...
    def _startSessionKeeper(self, *args, **kwargs):
        ...
    def _stopSessionKeeper(self):
        ...
