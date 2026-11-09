# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/clans/browser/web_handlers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.shared.event_dispatcher import showClanQuestWindow as showClanQuestWindow
from web.web_client_api import webApiCollection as webApiCollection
from web.web_client_api.exchange import PersonalExchangeRatesDiscountsWebApi as PersonalExchangeRatesDiscountsWebApi
from web.web_client_api.request import RequestWebApi as RequestWebApi
from web.web_client_api.rewards import RewardsWebApi as RewardsWebApi
from web.web_client_api.shop import ShopWebApi as ShopWebApi
from web.web_client_api.social import SocialWebApi as SocialWebApi
from web.web_client_api.sound import SoundWebApi as SoundWebApi, SoundStateWebApi as SoundStateWebApi
from web.web_client_api.clans import ClansWebApi as ClansWebApi
from web.web_client_api.strongholds import StrongholdsWebApi as StrongholdsWebApi
from web.web_client_api.ui import OpenWindowWebApi as OpenWindowWebApi, OpenTabWebApi as OpenTabWebApi, UtilWebApi as UtilWebApi, ContextMenuWebApi as ContextMenuWebApi, CloseWindowWebApi as CloseWindowWebApi

class _OpenTabWebApi(OpenTabWebApi):
    def _getVehiclePreviewReturnAlias(self, cmd):
        ...
    def _getVehiclePreviewReturnCallback(self, cmd):
        ...
    def __getReturnCallback(self, backUrl):
        ...

def createNotificationWebHandlers():
    ...
