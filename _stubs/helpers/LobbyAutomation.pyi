# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/helpers/LobbyAutomation.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import BigWorld as BigWorld
from frameworks.wulf import WindowLayer as WindowLayer
from gui.Scaleform.Waiting import Waiting as Waiting
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.framework.managers.containers import POP_UP_CRITERIA as POP_UP_CRITERIA
from gui.app_loader import settings as app_settings
from AccountCommands import CMD_PRB_TEAM_READY as CMD_PRB_TEAM_READY
from helpers import dependency as dependency
from skeletons.connection_mgr import IConnectionManager as IConnectionManager
from skeletons.gui.app_loader import IAppLoader as IAppLoader
_isConnecting = False
_server = ''
_login = ''
_password = ''
_battleTime = 10
_arenaId = 1
_justLogin = True

def _getLobby():
    ...
def setServerName(name):
    ...
def setLogin(login):
    ...
def setPassword(password):
    ...
def setBattleTime(time):
    ...
def setArenaId(arenaId):
    ...
def configure(serverName, login, password, battleTime, arenaId):
    ...
def logIn():
    ...
def startBattle():
    ...
def _detectCurrentScreen():
    ...
def _connect():
    ...
def _leaveDevRoom():
    ...
def _enterDevRoom():
    ...
def _enterBattle():
    ...
def _battleCallback(p1, p2, p3):
    ...
