# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/synchronous_event.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from wg_async import wg_async as wg_async, forwardAsFuture as forwardAsFuture, wg_await as wg_await
from debug_utils import LOG_CURRENT_EXCEPTION as LOG_CURRENT_EXCEPTION
from Event import Event as Event

class SynchronousEvent(Event):
    __slots__: tuple
    # decorador original: @wg_async
    def __call__(self, *args, **kwargs):
        ...
