# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/cgf_demo/test_module.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import CGF as CGF
import logging as logging
from constants import IS_CLIENT as IS_CLIENT, IS_EDITOR as IS_EDITOR
from cgf_script.registration import registerModule as registerModule
from cgf_demo.demo_category import DEMO_CATEGORY as DEMO_CATEGORY
from cgf_demo.test_bridge import TestBridgeSystem as TestBridgeSystem, TestBridge as TestBridge
from cgf_demo.test_movers import TestAxisRotatorSystem as TestAxisRotatorSystem, TestScriptAxisRotator as TestScriptAxisRotator, TestScriptMover as TestScriptMover
from cgf_demo.test_triggers import TestComponentCreation as TestComponentCreation, TestComponentCreationSystem as TestComponentCreationSystem, TestHealthTriggersComponent as TestHealthTriggersComponent, TestPrefabSpawner as TestPrefabSpawner, TestRotateWhileInTrigger as TestRotateWhileInTrigger, TestTriggersSystem as TestTriggersSystem, TestVehicleAreaTriggerComponent as TestVehicleAreaTriggerComponent
_logger: Any

class TestEdgeDrawerComponentSystem(object):
    Reactions: Any

class TestEdgeDrawerComponent(object):
    ...

# decorador original: @registerModule
class TestModule(object):
    name = 'Test Module'
    group = DEMO_CATEGORY
    systems: list
    components: list
