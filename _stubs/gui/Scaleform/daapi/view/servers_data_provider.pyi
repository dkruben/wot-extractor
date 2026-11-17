# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/servers_data_provider.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from gui.Scaleform.framework.entities.DAAPIDataProvider import SortableDAAPIDataProvider as SortableDAAPIDataProvider
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.formatters import icons as icons
from gui.shared.formatters.servers import formatPingStatus as formatPingStatus
from helpers import dependency as dependency
from predefined_hosts import AUTO_LOGIN_QUERY_URL as AUTO_LOGIN_QUERY_URL
from predefined_hosts import HOST_AVAILABILITY as HOST_AVAILABILITY, PING_STATUSES as PING_STATUSES, g_preDefinedHosts as g_preDefinedHosts
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.connection_mgr import IConnectionManager as IConnectionManager
_logger: Any

class _INDICATOR_STATUSES(object):
    WAITING = -1
    IGNORED = -2
    ALL: tuple

class ServersDataProvider(SortableDAAPIDataProvider):
    __PING_MAX_VALUE = 999
    __settingsCore: Any
    __connectionManager: Any
    _list: Any
    __mapping: Any
    __selectedID: Any
    __isColorBlind: Any
    def __init__(self):
        ...
    @property
    def collection(self):
        ...
    @property
    def isColorBlind(self):
        ...
    def emptyItem(self):
        ...
    def clear(self):
        ...
    def fini(self):
        ...
    def getSelectedIdx(self):
        ...
    def getSelectedID(self):
        ...
    def setSelectedID(self, sid):
        ...
    def resetSelectedIndex(self):
        ...
    def getVO(self, index):
        ...
    def buildList(self, cache):
        ...
    def rebuildList(self, cache):
        ...
    def pyGetSelectedIdx(self):
        ...
    def refreshRandomItems(self, indexes, items):
        ...
    def refreshSingleItem(self, index, item):
        ...
    def requestItemAtHandler(self, idx):
        ...
    def _makeVO(self, index, item):
        ...
    def __clearLists(self):
        ...
    def __onSettingsChanged(self, diff):
        ...
    def __getUpdatedPingStatus(self, pingStatus, item):
        ...
    @staticmethod
    def __checkPingForValidStatus(incomeStatus):
        ...
