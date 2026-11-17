# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/web/web_client_api/shop/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from web.web_client_api import w2capi as w2capi
from web.web_client_api.shop.actions import ActionsWebApiMixin as ActionsWebApiMixin
from web.web_client_api.shop.boosters import BoostersInfoWebApiMixin as BoostersInfoWebApiMixin
from web.web_client_api.shop.common import SettingsWebApiMixin as SettingsWebApiMixin
from web.web_client_api.shop.renewable_subscription import RenewableSubWebApiMixin as RenewableSubWebApiMixin
from web.web_client_api.shop.stats import BalanceWebApiMixin as BalanceWebApiMixin
from web.web_client_api.shop.stock import ItemsWebApiMixin as ItemsWebApiMixin
from web.web_client_api.shop.telecom_rentals import TelecomRentalsWebApiMixin as TelecomRentalsWebApiMixin
from web.web_client_api.shop.trade import TradeWebApiMixin as TradeWebApiMixin
from web.web_client_api.shop.unified_trade_in import UnifiedTradeInWebApiMixin as UnifiedTradeInWebApiMixin

# decorador original: @w2capi(...)
class ShopWebApi(ActionsWebApiMixin, BalanceWebApiMixin, ItemsWebApiMixin, TradeWebApiMixin, UnifiedTradeInWebApiMixin, BoostersInfoWebApiMixin, RenewableSubWebApiMixin, TelecomRentalsWebApiMixin, SettingsWebApiMixin):
    ...
