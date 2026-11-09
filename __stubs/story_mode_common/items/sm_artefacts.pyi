# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/common/story_mode_common/items/sm_artefacts.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from items.artefacts import Equipment as Equipment, AreaOfEffectEquipment as AreaOfEffectEquipment, TooltipConfigReader as TooltipConfigReader, ArcadeEquipmentConfigReader as ArcadeEquipmentConfigReader, AreaMarkerConfigReader as AreaMarkerConfigReader
from items.components import component_constants as component_constants
from items import _xml as _xml
from soft_exception import SoftException as SoftException
from ResMgr import DataSection as DataSection
from Math import Vector3 as Vector3

class SPGZoneEquipment(AreaOfEffectEquipment):
    __slots__: tuple
    yawHitPrediction: Any
    hitPredictionDuration: Any
    def _readConfig(self, xmlCtx, scriptSection):
        ...

class NavmeshSettingsReader(object):
    _SLOTS: tuple
    navmeshGirth: Any
    navmeshHeightTolerance: Any
    def initNavmeshConfig(self):
        ...
    def readNavmeshConfig(self, xmlCtx, section):
        ...

class AOENavmeshEquipment(AreaOfEffectEquipment, NavmeshSettingsReader):
    __slots__ = NavmeshSettingsReader._SLOTS
    def __init__(self):
        ...
    def _readConfig(self, xmlCtx, scriptSection):
        ...

class BaseAbilityEquipment(Equipment, TooltipConfigReader, ArcadeEquipmentConfigReader, AreaMarkerConfigReader, NavmeshSettingsReader):
    __slots__: Any
    prepareTime: Any
    respawnTime: Any
    cooldownTime: Any
    unspotDelay: Any
    directVisionRadius: Any
    visionMinRadius: Any
    detectFromVehicle: Any
    observationPoints: Any
    def __init__(self):
        ...
    def _readConfig(self, xmlCtx, scriptSection):
        ...
    @staticmethod
    def _readPointList(xmlCtx, section):
        ...

class ReconAbilityEquipment(BaseAbilityEquipment):
    activatingTime: Any
    deactivatingTime: Any
    def _readConfig(self, xmlCtx, scriptSection):
        ...

class DistractionAbilityEquipment(BaseAbilityEquipment):
    pointRadius: Any
    detectTime: Any
    autoDestroyTime: Any
    changeBrainDelay: Any
    investigateTime: Any
    showXrayMarker: Any
    detectSequence: Any
    def _readConfig(self, xmlCtx, scriptSection):
        ...
