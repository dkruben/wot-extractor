# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/armor_flashlight/config.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import BattleReplay as BattleReplay
import ResMgr as ResMgr
import section2dict as section2dict
from armor_flashlight_common.server_config import serverConfigSchema as serverConfigSchema
from debug_utils import LOG_ERROR as LOG_ERROR
from dict2model import models as models, schemas as schemas, fields as fields, validate as validate
from dict2model.exceptions import ValidationError as ValidationError
from dict2model.extensions.color import ColorModel as ColorModel, colorSchema as colorSchema
from typing import Tuple as Tuple
from Math import Vector4 as Vector4
_CONFIG_PATH = 'gui/armor_flashlight_config.xml'
_DEFAULT_RESOLUTION_INDEX = 0
_config = None
_armorPiercingColorsSchema: Any
_colorSchemaSchema: Any
_patternSchema: Any
_distanceConfigSchema: Any
_resolutionSchema: Any
_defaultResolutionByPostProcessingSchema: Any
_configSchema: Any

class ArmorPiercingColorsSchemaModel(models.Model):
    __slots__: tuple
    notPierced: Any
    littlePierced: Any
    greatPierced: Any
    def __init__(self, notPierced, littlePierced, greatPierced):
        ...
    def toFloats(self):
        ...
    def _reprArgs(self):
        ...

class ColorSchemaModel(models.Model):
    __slots__: tuple
    name: Any
    normal: Any
    colorBlindness: Any
    def __init__(self, name, normal, colorBlindness):
        ...
    def _reprArgs(self):
        ...

class PatternModel(models.Model):
    __slots__: tuple
    name: Any
    texturePath: Any
    def __init__(self, name, texturePath):
        ...
    def _reprArgs(self):
        ...

class DistanceConfigModel(models.Model):
    __slots__: tuple
    distance: Any
    value: Any
    def __init__(self, distance, value):
        ...
    def _reprArgs(self):
        ...
    def getTuple(self):
        ...
    @staticmethod
    def sortedByDist(config):
        ...

class ResolutionModel(models.Model):
    __slots__: tuple
    name: Any
    downscale: Any
    def __init__(self, name, downscale):
        ...
    def _reprArgs(self):
        ...

class DefaultResolutionByPostProcessingModel(models.Model):
    __slots__: tuple
    postProcessingLevel: Any
    maxResolutionName: Any
    def __init__(self, postProcessingLevel, maxResolutionName):
        ...
    def _reprArgs(self):
        ...

class ConfigModel(models.Model):
    __slots__: tuple
    colorSchemas: Any
    patterns: Any
    textureTilingFactor: Any
    alphaByDist: Any
    radiusByDist: Any
    appearanceDurationByDist: Any
    resolutions: Any
    defaultResolutionByPostProcessing: Any
    noiseIntensityMultiplier: Any
    maxSizePercentOfWindow: Any
    fadeoffFactorWhenNotAimed: Any
    borderSmoothness: Any
    aimingCircleAdjustment: Any
    smoothnessInAimingCircleAdjustment: Any
    def __init__(self, colorSchemas, patterns, textureTilingFactor, alphaByDist, radiusByDist, appearanceDurationByDist, resolutions, defaultResolutionByPostProcessing, noiseIntensityMultiplier, maxSizePercentOfWindow, fadeoffFactorWhenNotAimed, borderSmoothness, aimingCircleAdjustment, smoothnessInAimingCircleAdjustment):
        ...
    def getSchemaColorFloatsByIndex(self, index, isColorBlind):
        ...
    def getPatternByIndex(self, index):
        ...
    @staticmethod
    def getDistanceConfigTupleList(config):
        ...
    def getResolutionDownscaleByIndex(self, index):
        ...
    def getResolutionIndexByPostProcessing(self, postProcessingLevel):
        ...
    def _getDefaultResolutionByPostProcessing(self, postProcessingLevel):
        ...
    def _getResolutionIndexByName(self, name):
        ...
    def _reprArgs(self):
        ...

def _validateUniqueNames(items, itemType):
    ...
def _validateColorSchemasNames(config):
    ...
def _validatePatternsNames(config):
    ...
def _validateResolutionNames(config):
    ...
def _validateMaxResolutionNames(config):
    ...
def getConfig():
    ...
def isFeatureEnabled():
    ...
