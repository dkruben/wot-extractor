# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/cgf_demo_client/test_hierarchy_modificator.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import math as math
import logging as logging
import BigWorld as BigWorld
import GenericComponents as GenericComponents
import Triggers as Triggers
import CGF as CGF
import math_utils as math_utils
import Math as Math
from cgf_script.registration import ComponentProperty as ComponentProperty, registerComponent as registerComponent
from cgf_demo.demo_category import DEMO_CATEGORY as DEMO_CATEGORY
from helpers import isPlayerAccount as isPlayerAccount
_logger: Any

# decorador original: @registerComponent
class TestMaterialParamManipulator(object):
    group = DEMO_CATEGORY
    editorTitle = 'Test Material Param Manipulator'
    domain = CGF.Domain.Client
    model: Any
    paramName: Any

class TestMaterialManipulatorSystem(CGF.System):
    ManipulatorIterate: Any
    ModelAccess: Any
    Reactions: Any
    def update(self):
        ...

# decorador original: @registerComponent
class HierarchyModifier(object):
    group = DEMO_CATEGORY
    editorTitle = 'Hierarchy Modifier'
    domain = CGF.Domain.Client
    gameObject1: Any
    gameObject2: Any
    gameObject3: Any
    areaTrigger1: Any
    areaTrigger2: Any
    zone1: Any
    zone2: Any
    def __init__(self):
        ...

# decorador original: @registerComponent
class HierarchyModifier2(object):
    group = DEMO_CATEGORY
    editorTitle = 'Hierarchy Modifier 2'
    domain = CGF.Domain.Client
    top: Any
    bottom: Any
    box: Any
    cameraTransform: Any
    areaTrigger: Any

class TestHierarchyModifierSystem(CGF.System):
    ModifierCreated: Any
    ModifierActivated: Any
    Modifier2Activated: Any
    Modifier2Iterate: Any
    TransformAccess: Any
    AreaTriggerAccess: Any
    HierarchyAccess: Any
    ModifierAccess: Any
    Modifier2Access: Any
    Reactions: Any
    def update(self):
        ...
    def _onHierarchyModifierAdded(self, hierarchyModifier, go, triggerAccess):
        ...
    def _onHierarchyModifierAdded2(self, hierarchyModifier2, go, triggerAccess):
        ...
    def _tick(self):
        ...
    def _setupRoot(self, hierarchyModifier, root):
        ...
    def _unwrapFigure(self, hierarchyModifier2Go, where):
        ...
    def _wrapFigure(self, hierarchyModifier2Go, where):
        ...
    def _changeHierarchy(self, hierarchy, hierarchyAccess, go, childName, newParentName):
        ...
    def _switchConnectFirstTrigger(self, modifierGo, _):
        ...
    def _switchConnectSecondTrigger(self, modifierGo, _):
        ...
    def __connect(self, rootObject, sourceObj):
        ...
    def __connectToRoot(self, modifier, sourceObj):
        ...
    def _updateTransform(self, go, newParent):
        ...

# decorador original: @registerComponent
class TestModelSwapper(object):
    group = DEMO_CATEGORY
    editorTitle = 'Test Model Swapper'
    domain = CGF.Domain.Client
    model1: Any
    model2: Any

class ModelSwapperSystem(CGF.System):
    SwapperCreated: Any
    SwapperIterate: Any
    Reactions: Any
    __swapTime: Any
    def __init__(self):
        ...
    def update(self):
        ...
