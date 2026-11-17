# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/store/browser/web_handlers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.shared.event_dispatcher import showShop as showShop
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from web.web_client_api import webApiCollection as webApiCollection
from web.web_client_api.clans import ClansWebApi as ClansWebApi
from web.web_client_api.exchange import PersonalExchangeRatesDiscountsWebApi as PersonalExchangeRatesDiscountsWebApi
from web.web_client_api.platform import PlatformWebApi as PlatformWebApi
from web.web_client_api.quests import QuestsWebApi as QuestsWebApi
from web.web_client_api.loot_boxes_system import LootBoxSystemWebApi as LootBoxSystemWebApi
from web.web_client_api.ranked_battles import RankedBattlesWebApi as RankedBattlesWebApi
from web.web_client_api.request import RequestWebApi as RequestWebApi
from web.web_client_api.seniority_awards import SeniorityAwardsWebApi as SeniorityAwardsWebApi
from web.web_client_api.sound import SoundWebApi as SoundWebApi, SoundStateWebApi as SoundStateWebApi, HangarSoundWebApi as HangarSoundWebApi
from web.web_client_api.shop import ShopWebApi as ShopWebApi
from web.web_client_api.hero_tank import HeroTankWebApi as HeroTankWebApi
from web.web_client_api.battle_pass import BattlePassWebApi as BattlePassWebApi
from web.web_client_api.ui import NotificationWebApi as NotificationWebApi, OpenWindowWebApi as OpenWindowWebApi, OpenTabWebApi as OpenTabWebApi, CloseWindowWebApi as CloseWindowWebApi, UtilWebApi as UtilWebApi
from web.web_client_api.frontline import FrontLineWebApi as FrontLineWebApi
from web.web_client_api.blueprints_convert_sale import BlueprintsConvertSaleWebApi as BlueprintsConvertSaleWebApi
from web.web_client_api.uilogging import UILoggingWebApi as UILoggingWebApi
_SHOP_HANDLERS: list

class _OpenTabWebApi(OpenTabWebApi):
    def _getVehiclePreviewReturnAlias(self, cmd):
        ...
    def _getVehiclePreviewReturnCallback(self, cmd):
        ...
    def _getVehicleStylePreviewCallback(self, cmd):
        ...
    def __getReturnCallback(self, backUrl):
        ...

def createShopWebHandlers():
    ...
