# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/PveHudWidgetsStateComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from gui.shared import g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.events import HasCtxEvent as HasCtxEvent
from pve_battle_hud import getPveHudLogger as getPveHudLogger, WidgetType as WidgetType
from script_component.DynamicScriptComponent import DynamicScriptComponent as DynamicScriptComponent
_logger: Any

class PveHudWidgetHasCtxEvent(HasCtxEvent):
    INIT_STATE = '{widgetType}_INIT_STATE'
    CHANGE_STATE = '{widgetType}_CHANGE_STATE'
    UPDATE_STATE = '{widgetType}_UPDATE_STATE'
    RESTORE_STATE = '{widgetType}_RESTORE_STATE'

class PveHudWidgetsStateComponent(DynamicScriptComponent):
    _isReconnect: Any
    def __init__(self):
        ...
    def initState(self, settings):
        ...
    def changeState(self, settings):
        ...
    def updateState(self, settings):
        ...
    def _onAvatarReady(self):
        ...
    @staticmethod
    def _sendEvent(eventType, settings):
        ...
