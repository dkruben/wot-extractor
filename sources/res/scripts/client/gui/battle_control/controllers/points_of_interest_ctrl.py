# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/battle_control/controllers/points_of_interest_ctrl.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/battle_control/controllers/points_of_interest_ctrl.py
from __future__ import absolute_import
import logging, typing, BigWorld, CGF, Event
from gui.battle_control.arena_info.interfaces import IPointsOfInterestController
from gui.battle_control.battle_constants import BATTLE_CTRL_ID
from points_of_interest.managers import PoiStateUpdateSystem
from shared_utils import findFirst
if typing.TYPE_CHECKING:
    from EmptyEntity import EmptyEntity
    from gui.battle_control.controllers.repositories import BattleSessionSetup
    from points_of_interest.components import PoiStateComponent
_logger = logging.getLogger(__name__)

class PointsOfInterestController(IPointsOfInterestController):

    def __init__(self, setup):
        super(PointsOfInterestController, self).__init__()
        self.__eManager = Event.EventManager()
        self.onPoiEquipmentUsed = Event.Event(self.__eManager)
        self.onPoiCaptured = Event.Event(self.__eManager)
        self.onPoiInvaderDestroyed = Event.Event(self.__eManager)
        self.__vehPoiRegistry = {}

    def startControl(self):
        _logger.debug('[POI] PointsOfInterestController started.')

    def stopControl(self):
        _logger.debug('[POI] PointsOfInterestController stopped.')
        self.__vehPoiRegistry.clear()
        self.__eManager.clear()

    def getControllerID(self):
        return BATTLE_CTRL_ID.POINTS_OF_INTEREST_CTRL

    @staticmethod
    def getPoiState(poiID):
        poiStateSystem = CGF.getSystem(BigWorld.player().spaceID, PoiStateUpdateSystem)
        states = poiStateSystem.getStates()
        return findFirst((lambda s: s.id == poiID), states)

    @staticmethod
    def getPoiEntity(poiID):
        return BigWorld.entities.get(poiID)

    def getVehicleCapturingPoiGO(self, poiName, entityGameObject, vehicleID, spaceID):
        poiGameObject = self.__vehPoiRegistry.get(vehicleID, {}).get(poiName)
        if poiGameObject is None or not poiGameObject.valid:
            queue = CGF.CommandQueue(spaceID)
            poiGameObject = queue.createGameObject(poiName)
            self.__vehPoiRegistry.setdefault(vehicleID, {})[poiName] = poiGameObject
            if entityGameObject:
                queue.createComponent(poiGameObject, CGF.HierarchyComponent, entityGameObject)
            queue.activateGameObject(poiGameObject)
        return poiGameObject
