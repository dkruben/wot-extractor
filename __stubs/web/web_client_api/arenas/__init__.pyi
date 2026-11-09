# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/web/web_client_api/arenas/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewitems as viewitems
import ArenaType as ArenaType
from gui.impl import backport as backport
from gui.impl.gen import R as R
from web.web_client_api import w2c as w2c, w2capi as w2capi, Field as Field, W2CSchema as W2CSchema
INVALID_DYN_ATTR = -1

class _ArenaInfoSchema(W2CSchema):
    arena_id: Any

class _ArenasInfoSchema(W2CSchema):
    arena_ids: Any

# decorador original: @w2capi(...)
class ArenasWebApi(object):
    # decorador original: @w2c(...)
    def arenaInfo(self, cmd):
        ...
    # decorador original: @w2c(...)
    def arenasInfo(self, cmd):
        ...
    def __collectArenaInfo(self, arenaType):
        ...
    def __getText(self, text):
        ...
    def __getImage(self, image):
        ...
