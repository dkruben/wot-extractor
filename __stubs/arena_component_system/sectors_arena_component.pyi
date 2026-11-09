# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client_common/arena_component_system/sectors_arena_component.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import defaultdict as defaultdict
from arena_component_system.client_arena_component_system import ClientArenaComponent as ClientArenaComponent
import Event as Event
from constants import SECTOR_STATE as SECTOR_STATE
from debug_utils import LOG_WARNING as LOG_WARNING
import Math as Math
from epic_constants import EPIC_BATTLE_TEAM_ID as EPIC_BATTLE_TEAM_ID

class SectorGroup(object):
    id: Any
    center: Any
    numSubSectors: Any
    playerGroup: Any
    IDInPlayerGroup: Any
    endOfTransitionPeriod: Any
    sectors: Any
    __id: Any
    __state: Any
    __center: Any
    __sectors: Any
    __bottomLeft: Any
    __upperRight: Any
    __wayPoints: Any
    def __init__(self, sectorGroupId):
        ...
    def destroy(self):
        ...
    def addSector(self, sector):
        ...
    def updateSector(self, sector):
        ...
    def calculateSectorBoundaries(self):
        ...
    def getBound(self):
        ...
    def isInSector(self, position):
        ...
    def getWaypointsForTeam(self, arenaType, team):
        ...
    def getClosestWayPointPosition(self, arenaType, team, position):
        ...
    @property
    def state(self):
        ...
    @state.setter
    def state(self, value):
        ...
    def __getWayPointsForSector(self, arenaType):
        ...

class PlayerGroup(object):
    id: Any
    sectors: Any
    __id: Any
    __sectors: Any
    def __init__(self, groupID):
        ...
    def destroy(self):
        ...
    def addSector(self, sector):
        ...

class SectorsArenaComponent(ClientArenaComponent):
    sectors: Any
    sectorGroups: Any
    playerGroups: Any
    currentPlayerSectorId: Any
    __sectors: Any
    __sectorGroups: Any
    __playerGroups: Any
    __currentPlayerSectorGroupID: Any
    __currentWayPointSector: Any
    __currentPlayerSectorID: Any
    __wayPointRepetitionRules: Any
    onSectorAdded: Any
    onSectorTransitionTimeChanged: Any
    onSectorGroupUpdated: Any
    onSectorGroupTransitionTimeChanged: Any
    onPlayerSectorGroupChanged: Any
    onWaypointsForPlayerActivated: Any
    onWaypointsRepetitionRulesChanged: Any
    def __init__(self, componentSystem):
        ...
    def destroy(self):
        ...
    def addSector(self, sector):
        ...
    def updateSector(self, sector, oldState=None):
        ...
    def updateSectorTransitionTime(self, sector, oldTime, newTime):
        ...
    def removeSector(self, sector):
        ...
    def getSectorById(self, sectorID):
        ...
    def getSectorGroupById(self, sectorGroupID):
        ...
    def getAllSectorsForPlayerGroup(self, playerGroup):
        ...
    def getNeighbouringSectorIdsByOwnSectorId(self, ownSectorId):
        ...
    def getActiveWaypointSectorGroupForPlayer(self):
        ...
    def getActiveWaypointSectorGroupForPlayerGroup(self, playerGroupID):
        ...
    def getClosestWayPointForSectorAndTeam(self, sectorID, arenaType, teamID, position):
        ...
    def playerSectorGroupChanged(self, newSectorGroupID, isAllowed, oldSectorGroupID, wasAllowed, physicalSector):
        ...
    def __activateWaypointsForPlayer(self):
        ...
    def getWayPointBorderMarkerRepetitionRules(self, team):
        ...
    def setWayPointBorderMarkerRepetitionRules(self, teamID, rule):
        ...
