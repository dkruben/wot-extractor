# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/framework/managers/TutorialManager.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from Event import Event as Event, EventManager as EventManager
from gui.Scaleform.framework.entities.abstract.TutorialManagerMeta import TutorialManagerMeta as TutorialManagerMeta

class ScaleformTutorialManager(TutorialManagerMeta):
    __eventMgr: Any
    onComponentFoundEvent: Any
    onComponentDisposedEvent: Any
    onTriggerActivatedEvent: Any
    onEffectCompletedEvent: Any
    def __init__(self):
        ...
    def _dispose(self):
        ...
    def onComponentFound(self, componentId, viewTutorialId):
        ...
    def onTriggerActivated(self, componentId, triggerId, state):
        ...
    def onComponentDisposed(self, componentId):
        ...
    def onEffectCompleted(self, componentId, effectType):
        ...
