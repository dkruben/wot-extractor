# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/abilities/influence_zones.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import math as math
import CGF as CGF
import Math as Math
import CombatSelectedArea as CombatSelectedArea
import math_utils as math_utils
from typing import List as List
from battle_royale.abilities.area_abilities import AreaAbilityVisualizer as AreaAbilityVisualizer
from cgf_components.marker_component import CombatMarker as CombatMarker
from cgf_script.registration import ComponentProperty as ComponentProperty, registerComponent as registerComponent
from constants import IS_CLIENT as IS_CLIENT
from helpers import dependency as dependency
from items import vehicles as vehicles

class Vehicle(object):
    ...

class InfluenceZone(object):
    ...

class IBattleSessionProvider(object):
    ...

# decorador original: @registerComponent
class InfluenceZoneMultiVisualizer(object):
    editorTitle = 'Influence Zone Multi Visualizer'
    group = 'Abilities'
    domain = CGF.Domain.Client
    influencePrefab: Any
    rotateFromCenter: Any

class ZonePrefabLoader(object):
    __guiSessionProvider: Any
    ALLY_MARKER_POSTFIX = 'Ally'
    ENEMY_MARKER_POSTFIX = 'Enemy'
    influenceZone: Any
    go: Any
    equipment: Any
    __prefabGO: Any
    __loadedPrefabPath: Any
    def __init__(self, influenceZone, go):
        ...
    def activate(self):
        ...
    def deactivate(self):
        ...
    def __multipositionSpawn(self, rootUUID, spaceID, multivisualizer, influenceZone, equipment, _):
        ...
    def __onUpdateObservedVehicleData(self, *args):
        ...
    def __getPrefabPath(self, equipment, zoneTeamID):
        ...
    def __loadGameObject(self, prefabPath):
        ...
    def __removeGameObject(self):
        ...

# decorador original: @registerComponent
class InfluenceZoneTerrainArea(object):
    editorTitle = 'Influence Zone Terrain Area'
    group = 'Abilities'
    domain = CGF.Domain.Client
    fullZoneVisual: Any
    dropOffset: Any
    fullZoneArea: Any
    def __init__(self):
        ...

# decorador original: @registerComponent
class InfluenceZoneEquipmentComponent(object):
    editorTitle = 'Influence Zone Equipment'
    domain = CGF.Domain.Client
    userVisible = False
    radius: Any
    zonesCount: Any
    zoneRadius: Any
    equipment: Any
    def __init__(self):
        ...
    def setupEquipment(self, equipment):
        ...

class InfluenceZoneVisualizationSystem(CGF.System):
    CUT_OFF_ANGLE: Any
    CUT_OFF_DISTANCE = 100
    InfluenceZoneActivated: Any
    TerrainAreaActivated: Any
    TerrainAreaDeactivated: Any
    ZonePrefabLoaderActivated: Any
    ZonePrefabLoaderDeactivated: Any
    Reactions: Any
    def update(self):
        ...
    def onInfluenceZoneSpawn(self, influenceZone, go, queue):
        ...
    def terrainAreaInit(self, transform, influenceZoneEquipment, terrainArea):
        ...
    def terrainAreaDestroy(self, terrainArea):
        ...
