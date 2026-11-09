# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/macroses.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from future.moves.urllib.parse import quote_plus as quote_plus
import BigWorld as BigWorld
import constants as constants
from adisp import adisp_async as adisp_async, adisp_process as adisp_process
from helpers import getClientLanguage as getClientLanguage, dependency as dependency
from helpers.http.url_formatters import addParamsToUrlQuery as addParamsToUrlQuery
from py2to3.compat import base64compat as base64compat
from skeletons.gui.login_manager import ILoginManager as ILoginManager
from skeletons.gui.web import IWebController as IWebController
from skeletons.connection_mgr import IConnectionManager as IConnectionManager
from skeletons.gui.game_control import IMarathonEventsController as IMarathonEventsController

def getLanguageCode(args=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getAreaID(args=None, connectionMgr=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getEncodedLogin(args=None, connectionMgr=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getQuotedLogin(args=None, connectionMgr=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getDatabaseID(args=None, connectionMgr=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getPeripheryID(args=None, connectionMgr=None):
    ...
def getUnitServerID(args=None):
    ...
def getAuthRealm(args=None):
    ...
def getCurrentRealm(args=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getMarathonPackage(args=None, marathonCtrl=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getMarathonStylePackage(args=None, marathonCtrl=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def isSteamClient(args=None, loginManager=None):
    ...
def getClanDBID(args=None):
    ...
def getSyncMacroses():
    ...
# decorador original: @adisp_async
def getWgniToken(proxy, args, params, callback):
    ...
# decorador original: @adisp_async
# decorador original: @adisp_process
def getTargetURL(proxy, args, params, callback):
    ...
# decorador original: @adisp_async
# decorador original: @adisp_process
def getUrlParams(proxy, args, params, callback):
    ...
def getAsyncMacroses():
    ...
