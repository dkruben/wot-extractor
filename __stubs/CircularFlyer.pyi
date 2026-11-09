# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/CircularFlyer.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import math as math
import BigWorld as BigWorld
import AnimationSequence as AnimationSequence
from Math import Matrix as Matrix, Vector3 as Vector3
from debug_utils import LOG_CURRENT_EXCEPTION as LOG_CURRENT_EXCEPTION
from vehicle_systems.stricted_loading import makeCallbackWeak as makeCallbackWeak
import SoundGroups as SoundGroups

class CircularFlyer(BigWorld.UserDataObject):
    __prevTime: Any
    __angularVelocity: Any
    __currentAngle: Any
    __updateCallbackId: Any
    __model: Any
    __modelMatrix: Any
    __sound: Any
    __animator: Any
    def __init__(self):
        ...
    def __del__(self):
        ...
    def __clear(self):
        ...
    def __onResourcesLoaded(self, resourceRefs):
        ...
    def __update(self):
        ...
