# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/VisualScriptCache.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from visual_script.misc import ASPECT as ASPECT
from visual_script.multi_plan_provider import MultiPlanCache as MultiPlanCache

class VisualScriptCache(BigWorld.DynamicScriptComponent):
    _multiPlanCache: Any
    def __init__(self):
        ...
    def _destroy(self):
        ...
    def onLeaveWorld(self):
        ...
    def onDestroy(self):
        ...
    def getPlan(self, componentName, planNames):
        ...
