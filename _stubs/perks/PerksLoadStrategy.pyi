# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/perks/PerksLoadStrategy.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import iteritems as iteritems
from perks.vse_plan import VsePlan as VsePlan, PlanStatus as PlanStatus
from wg_async import wg_async as wg_async, wg_await as wg_await, distributeLoopOverTicks2 as distributeLoopOverTicks2
BUILDER: dict

class LoadType:
    DEFAULT = 0
    AUTO_START = 1
    DELAYED_LOAD_START = 2

class LoadState:
    DEFAULT = 0
    PRE_LOAD = 1
    LOAD = 2
    PRE_START = 3
    START = 4
    STATUS_LOADED: tuple

class BaseLoadStrategy(object):
    _plans: Any
    _scope: Any
    _owner: Any
    _state: Any
    _onPlansReady: Any
    def __init__(self, plans, scope, owner, onPlanReady):
        ...
    def load(self):
        ...
    def start(self):
        ...
    def beforeBattleStart(self):
        ...
    @property
    def state(self):
        ...
    def _setState(self, value):
        ...
    def _stateLogic(self):
        ...
    def _onStatusChanged(self):
        ...
    def _checkIsAllPlansReady(self):
        ...
    def _checkIsAllPlansLoaded(self):
        ...
    def _clearPlansCallback(self):
        ...
    def _onReady(self):
        ...

class DefaultLoadStrategy(BaseLoadStrategy):
    def load(self):
        ...
    def start(self):
        ...
    # decorador original: @wg_async
    def loadPlansAsync(self, isAutoStart=False):
        ...
    # decorador original: @wg_async
    def _startAsync(self):
        ...
    def _onStatusChanged(self):
        ...
    def _stateLogic(self):
        ...

class AutoStartStrategy(DefaultLoadStrategy):
    def start(self):
        ...
    def load(self):
        ...
    def _stateLogic(self):
        ...
    def _onStatusChanged(self):
        ...

class DelayLoadStartStrategy(DefaultLoadStrategy):
    _isStarted: Any
    def __init__(self, plans, scope, owner, onPlanReady):
        ...
    def load(self):
        ...
    def start(self):
        ...
    def beforeBattleStart(self):
        ...
    def _onStatusChanged(self):
        ...
    def _stateLogic(self):
        ...

def getLoadStarategy(value):
    ...
