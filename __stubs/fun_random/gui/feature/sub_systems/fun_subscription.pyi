# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/feature/sub_systems/fun_subscription.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from Event import SuspendedEventManager as SuspendedEventManager, SuspendedEvent as SuspendedEvent
from fun_random.gui.shared import g_funEventBus as g_funEventBus
from fun_random.gui.shared.events import EventBridge as EventBridge, FunEventScope as FunEventScope, FunEventType as FunEventType
from gui.shared import events as events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from skeletons.gui.game_control import IFunRandomController as IFunRandomController
from gui.shared.event_bus import SharedEvent as SharedEvent

class FunSubscription(IFunRandomController.IFunSubscription):
    __em: Any
    __handleEvent: Any
    __eventsBridges: Any
    def __init__(self):
        ...
    def fini(self):
        ...
    def clear(self):
        ...
    def resume(self):
        ...
    def suspend(self):
        ...
    def addListener(self, eventType, handler, scope=...):
        ...
    def removeListener(self, eventType, handler, scope=...):
        ...
    def handleEvent(self, event, scope=...):
        ...
    def startCoreNotifications(self):
        ...
    def __addSubModesListener(self, method, desiredOnly=False, withTicks=False):
        ...
