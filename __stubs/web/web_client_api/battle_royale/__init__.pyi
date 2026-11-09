# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/web/web_client_api/battle_royale/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
from future.utils import listvalues as listvalues
from web.web_client_api import webApiCollection as webApiCollection
from web.web_client_api.exchange import PersonalExchangeRatesDiscountsWebApi as PersonalExchangeRatesDiscountsWebApi
from web.web_client_api.request import RequestWebApi as RequestWebApi
from web.web_client_api.sound import SoundWebApi as SoundWebApi, SoundStateWebApi as SoundStateWebApi, HangarSoundWebApi as HangarSoundWebApi
from web.web_client_api.ui import NotificationWebApi as NotificationWebApi, OpenWindowWebApi as OpenWindowWebApi
from web.web_client_api.ui import CloseWindowWebApi as CloseWindowWebApi, OpenTabWebApi as OpenTabWebApi, ContextMenuWebApi as ContextMenuWebApi, UtilWebApi as UtilWebApi
from web.web_client_api.quests import QuestsWebApi as QuestsWebApi
from web.web_client_api.shop import ShopWebApi as ShopWebApi
from web.web_client_api.vehicles import VehiclesWebApi as VehiclesWebApi
from web.web_client_api import w2capi as w2capi, W2CSchema as W2CSchema, w2c as w2c
from helpers import dependency as dependency, time_utils as time_utils
from skeletons.gui.game_control import IBattleRoyaleController as IBattleRoyaleController
from skeletons.gui.shared import IItemsCache as IItemsCache
from web.web_client_api.frontline import FrontLineWebApi as FrontLineWebApi
BattleRoyaleSeasonAchievements: Any

# decorador original: @w2capi(...)
class BattleRoyaleWebApi(W2CSchema):
    __battleRoyale: Any
    __itemsCache: Any
    # decorador original: @w2c(...)
    def handleGetCalendarInfo(self, _):
        ...
    # decorador original: @w2c(...)
    def getSeasonAchievements(self, _):
        ...
    def __getSeasonAchievements(self, achievements, template):
        ...
    def __validateSeasonData(self, seasonID, cycleID):
        ...
    def __getSeasons(self):
        ...

def createBattleRoyaleWebHanlders():
    ...
