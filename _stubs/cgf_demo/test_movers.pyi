# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/cgf_demo/test_movers.py (BYTECODE: a descompilacao falhou; sem bases, decoradores nem valores por omissao).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import CGF as CGF
from Math import Matrix as Matrix
from cgf_script.registration import ComponentProperty as ComponentProperty, registerComponent as registerComponent
from cgf_demo.demo_category import DEMO_CATEGORY as DEMO_CATEGORY
absolute_import: Any
division: Any
clamp: Any

# gerado do bytecode: classes base desconhecidas
class TestScriptAxisRotator:
    group: Any
    editorTitle: Any
    domain: Any
    rotationSpeedYaw: Any
    rotationSpeedPitch: Any
    rotationSpeedRoll: Any
    transform: Any

# gerado do bytecode: classes base desconhecidas
class TestScriptMover:
    group: Any
    editorTitle: Any
    domain: Any
    finalPoint: Any
    period: Any
    transform: Any
    def prepare(self, transform):
        ...

# gerado do bytecode: classes base desconhecidas
class TestAxisRotatorSystem:
    MoverCreated: Any
    MoverActivated: Any
    MoverIterate: Any
    RotatorIterate: Any
    TransformAccess: Any
    Reactions: Any
    _TestAxisRotatorSystem__move: Any
    def update(self):
        ...
    def _setupMover(self, myTransform, mover, transformAccess):
        ...
    def __move(self, myTransform, mover, delta, transformAccess):
        ...

def createRotationMatrix(rotation):
    ...

def __getattr__(name: str) -> Any: ...  # stub incompleto (gerado do bytecode)
