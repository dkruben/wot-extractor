# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/web/web_client_api/blueprints_convert_sale/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewitems as viewitems
from past.builtins import basestring as basestring
import BigWorld as BigWorld
from gui.shared.gui_items.processors.blueprints_convert_sale import ProcessExchangeBlueprintsProcessor as ProcessExchangeBlueprintsProcessor
from nations import NAMES as NATION_NAMES
from helpers import dependency as dependency
from gui.server_events.bonuses import getNonQuestBonuses as getNonQuestBonuses, VehicleBlueprintBonus as VehicleBlueprintBonus
from math_common import decimal_round as decimal_round
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.server_events import IEventsCache as IEventsCache
from skeletons.gui.shared import IItemsCache as IItemsCache
from web.web_client_api import w2c as w2c, w2capi as w2capi, W2CSchema as W2CSchema, Field as Field
_MAX_VISIBLE_NATION_ICONS = 2
_BCS_ACTION_POSTFIX = '_BCS'

class _GetOfferByCategorySchema(W2CSchema):
    category: Any

class _ExchangeBlueprintSchema(W2CSchema):
    offerID: Any
    count: Any

# decorador original: @w2capi(...)
class BlueprintsConvertSaleWebApi(object):
    _lobbyContext: Any
    _itemsCache: Any
    _eventsCache: Any
    # decorador original: @w2c(...)
    def getBlueprintExchangeCategories(self, _):
        ...
    # decorador original: @w2c(...)
    def getBlueprintOfferByCategory(self, cmd):
        ...
    # decorador original: @w2c(...)
    def getBlueprintBalance(self, _):
        ...
    # decorador original: @w2c(...)
    def getExchangeEndTime(self, _):
        ...
    # decorador original: @w2c(...)
    def doExchangeBlueprints(self, cmd):
        ...

def wrap(data):
    ...
