# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/cgf_demo_client/test_triggers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import functools as functools
import CGF as CGF
import GameplayDebug as GameplayDebug
import GenericComponents as GenericComponents
import Triggers as Triggers
from cgf_demo.demo_category import DEMO_CATEGORY as DEMO_CATEGORY
from cgf_script.registration import ComponentProperty as ComponentProperty, registerComponent as registerComponent
from HealthComponent import HealthComponent as HealthComponent

# decorador original: @registerComponent
class ShowHealthInfoComponent(object):
    group = DEMO_CATEGORY
    editorTitle = 'Show Health Info Component'
    domain = CGF.Domain.ClientEditor

# decorador original: @registerComponent
class TestEntranceNotifier(object):
    group = DEMO_CATEGORY
    editorTitle = 'Test Entrance Notifier'
    domain = CGF.Domain.Client
    textComponent: Any
    trigger: Any
    title: Any
    __log: Any
    __messageCount: Any
    def __init__(self):
        ...
    def addMessage(self, message, text):
        ...
    def __flushText(self, text):
        ...

class EntranceModifierSystem(CGF.System):
    EntranceActivated: Any
    AreaTriggerAccess: Any
    DebugTextAccess: Any
    EntranceAccess: Any
    TransformAccess: Any
    Reactions: Any
    def update(self):
        ...
    def _onEntranceAdded(self, entranceObj, entrance, triggerAccess):
        ...
    def __onEnter(self, entranceObj, who, where):
        ...
    def __onExit(self, entranceObj, who, where):
        ...

class TestHealthMonitoringSystem(CGF.System):
    HealthInfoActivated: Any
    HealthIterate: Any
    GradationIterate: Any
    Reactions: Any
    def update(self):
        ...
    def _onAddedShowHealthInfo(self, go):
        ...
    def _showCurrentHealth(self, health, debugText):
        ...
    def _showExplosion(self, gradation, health, debugText):
        ...
