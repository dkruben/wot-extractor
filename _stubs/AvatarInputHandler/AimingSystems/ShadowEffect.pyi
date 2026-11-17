# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/AvatarInputHandler/AimingSystems/ShadowEffect.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import GUI as GUI
import math_utils as math_utils
from math_common import decimal_round as decimal_round

class ShadowEffect(object):
    __texturePath: Any
    __startPositionX: Any
    __shadowUpInitialPosition: Any
    __shadowDownInitialPosition: Any
    __size: Any
    __shadowUp: Any
    __shadowDown: Any
    cachedPosition: Any
    def __init__(self):
        ...
    def destroy(self):
        ...
    def __spawnShadow(self, position, path, rotateAngle=None):
        ...
    def onGunIndexChanged(self, transitionSide):
        ...
    def spawn(self):
        ...
    def show(self):
        ...
    def hide(self):
        ...
    def move(self, positionX):
        ...
    def update(self, coefficient):
        ...
