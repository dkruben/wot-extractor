# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/persistent_data_cache_common/events.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from Event import EventManager as EventManager, SafeEvent as SafeEvent

class DefaultPDCEventsDispatcher(object):
    __slots__: tuple
    _manager: Any
    onDataDeserialized: Any
    onCachedDataLoaded: Any
    onFailedToLoadCachedData: Any
    onCacheDataSavingStarted: Any
    onCachedDataSaved: Any
    onFailedToSaveCachedData: Any
    def __init__(self):
        ...
    def fini(self):
        ...
