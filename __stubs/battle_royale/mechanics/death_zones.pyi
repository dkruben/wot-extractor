# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/mechanics/death_zones.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
import CGF as CGF
import Math as Math
import BigWorld as BigWorld
from death_zones_helpers import ZONE_STATE as ZONE_STATE, idxFrom as idxFrom, zoneIdFrom as zoneIdFrom, ZONES_SIZE as ZONES_SIZE
from constants import IS_CLIENT as IS_CLIENT
from cgf_script.registration import ComponentProperty as ComponentProperty, registerComponent as registerComponent
from gui.shared import g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from battle_royale.gui.shared.events import DeathZoneEvent as DeathZoneEvent
_INVISIBLE_RIGHT = 1
_INVISIBLE_LEFT = 2
_INVISIBLE_UP = 4
_INVISIBLE_DOWN = 8
_UPDATE_PERIOD = 0.1
DeathZoneWallParameters: Any

class ArenaInfoDeathZonesComponent(object):
    ...

# decorador original: @registerComponent
class DeathZoneComponentSettings(object):
    category = 'Steel Hunter'
    editorTitle = 'Death Zones Mechanics Rule'
    domain = CGF.Domain.Client
    activeEnableCenter: Any
    activeMaxAlpha: Any
    activeCentarAlpha: Any
    activeWallHeight: Any
    activeCenterHeight: Any
    activeGroundLineHeight: Any
    activeGroundLineAlpha: Any
    activeColor: Any
    waitingEnableCenter: Any
    waitingMaxAlpha: Any
    waitingCentarAlpha: Any
    waitingWallHeight: Any
    waitingCenterHeight: Any
    waitingGroundLineHeight: Any
    waitingGroundLineAlpha: Any
    waitingColor: Any

class DeathZoneDrawSystem(CGF.System):
    DeathZonesIterate: Any
    SettingsCreate: Any
    Reactions: Any
    activeWall: Any
    waitingWall: Any
    __hashedBoundingBox: Any
    _cornerPosition: Any
    _zoneSizeX: Any
    _zoneSizeY: Any
    _zonePositionOffset: Any
    _zoneScale: Any
    def commonUpdate(self):
        ...
    def periodUpdate(self):
        ...
    def __init__(self):
        ...
    def onMappingLoaded(self):
        ...
    def onProcess(self, zone):
        ...
    def _updateZones(self, deathZones):
        ...
    def _drawZones(self, zoneID, deathZones):
        ...
    def _setBoundsVisibility(self, x, y, state, deathZones):
        ...
    def _checkSide(self, x, y, mask, state, deathZones):
        ...
    def __getBoundingBox(self):
        ...
