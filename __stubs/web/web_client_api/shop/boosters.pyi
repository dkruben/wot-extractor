# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/web/web_client_api/shop/boosters.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from helpers import dependency as dependency
from skeletons.gui.goodies import IGoodiesCache as IGoodiesCache
from web.web_client_api import w2c as w2c, W2CSchema as W2CSchema, Field as Field

class _ActiveBoostersSchema(W2CSchema):
    filter_types: Any

class BoostersInfoWebApiMixin(object):
    __goodiesCache: Any
    # decorador original: @w2c(...)
    def getActiveBoosters(self, cmd):
        ...
