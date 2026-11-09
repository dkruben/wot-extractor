# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/web/web_client_api/frontline/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from helpers import dependency as dependency
from skeletons.gui.game_control import IEpicBattleMetaGameController as IEpicBattleMetaGameController
from web.web_client_api import w2c as w2c, w2capi as w2capi, W2CSchema as W2CSchema

# decorador original: @w2capi(...)
class FrontLineWebApi(W2CSchema):
    __epicController: Any
    # decorador original: @w2c(...)
    def handleGetPlayerDiscount(self, _):
        ...
    # decorador original: @w2c(...)
    def handleGetCalendarInfo(self, _):
        ...
