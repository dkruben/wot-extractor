# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/web/client_web_api/common.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from Event import Event as Event
from web.client_web_api.battle_pass import BattlePassEventHandler as BattlePassEventHandler
from web.client_web_api.exchange import PersonalExchangeRatesDiscountsEventHandler as PersonalExchangeRatesDiscountsEventHandler
from web.client_web_api.platform import PlatformEventHandler as PlatformEventHandler
from web.client_web_api.ranked import BrowsersBridgeC2W as BrowsersBridgeC2W, RankedEventHandler as RankedEventHandler
from web.client_web_api.reactive_comm import ReactiveCommunicationEventHandler as ReactiveCommunicationEventHandler
from web.client_web_api.seniority_awards import SeniorityAwardsEventHandler as SeniorityAwardsEventHandler
from web.client_web_api.shop.stats import BalanceEventHandler as BalanceEventHandler
from web.client_web_api.shop.telecom_rentals import TelecomTokenEventHandler as TelecomTokenEventHandler
from web.client_web_api.shop.unified_trade_in import UnifiedTradeInEventHandler as UnifiedTradeInEventHandler
from web.client_web_api.util.vehicle import VehicleCompareEventHandler as VehicleCompareEventHandler, VehicleStateEventHandler as VehicleStateEventHandler
_logger: Any

class WebEventSender(object):
    onCallback: Any
    _handlers: Any
    def __init__(self):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def sendEvent(self, webEvent):
        ...
    def _createHandlers(self):
        ...
