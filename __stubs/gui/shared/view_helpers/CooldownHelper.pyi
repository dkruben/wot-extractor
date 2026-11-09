# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/view_helpers/CooldownHelper.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import operator as operator
from future.utils import viewitems as viewitems
import BigWorld as BigWorld
from gui.shared import g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.rq_cooldown import getRequestCoolDown as getRequestCoolDown

class CooldownHelper(object):
    _eventType: Any
    _eventScope: Any
    _requestIDs: Any
    _cooldownCbID: Any
    __handler: Any
    __isInCooldown: Any
    def __init__(self, requestIDs, handler, eventType, eventScope=...):
        ...
    def start(self):
        ...
    def stop(self):
        ...
    def isInCooldown(self):
        ...
    def _handleSetCoolDown(self, event):
        ...
    def _loadCallback(self, cooldown):
        ...
    def _cancelCallback(self):
        ...
    def _onCooldownTimeLeft(self):
        ...
    def _checkCooldowns(self):
        ...
