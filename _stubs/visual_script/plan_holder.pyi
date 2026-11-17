# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/visual_script/plan_holder.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewitems as viewitems
from debug_utils import LOG_ERROR as LOG_ERROR

class PlanHolder(object):
    __slots__: tuple
    INACTIVE = 0
    LOADING = 1
    LOADED = 2
    ERROR = 3
    LOAD_CANCELED = 4
    plan: Any
    loadState: Any
    autoStart: Any
    __inputParamCache: Any
    params: Any
    __planName: Any
    key: Any
    def __init__(self, plan, state, auto=False):
        ...
    @property
    def isLoaded(self):
        ...
    @property
    def isError(self):
        ...
    @property
    def isLoadCanceled(self):
        ...
    def load(self, planName, aspect, tags):
        ...
    def loadOverTime(self, planName, aspect, tags):
        ...
    def onLoad(self, status):
        ...
    def start(self):
        ...
    def _fetchInputParams(self):
        ...
    def setOptionalInputParam(self, name, value):
        ...
    def setOptionalInputParams(self, **kwargs):
        ...
