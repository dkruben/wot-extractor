# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/visual_script/debug_plan_loader.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from constants import IS_DEVELOPMENT as IS_DEVELOPMENT
import VSE as VSE
import weakref as weakref
from debug_utils import LOG_DEBUG_DEV as LOG_DEBUG_DEV
from visual_script.plan_holder import PlanHolder as PlanHolder
from visual_script.plan_tags import getAllTags as getAllTags
debugPlanLoader: Any

class DebugPlanHolder(PlanHolder):
    __slots__: tuple
    contextName: Any
    def __init__(self, plan, state, auto=False):
        ...

class DebugPlanLoader(object):
    __contextAll: Any
    __plans: Any
    __tags: Any
    def __init__(self):
        ...
    def getContext(self, name):
        ...
    def regContext(self, context):
        ...
    def unregContext(self, context):
        ...
    def startPlan(self, planName, contextName, aspect, params=...):
        ...
    def stopPlan(self, planName):
        ...
    def stopAllPlans(self):
        ...
    def __contextDestroyed(self, context):
        ...
