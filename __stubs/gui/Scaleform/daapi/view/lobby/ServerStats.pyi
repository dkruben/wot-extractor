# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/ServerStats.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import BigWorld as BigWorld
import constants as constants
from wg_async import wg_await as wg_await, wg_async as wg_async
from gui.Scaleform.daapi.view.servers_data_provider import ServersDataProvider as ServersDataProvider
from gui.impl.dialogs.builders import ResSimpleDialogBuilder as ResSimpleDialogBuilder
from gui.impl.dialogs.dialogs import showSimple as showSimple
from gui.impl.gen import R as R
from gui.impl.pub.dialog_window import DialogFlags as DialogFlags
from gui.prb_control.entities.base.legacy.listener import ILegacyListener as ILegacyListener
from helpers import dependency as dependency
from helpers import i18n as i18n
from predefined_hosts import g_preDefinedHosts as g_preDefinedHosts, HOST_AVAILABILITY as HOST_AVAILABILITY, REQUEST_RATE as REQUEST_RATE
from gui import GUI_SETTINGS as GUI_SETTINGS
from gui.shared import events as events
from gui.shared.utils.functions import makeTooltip as makeTooltip
from gui.shared.event_bus import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.Scaleform.daapi.view.meta.ServerStatsMeta import ServerStatsMeta as ServerStatsMeta
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.connection_mgr import IConnectionManager as IConnectionManager
from skeletons.gui.game_control import IServerStatsController as IServerStatsController, IReloginController as IReloginController
_logger: Any

class ServerStats(ServerStatsMeta, ILegacyListener):
    serverStats: Any
    reloginCtrl: Any
    connectionMgr: Any
    _settingsCore: Any
    __isListSelected: Any
    _serversDP: Any
    def __init__(self):
        ...
    # decorador original: @wg_async
    def relogin(self, peripheryID):
        ...
    def startListenCsisUpdate(self, startListenCsis):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _updateCurrentServerInfo(self):
        ...
    def _updateServersList(self):
        ...
    def _updateRoamingCtrl(self, event=None):
        ...
    def __onStatsReceived(self):
        ...
    def __onServersUpdate(self, _=None):
        ...
    def __onRelogin(self, isCompleted):
        ...
