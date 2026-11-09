# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/live_ops_web_events/entry_point_base.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from frameworks.wulf import ViewModel as ViewModel

class State(Enum):
    PRE_EVENT = 'preEvent'
    EVENT_ACTIVE = 'eventActive'
    POST_EVENT = 'postEvent'

class EntryPointBase(ViewModel):
    __slots__: tuple
    def __init__(self, properties=2, commands=0):
        ...
    def getState(self):
        ...
    def setState(self, value):
        ...
    def getPreviousState(self):
        ...
    def setPreviousState(self, value):
        ...
    def _initialize(self):
        ...
