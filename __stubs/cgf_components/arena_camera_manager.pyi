# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/cgf_components/arena_camera_manager.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import CGF as CGF
from CameraComponents import CameraComponent as CameraComponent
_logger: Any

class ArenaCameraSystem(CGF.System):
    CameraActivated: Any
    CameraDeactivated: Any
    Reactions: Any
    __cameras: Any
    def __init__(self, *args):
        ...
    def update(self):
        ...
    def getCameraTransform(self, name):
        ...
    def onCameraAdded(self, cameraComponent, transformComponent):
        ...
    def onCameraRemoved(self, cameraComponent):
        ...
