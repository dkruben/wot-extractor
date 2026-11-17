# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/web/web_client_api/ui/boosters.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from web.web_client_api import w2c as w2c, W2CSchema as W2CSchema, Field as Field
from gui.shared import event_dispatcher as shared_events

class _OpenBoosterActivationWindow(W2CSchema):
    booster_id: Any

class BoostersWindowWebApiMixin(object):
    # decorador original: @w2c(...)
    def openBoosterActivationWindow(self, cmd):
        ...
