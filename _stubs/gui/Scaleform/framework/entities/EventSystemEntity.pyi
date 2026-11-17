# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/framework/entities/EventSystemEntity.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.Scaleform.framework.entities.DisposableEntity import DisposableEntity as DisposableEntity
from gui.shared import g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, EventPriority as EventPriority

class EventSystemEntity(DisposableEntity):
    def fireEvent(self, event, scope=...):
        ...
    def addListener(self, eventType, handler, scope=..., priority=...):
        ...
    def removeListener(self, eventType, handler, scope=...):
        ...
    def addRestriction(self, eventType, restriction, scope=..., priority=...):
        ...
    def removeRestriction(self, eventType, restriction, scope=...):
        ...
