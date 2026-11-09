# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/hangar_config.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import math as math
from Math import Vector3 as Vector3
from items.components import component_constants as component_constants

class HangarConfig(object):
    __slots__: list
    cfg: Any
    vStartAngles: Any
    vStartPos: Any
    emblemsAlphaDamaged: Any
    emblemsAlphaUndamaged: Any
    shadowLightDir: Any
    shadowModelName: Any
    shadowForwardYOffset: Any
    shadowDeferredYOffset: Any
    shadowDefaultTextureName: Any
    shadowEmptyTextureName: Any
    vehicleGunPitch: Any
    vehicleTurretYaw: Any
    camMinDistVehicleHullLengthK: Any
    pivotTransform: Any
    camCapsuleScale: Any
    camCapsuleGunScale: Any
    cameraName: Any
    translation: Any
    def __init__(self):
        ...
    def __iter__(self):
        ...
    def __getitem__(self, key):
        ...
    def __setitem__(self, key, value):
        ...
    def get(self, key, default=None):
        ...
    def loadConfig(self, xml, defaultCfg=None):
        ...
    def loadDefaultHangarConfig(self, xml, hangarPathKey):
        ...
    def loadCustomizationConfig(self, xml):
        ...
    def loadSecondaryConfig(self, xml):
        ...
    def loadConfigValue(self, name, xml, fn, defaultCfg=None):
        ...
