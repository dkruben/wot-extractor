# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/hangar_cameras/hangar_camera_yaw_filter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import math as math
import math_utils as math_utils
_EPS = 0.001

class HangarCameraYawFilter(object):
    __offset: Any
    __length: Any
    __cycled: Any
    __camSens: Any
    __prevDirection: Any
    def __init__(self, start, length, camSens):
        ...
    def toLimit(self, inAngle):
        ...
    def getNextYaw(self, currentYaw, targetYaw, delta):
        ...
    def __normalize(self, angle):
        ...
    def __refresh(self, angle):
        ...
