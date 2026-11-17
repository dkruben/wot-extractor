# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/uilogging/last_stand/loggers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import TYPE_CHECKING as TYPE_CHECKING
from last_stand.uilogging.last_stand.constants import NarrationLogAction as NarrationLogAction, FEATURE as FEATURE
from uilogging.base.logger import MetricsLogger as MetricsLogger
from uilogging.types import ItemType as ItemType

class NarrationEventLogger(MetricsLogger):
    __slots__: tuple
    def __init__(self):
        ...
    def logStartEvent(self, item):
        ...
    def logEndEvent(self, item):
        ...
