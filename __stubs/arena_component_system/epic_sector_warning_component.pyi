# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client_common/arena_component_system/epic_sector_warning_component.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import math as math
import weakref as weakref
from collections import defaultdict as defaultdict
from functools import partial as partial
from future.utils import lmap as lmap, viewitems as viewitems
from math import copysign as copysign
import BigWorld as BigWorld
import Event as Event
from arena_component_system.client_arena_component_system import ClientArenaComponent as ClientArenaComponent
from epic_constants import EPIC_BATTLE_TEAM_ID as EPIC_BATTLE_TEAM_ID
from constants import SECTOR_STATE as SECTOR_STATE
from coordinate_system import AXIS_ALIGNED_DIRECTION as AAD
from debug_utils import LOG_WARNING as LOG_WARNING
from gui.battle_control.avatar_getter import getArena as getArena, getPlayerTeam as getPlayerTeam
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
from Math import Vector2 as Vector2, Vector3 as Vector3
from PlayerEvents import g_playerEvents as g_playerEvents
from epic_constants import SECTOR_EDGE_STATE as SECTOR_EDGE_STATE
from battleground.BorderVisual import BorderVisual as BorderVisual
SECTOR_STATE_TO_MAPPED_STATE: dict
ADJACENT_MAPPED_STATES_TO_EDGE_STATE: dict
MAX_NUM_NODES = 10

class MAPPED_SECTOR_STATE(object):
    GOOD = 0
    BAD = 1

class WARNING_TYPE(object):
    NONE = 0
    SAFE = 1
    BOMBING = 2
    PROTECTED = 3

class _SectorGroupNode(object):
    neighbours: Any
    mappedState: Any
    def __init__(self):
        ...

class _SectorGroupEdge(object):
    state: Any
    start: Any
    end: Any
    def __init__(self):
        ...
    def getEdgePoints(self):
        ...

class _ProtectionZoneSetting(object):
    mappedState: Any
    geometry: Any
    edgeState: Any
    isActive: Any
    team: Any
    def __init__(self):
        ...

class _SectorWarning(object):
    type: Any
    targetSectorGroup: Any
    def __init__(self, warningType, targetNode):
        ...

class EpicSectorWarningComponent(ClientArenaComponent, CallbackDelayer):
    edges: Any
    protectionZones: Any
    warnings: Any
    __sectorComponent: Any
    __playerDataComponent: Any
    __protectionZoneComponent: Any
    __teamId: Any
    __nodes: Any
    __edges: Any
    __protectionZones: Any
    __activeWarnings: Any
    __transitionEndTimes: Any
    __visual: Any
    onShowSectorWarning: Any
    onTransitionTimerUpdated: Any
    def __init__(self, componentSystem):
        ...
    def activate(self):
        ...
    def deactivate(self):
        ...
    def destroy(self):
        ...
    def getEdgeByID(self, edgeID):
        ...
    def getEdgeIdsByNodeId(self, nodeId):
        ...
    def __onAvatarReady(self):
        ...
    def __onSectorAdded(self, sector, sectorGroup):
        ...
    def __onProtectionZoneAdded(self, zoneId, position, bound):
        ...
    def __onProtectionZoneActive(self, zoneId, isActive):
        ...
    def __onPlayerInProtectionZone(self, zoneId, isInZone):
        ...
    def __updateProtectionZone(self, zoneId, isInZone, isZoneActive):
        ...
    def __onPlayerSectorGroupChanged(self, newNodeID, *args):
        ...
    def __showEdgeState(self, edgeId, edge, state, forceUpdate=False):
        ...
    def __showWarning(self, fromNodeId, toNodeId, warningType):
        ...
    def __onSectorGroupUpdated(self, groupId, state, center, bounds):
        ...
    def __calcEdgeLine(self, nodeIdA, nodeIdB):
        ...
    def __getNodeGeometry(self, nodeId):
        ...
    def __onSectorGroupTransitionTimeChanged(self, sectorGroupId, oldTime, newTime):
        ...
    def __startCountdownTimer(self, sectorGroupId):
        ...
    def __tick(self):
        ...

class SectorBorderVisualisation(object):
    _TEAM_BORDER_DIRS: dict
    __sectorVisuals: Any
    __protectionVisuals: Any
    def __init__(self, sectorWarningComponent):
        ...
    def destroy(self):
        ...
    def showSectorBorder(self, edgeId, edgeState, edges):
        ...
    def showProtectionZone(self, zoneId, edgeState, owningTeam, protectionZones):
        ...

def makeEdgeId(a, b):
    ...
def decomposeEdgeId(edgeId):
    ...
