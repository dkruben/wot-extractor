# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/vehicle_hub/camera_mover.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import math as math
import CGF as CGF
from CameraComponents import OrbitComponent as OrbitComponent
from gui.subhangar.subhangar_state_groups import CameraMover as CameraMover
from helpers import dependency as dependency
from math_utils import reduceToPI as reduceToPI
from skeletons.gui.shared.utils import IHangarSpace as IHangarSpace

class VehicleHubCameraMover(CameraMover):
    __hangarSpace: Any
    _moveInstantly: Any
    _transitionDuration: Any
    def __init__(self, transitionDuration):
        ...
    def moveCamera(self, cameraManager, cameraName):
        ...
