# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/helpers/events_handler.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import TYPE_CHECKING as TYPE_CHECKING
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.shared import g_eventBus as g_eventBus
from typing import Callable as Callable, Optional as Optional, Tuple as Tuple
from Event import Event as Event

class EventsHandler(object):
    __slots__: tuple
    def _getCallbacks(self):
        ...
    def _getListeners(self):
        ...
    def _getEvents(self):
        ...
    def _getRestrictions(self):
        ...
    def _subscribe(self):
        ...
    def _unsubscribe(self):
        ...
