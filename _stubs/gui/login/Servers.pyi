# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/login/Servers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
import Settings as Settings
from gui import GUI_SETTINGS as GUI_SETTINGS
from Event import Event as Event
from predefined_hosts import g_preDefinedHosts as g_preDefinedHosts, REQUEST_RATE as REQUEST_RATE

class Servers(object):
    onServersStatusChanged: Any
    _loginPreferences: Any
    _serverList: Any
    _selectedServerIdx: Any
    def __init__(self, loginPreferences):
        ...
    def fini(self):
        ...
    def updateServerList(self):
        ...
    def _setServerList(self, baseServerList):
        ...
    def startListenCsisQuery(self, startListen):
        ...
    def setServerPreselection(self, peripheryId):
        ...
    @property
    def serverList(self):
        ...
    @property
    def selectedServerIdx(self):
        ...
    @property
    def selectedServer(self):
        ...
    def __onServerUpdate(self, _=None):
        ...

class DevelopmentServers(Servers):
    def __init__(self, loginPreferences):
        ...
    def fini(self):
        ...
    def updateServerList(self):
        ...
