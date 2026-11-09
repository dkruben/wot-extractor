# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/cgf_demo/test_bridge.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import CGF as CGF
import Triggers as Triggers
import math as math
import logging as logging
from cgf_script.registration import ComponentProperty as ComponentProperty, registerComponent as registerComponent
from Math import Matrix as Matrix
from cgf_demo.demo_category import DEMO_CATEGORY as DEMO_CATEGORY
_logger: Any

# decorador original: @registerComponent
class TestBridge(object):
    group = DEMO_CATEGORY
    editorTitle = 'Test Bridge'
    domain = CGF.Domain.ClientEditor
    moverTransform1: Any
    moverTransform2: Any
    trigger1: Any
    trigger2: Any
    limit: Any
    speed: Any
    moveDirection1: Any
    moveDirection2: Any
    def tr1In(self, who, where):
        ...
    def tr1Out(self, who, where):
        ...
    def tr2In(self, who, where):
        ...
    def tr2Out(self, who, where):
        ...

class TestBridgeSystem(CGF.System):
    BridgeCreated: Any
    BridgeActivated: Any
    BridgeIterate: Any
    TransformAccess: Any
    AreaTriggerAccess: Any
    Reactions: Any
    def update(self):
        ...
    def _createBridge(self, bridge):
        ...
    def _activateBridge(self, bridge, triggerAccess):
        ...
    def __simulate(self, bridge, dt, transformAccess):
        ...

def createRTMatrix(rotation, translation):
    ...
