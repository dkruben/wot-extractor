# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/web/web_client_api/ranked_battles/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from functools import partial as partial
from gui.ranked_battles.constants import RankedDossierKeys as RankedDossierKeys, SeasonResultTokenPatterns as SeasonResultTokenPatterns
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared import events as events
from gui.shared import g_eventBus as g_eventBus
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams as SFViewLoadParams
from gui.Scaleform.genConsts.RANKEDBATTLES_CONSTS import RANKEDBATTLES_CONSTS as RANKEDBATTLES_CONSTS
from gui.server_events.events_helpers import isRankedPlatform as isRankedPlatform
from helpers import dependency as dependency
from skeletons.gui.game_control import IRankedBattlesController as IRankedBattlesController
from skeletons.gui.server_events import IEventsCache as IEventsCache
from skeletons.gui.shared import IItemsCache as IItemsCache
from web.web_client_api import w2capi as w2capi, w2c as w2c, W2CSchema as W2CSchema, webApiCollection as webApiCollection, Field as Field
from web.web_client_api.clans import ClansWebApi as ClansWebApi
from web.web_client_api.exchange import PersonalExchangeRatesDiscountsWebApi as PersonalExchangeRatesDiscountsWebApi
from web.web_client_api.quests import QuestsWebApi as QuestsWebApi
from web.web_client_api.request import RequestWebApi as RequestWebApi
from web.web_client_api.sound import SoundWebApi as SoundWebApi, SoundStateWebApi as SoundStateWebApi, HangarSoundWebApi as HangarSoundWebApi
from web.web_client_api.shop import ShopWebApi as ShopWebApi
from web.web_client_api.ui import NotificationWebApi as NotificationWebApi, ContextMenuWebApi as ContextMenuWebApi, OpenWindowWebApi as OpenWindowWebApi, CloseWindowWebApi as CloseWindowWebApi, OpenTabWebApi as OpenTabWebApi, UtilWebApi as UtilWebApi
from web.web_client_api.ui.ranked import OpenRankedPagesMixin as OpenRankedPagesMixin
BROWSER_BRIDGE_EVENT = 'browser_bridge_event'
DEFAULT_WEB_HANDLERS: set

# decorador original: @w2capi(...)
class RankedBattlesWebApi(OpenRankedPagesMixin):
    __eventsCache: Any
    __itemsCache: Any
    __rankedController: Any
    # decorador original: @w2c(...)
    def closeBrowser(self, _):
        ...
    # decorador original: @w2c(...)
    def getGamemodeState(self, _):
        ...
    # decorador original: @w2c(...)
    def getPlatformQuestsInfo(self, _):
        ...
    # decorador original: @w2c(...)
    def getSeasonsStats(self, _):
        ...
    def __getRankedSeasonDossier(self, seasonKey, seasonID):
        ...

class _ProxyDataSchema(W2CSchema):
    data: Any

# decorador original: @w2capi(...)
class BrowsersBridgeW2C(object):
    # decorador original: @w2c(...)
    def sendData(self, cmd):
        ...

class _OpenTabWebApi(OpenTabWebApi):
    __rankedController: Any
    def _getVehiclePreviewReturnAlias(self, cmd):
        ...
    def _getVehiclePreviewReturnCallback(self, cmd):
        ...
    def _getVehicleStylePreviewCallback(self, cmd):
        ...
    def __getRankedShopCallback(self, cmd):
        ...

class _SoundStateWebApi(SoundStateWebApi):
    _ON_EXIT_STATES: dict

def _packQuest(quest, rankModel):
    ...
def createRankedOverlayHandlers():
    ...
def createRankedBattlesWebHandlers():
    ...
