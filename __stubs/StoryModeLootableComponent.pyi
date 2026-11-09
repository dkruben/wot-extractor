# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/client/StoryModeLootableComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import CGF as CGF
import Math as Math
from script_component.DynamicScriptComponent import DynamicScriptComponent as DynamicScriptComponent
from Event import SafeEvent as SafeEvent, EventManager as EventManager
from typing import List as List

class StoryModeLootableComponent(DynamicScriptComponent):
    _PREFAB_URL_BY_STYLE: dict
    _eventManager: Any
    onStartCapturing: Any
    onStopCapturing: Any
    def __init__(self, *args, **kwargs):
        ...
    def set_startTime(self, prevValue):
        ...
    def onDestroy(self):
        ...
    def _loadPrefab(self):
        ...
    def _onPrefabLoaded(self, objects, queue):
        ...
