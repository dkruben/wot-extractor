# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/queues/LimitedThroughputQueue.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from past.builtins import xrange as xrange
import BigWorld as BigWorld

class LimitedThroughputQueue:
    __queue: Any
    __actionsPerSecond: Any
    __maxActionsPerBatch: Any
    __timerID: Any
    def __init__(self, actionsPerSecond, maxActionsPerBatch=1):
        ...
    def scheduleAction(self, action):
        ...
    def _startJob(self):
        ...
    def _stopJob(self):
        ...
    def _job(self, timerID, _=0):
        ...
    @property
    def actionsPerSecond(self):
        ...
