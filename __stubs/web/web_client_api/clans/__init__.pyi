# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/web/web_client_api/clans/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.clans.clan_cache import g_clanCache as g_clanCache
from messenger.proto.shared_find_criteria import MutualFriendsFindCriteria as MutualFriendsFindCriteria
from web.web_client_api import w2capi as w2capi, w2c as w2c, W2CSchema as W2CSchema
from web.web_client_api.social import getStatuses as getStatuses
from helpers import dependency as dependency
from skeletons.gui.game_control import IClanNotificationController as IClanNotificationController
from skeletons.gui.web import IWebController as IWebController

# decorador original: @w2capi(...)
class ClansWebApi(object):
    __notificationCtrl: Any
    __webCtrl: Any
    # decorador original: @w2c(...)
    def membersOnline(self, cmd):
        ...
    # decorador original: @w2c(...)
    def membersStatus(self, cmd):
        ...
    # decorador original: @w2c(...)
    def friendsStatus(self, cmd):
        ...
    # decorador original: @w2c(...)
    def setNewsCounter(self, cmd):
        ...
    # decorador original: @w2c(...)
    def getNewsCounters(self, cmd):
        ...
    # decorador original: @w2c(...)
    def getClanInfo(self, cmd):
        ...
