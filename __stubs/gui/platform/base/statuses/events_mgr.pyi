# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/platform/base/statuses/events_mgr.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import Event as Event
from gui.platform.base.logger import getWithContext as getWithContext
from gui.platform.base.statuses.constants import StatusTypes as StatusTypes, DEFAULT_CONTEXT as DEFAULT_CONTEXT
from gui.platform.base.statuses.status import Status as Status

class StatusEventsManager(object):
    _logger: Any
    _em: Any
    _events: Any
    def __init__(self):
        ...
    def subscribe(self, statusType, handler, context=...):
        ...
    def unsubscribe(self, statusType, handler, context=...):
        ...
    def send(self, status, context=...):
        ...
    def clear(self):
        ...
    def _get(self, context, statusType):
        ...
