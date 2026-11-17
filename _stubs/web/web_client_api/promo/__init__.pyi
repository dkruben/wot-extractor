# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/web/web_client_api/promo/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from helpers import dependency as dependency
from skeletons.gui.game_control import IPromoController as IPromoController
from web.web_client_api import w2c as w2c, w2capi as w2capi, W2CSchema as W2CSchema, Field as Field

class _PromoCountSchema(W2CSchema):
    count: Any

# decorador original: @w2capi(...)
class PromoWebApi(object):
    _promoCtrl: Any
    # decorador original: @w2c(...)
    def promoCount(self, cmd):
        ...
