# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/cgf_demo/test_triggers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import functools as functools
import random as random
import math as math
import GenericComponents as GenericComponents
import Triggers as Triggers
import CGF as CGF
import Math as Math
import logging as logging
from typing import List as List
from cgf_demo.demo_category import DEMO_CATEGORY as DEMO_CATEGORY
from cgf_script.registration import ComponentProperty as ComponentProperty, registerComponent as registerComponent
from cgf_demo.test_movers import TestScriptAxisRotator as TestScriptAxisRotator
from HealthComponent import HealthComponent as HealthComponent
from constants import IS_CLIENT as IS_CLIENT
_logger: Any

class Vehicle(object):
    ...

# decorador original: @registerComponent
class TestRotateWhileInTrigger(object):
    group = DEMO_CATEGORY
    editorTitle = 'Test Rotate While In Trigger'
    domain = CGF.Domain.Client
    rotationSpeed: Any

# decorador original: @registerComponent
class TestComponentCreation(object):
    group = DEMO_CATEGORY
    editorTitle = 'Test Component Creation'
    domain = CGF.Domain.Client
    trigger: Any
    rotationSpeed: Any

# decorador original: @registerComponent
class TestPrefabSpawner(object):
    group = DEMO_CATEGORY
    editorTitle = 'Test Prefab Spawner'
    domain = CGF.Domain.Client
    prefabPath: Any
    instancesCount: Any
    areaToSpawn: Any
    triggerToMonitor: Any
    transform: Any
    attachToEntered: Any

class TestComponentCreationSystem(CGF.System):
    CreationActivated: Any
    PrefabSpawnerActivated: Any
    TransformAccess: Any
    RotatorAccess: Any
    RemoveDelayedAccess: Any
    VehicleAccess: Any
    AreaTriggerAccess: Any
    CylinderAreaAccess: Any
    PrefabSpawnerAccess: Any
    Reactions: Any
    def update(self):
        ...
    def _onTestComponentCreationAdded(self, testComponentCreation, triggerAccess):
        ...
    def _onPrefabSpawnerAdded(self, spawnerObj, prefabSpawner, triggerAccess):
        ...
    def __componentCreationEnter(self, rotationSpeed, who, where):
        ...
    def __componentCreationExit(self, who, where):
        ...
    def __onPrefabSpawnerEnter(self, spawnerObj, who, where):
        ...
    def __spawn(self, spawner, who):
        ...

class TestTriggersSystem(CGF.System):
    RotatorIterate: Any
    Reactions: Any
    def update(self):
        ...

# decorador original: @registerComponent
class TestVehicleAreaTriggerComponent(object):
    group = DEMO_CATEGORY
    editorTitle = 'Test Vehicle Area Trigger'
    domain = CGF.Domain.ServerEditor
    trigger: Any
    health: Any
    isDamageTrigger: Any
    reactionID: Any
    def __init__(self):
        ...

# decorador original: @registerComponent
class TestHealthTriggersComponent(object):
    group = DEMO_CATEGORY
    editorTitle = 'Test Health Triggers'
    domain = CGF.Domain.ServerEditor
    healthComponent: Any
    trigger: Any
    health: Any
    isDamageTrigger: Any
    reactionID: Any
    def __init__(self):
        ...
