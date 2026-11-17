# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/AvatarInputHandler/AimingSystems/magnetic_aim.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import math as math
from collections import namedtuple as namedtuple
from itertools import chain as chain
import BigWorld as BigWorld
from Math import Vector3 as Vector3, Matrix as Matrix
import math_utils as math_utils
_TargetVeh: Any

class MagneticAimSettings(object):
    MAGNETIC_ANGLE = 2.25
    KEY_DELAY_SEC = 0.5
    @staticmethod
    def getMagneticAngle():
        ...

def magneticAimProcessor(previousSimpleTarget=None, previousMagneticTarget=None):
    ...
def magneticAimFindTarget():
    ...
def getVehiclePointsGen(vehicle):
    ...
def getVisibilityCheckPointsGen(vehicle):
    ...
def isVehicleVisibleFromCamera(vehicle, aimCamera):
    ...
