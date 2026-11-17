# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/dyn_objects_cache.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from collections import namedtuple as namedtuple
from future.utils import viewvalues as viewvalues, viewitems as viewitems
import BigWorld as BigWorld
import CGF as CGF
import resource_helper as resource_helper
from constants import ARENA_GUI_TYPE as ARENA_GUI_TYPE
from gui.shared.system_factory import registerDynObjCache as registerDynObjCache, collectDynObjCache as collectDynObjCache
from gui.shared.utils.graphics import isRendererPipelineDeferred as isRendererPipelineDeferred
from items.components.component_constants import ZERO_FLOAT as ZERO_FLOAT
from shared_utils import first as first
from skeletons.dynamic_objects_cache import IBattleDynamicObjectsCache as IBattleDynamicObjectsCache
from vehicle_systems.stricted_loading import makeCallbackWeak as makeCallbackWeak
_CONFIG_PATH = 'scripts/dynamic_objects.xml'
_logger: Any
_ScenariosEffect: Any
_DropPlane: Any
_AirDrop: Any
_Loot: Any
_MinesEffects: Any
_BerserkerEffects: Any
MIN_OVER_TERRAIN_HEIGHT = 0
MIN_UPDATE_INTERVAL = 0
_TerrainCircleSettings: Any
_COMMON_FEATURES_CONF_STORAGES: tuple

class _SimpleEffect(object):
    _SECTION_NAME = None
    effectDescr: Any
    def __init__(self, dataSection):
        ...

class _TeamRelatedEffect(object):
    _ENEMY_SUB_NAME = 'enemy'
    _ALLY_SUB_NAME = 'ally'
    _SECTION_NAME = None
    ally: Any
    enemy: Any
    def __init__(self, dataSection):
        ...

class _BattleRoyaleTrapPointEffect(object):
    _SECTION_NAME = 'TrapPoint'
    vehicleEffect: Any
    def __init__(self, dataSection):
        ...

class _BattleRoyaleRepairPointEffect(_TeamRelatedEffect):
    _SECTION_NAME = 'RepairPoint'

class _BattleRoyaleBotDeliveryEffect(_TeamRelatedEffect):
    _SECTION_NAME = 'BotDeliveryEffect'

class _BattleRoyaleBotClingDeliveryEffect(_TeamRelatedEffect):
    _SECTION_NAME = 'BotClingDeliveryEffect'

class _BattleRoyaleBotDeliveryMarkerArea(_TeamRelatedEffect):
    _SECTION_NAME = 'BotDeliveryArea'

class _MinesPlantEffect(_SimpleEffect):
    _SECTION_NAME = 'minesPlantEffect'

class _MinesIdleEffect(_TeamRelatedEffect):
    _SECTION_NAME = 'minesIdleEffect'

class _EpicMinesIdleEffect(_TeamRelatedEffect):
    _SECTION_NAME = 'epicMinesIdleEffect'

class _MinesDestroyEffect(_SimpleEffect):
    _SECTION_NAME = 'minesDestroyEffect'

class _VehicleUpgradeEffect(_SimpleEffect):
    _SECTION_NAME = 'VehicleUpgrade'

class _KamikazeActivatedEffect(_SimpleEffect):
    _SECTION_NAME = 'KamikazeActivated'

class _BerserkerHullEffect(_SimpleEffect):
    _SECTION_NAME = 'berserkerHullEffect'

class _BerserkerTurretEffect(_SimpleEffect):
    _SECTION_NAME = 'berserkerTurretEffect'

class _PrefabsReader(object):
    _SECTION_NAME = None
    prefabs: Any
    __prefabs: Any
    def __init__(self, dataSection):
        ...

class _VehicleRespawnEffects(_PrefabsReader):
    _SECTION_NAME = 'VehicleRespawn'

class _StPatrickLootEffect(_PrefabsReader):
    _SECTION_NAME = 'StPatrickLootEffect'

class _FireCircleEffects(_PrefabsReader):
    _SECTION_NAME = 'FireCircleEffect'

class DynObjectsBase(object):
    _initialized: Any
    def __init__(self):
        ...
    def init(self, dataSection):
        ...
    def clear(self):
        ...
    def destroy(self):
        ...
    def getInspiringEffect(self):
        ...
    def getHealPointEffect(self):
        ...
    def getAimingCircleRestrictionEffect(self, equipment):
        ...

class _CommonForBattleRoyaleAndEpicBattleDynObjects(DynObjectsBase):
    __inspiringEffect: Any
    __healPointEffect: Any
    def __init__(self):
        ...
    def init(self, dataSection):
        ...
    def getInspiringEffect(self):
        ...
    def getHealPointEffect(self):
        ...
    @property
    def _healPointKey(self):
        ...
    def clear(self):
        ...
    def destroy(self):
        ...

class _StrongholdDynObjects(DynObjectsBase):
    __inspiringEffect: Any
    def __init__(self):
        ...
    def init(self, dataSection):
        ...
    def getInspiringEffect(self):
        ...

class _EpicBattleDynObjects(_CommonForBattleRoyaleAndEpicBattleDynObjects):
    __minesEffects: Any
    def __init__(self):
        ...
    def init(self, dataSection):
        ...
    def getMinesEffect(self):
        ...

class _BattleRoyaleDynObjects(_CommonForBattleRoyaleAndEpicBattleDynObjects):
    __vehicleUpgradeEffect: Any
    __kamikazeActivatedEffect: Any
    __trapPoint: Any
    __repairPoint: Any
    __botDeliveryEffect: Any
    __botClingDeliveryEffect: Any
    __vehicleRespawnEffects: Any
    __stPatrickLootEffect: Any
    __botDeliveryMarker: Any
    __dropPlane: Any
    __airDrop: Any
    __loots: Any
    __minesEffects: Any
    __berserkerEffects: Any
    __fireCircleEffects: Any
    __resourcesCache: Any
    def __init__(self):
        ...
    def init(self, dataSection):
        ...
    def getVehicleUpgradeEffect(self):
        ...
    def getKamikazeActivatedEffect(self):
        ...
    def getTrapPointEffect(self):
        ...
    def getRepairPointEffect(self):
        ...
    def getBotDeliveryEffect(self):
        ...
    def getBotClingDeliveryEffect(self):
        ...
    def getBotDeliveryMarker(self):
        ...
    def getDropPlane(self):
        ...
    def getAirDrop(self):
        ...
    def getLoots(self):
        ...
    def getMinesEffect(self):
        ...
    def getBerserkerEffects(self):
        ...
    def getVehicleRespawnEffect(self):
        ...
    def getStPatrickLootEffect(self):
        ...
    def clear(self):
        ...
    def destroy(self):
        ...
    @property
    def _healPointKey(self):
        ...
    def __onResourcesLoaded(self, resourceRefs):
        ...

class _SpawnPointsConfig(object):
    __size: Any
    __visualsPath: Any
    __colors: Any
    __overTerrainHeight: Any
    def __init__(self, size, visualsPath, colors, overTerrainHeight):
        ...
    @property
    def size(self):
        ...
    @property
    def overTerrainHeight(self):
        ...
    def getColor(self, isMyOwn, isConfirmed):
        ...
    def getVisualPath(self, positionNumber):
        ...
    @classmethod
    def createFromXML(cls, section):
        ...
    @staticmethod
    def __readVisualsPath(section):
        ...
    @staticmethod
    def __readColors(section):
        ...

class _PointsOfInterestConfig(object):
    __prefabs: Any
    def __init__(self, prefabs):
        ...
    def getPointOfInterestPrefab(self, radius):
        ...
    def getPrefabs(self):
        ...
    @classmethod
    def createFromXML(cls, section):
        ...

class _FeatureDynObjects(DynObjectsBase):
    _ROOT_SECTION_NAME = ''
    __cachedPrefabs: Any
    def __init__(self):
        ...
    def init(self, dataSection):
        ...
    def _init(self, dataSection):
        ...
    def clear(self):
        ...
    def destroy(self):
        ...

class _KillCamEffectDynObjects(_FeatureDynObjects):
    CONFIG_NAME = 'KillCamEffectDynObjects'
    _ROOT_SECTION_NAME = 'killCameraVisualEffects'
    emptyGO: Any
    cone: Any
    impactPoint: Any
    spacedArmorLinePoint: Any
    explosionSphere: Any
    spacedArmorImpactPoint: Any
    trajectoryRed: Any
    trajectoryGradient: Any
    def __init__(self):
        ...
    def _init(self, dataSection):
        ...

class BattleDynamicObjectsCache(IBattleDynamicObjectsCache):
    __gameModeConfigStorage: Any
    __featuresConfigStorage: Any
    def __init__(self):
        ...
    def getConfig(self, arenaType):
        ...
    def getFeaturesConfig(self, feature):
        ...
    def load(self, arenaType):
        ...
    def unload(self, arenaType):
        ...
    def destroy(self):
        ...

def _createScenarioEffect(section, path):
    ...
def _addPrecacheCandidate(prerequisites, modelName):
    ...
def _createDropPlane(section, prerequisites):
    ...
def _createAirDrop(section, prerequisites):
    ...
def _createLoots(dataSection, typeSection):
    ...
def createTerrainCircleSettings(section):
    ...
def _parseEffectSubsection(dataSection, sectionKey):
    ...
