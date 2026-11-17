# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/web/web_client_api/ui/tankman.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from past.builtins import basestring as basestring
from gui.server_events.recruit_helper import getRecruitInfo as getRecruitInfo
from web.web_client_api import w2c as w2c, W2CSchema as W2CSchema, Field as Field
from gui.server_events import events_dispatcher as server_events

class _RecruitIDSchema(W2CSchema):
    recruit_id: Any

class OpenTankmanWebApiMixin(object):
    # decorador original: @w2c(...)
    def openRecruitingWindow(self, cmd):
        ...

def _tankManTokenValidator(tokenID):
    ...
