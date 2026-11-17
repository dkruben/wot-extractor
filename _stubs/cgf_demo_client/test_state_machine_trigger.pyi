# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/cgf_demo_client/test_state_machine_trigger.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import CGF as CGF
import GenericComponents as GenericComponents
import Triggers as Triggers
import logging as logging
from cgf_script.registration import ComponentProperty as ComponentProperty, registerComponent as registerComponent
from cgf_demo.demo_category import DEMO_CATEGORY as DEMO_CATEGORY
_logger: Any

# decorador original: @registerComponent
class TestStateMachineStatesActivator(object):
    group = DEMO_CATEGORY
    editorTitle = 'Test State Machine States Activator'
    domain = CGF.Domain.ClientEditor
    statesList: Any
    animator: Any
    trigger: Any
    __index: Any
    callbackID: Any
    def __init__(self):
        ...
    def switchState(self, animator):
        ...

class StateMachineActivatorSystem(CGF.System):
    ActivatorActivated: Any
    ActivatorDeactivated: Any
    AnimatorAccess: Any
    ActivatorAccess: Any
    TimeTriggerAccess: Any
    Reactions: Any
    def update(self):
        ...
    def _onActivatorAdded(self, activatorObj, activator, triggerAccess):
        ...
    def _onActivatorRemoved(self, activator, triggerAccess):
        ...
    def switchState(self, activatorObj):
        ...
