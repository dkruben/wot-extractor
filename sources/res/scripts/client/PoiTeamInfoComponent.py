# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/PoiTeamInfoComponent.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/PoiTeamInfoComponent.py
from __future__ import absolute_import
import logging, typing
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS
from script_component.ScriptComponent import ScriptComponent
from helpers import dependency
from items import vehicles
from skeletons.gui.battle_session import IBattleSessionProvider
if typing.TYPE_CHECKING:
    from gui.battle_control.arena_info.interfaces import IPointsOfInterestController
_logger = logging.getLogger(__name__)

class PoiTeamInfoComponent(ScriptComponent):
    REQUIRED_BONUS_CAP = ARENA_BONUS_TYPE_CAPS.POINTS_OF_INTEREST

    def __init__(self):
        super(PoiTeamInfoComponent, self).__init__()
        self.__sessionProvider = dependency.instance(IBattleSessionProvider)

    def onEnterWorld(self, _):
        _logger.debug('PoiTeamInfoComponent.onEnterWorld. TeamID=%s', self.entity.teamID)

    def onLeaveWorld(self):
        _logger.debug('PoiTeamInfoComponent.onLeaveWorld. TeamID=%s', self.entity.teamID)

    def onPoiEquipmentUsed(self, vehicleID, equipmentID):
        equipment = vehicles.g_cache.equipments().get(equipmentID)
        if equipment is None:
            _logger.error('Equipment %s does not exist', equipmentID)
            return
        else:
            poiCtrl = self.__sessionProvider.dynamic.pointsOfInterest
            if poiCtrl is not None:
                poiCtrl.onPoiEquipmentUsed(equipment, vehicleID)
            return

    def onPoiCaptured(self, poiID, vehicleID):
        poiCtrl = self.__sessionProvider.dynamic.pointsOfInterest
        if poiCtrl is not None:
            poiCtrl.onPoiCaptured(poiID, vehicleID)
        return

    def onPoiInvaderDestroyed(self, vehicleID):
        poiCtrl = self.__sessionProvider.dynamic.pointsOfInterest
        if poiCtrl is not None:
            poiCtrl.onPoiInvaderDestroyed(vehicleID)
        return
