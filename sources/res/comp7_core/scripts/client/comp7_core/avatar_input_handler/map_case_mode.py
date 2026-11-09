# wot-extractor: codigo DESCOMPILADO de sources/res/comp7_core/scripts/client/comp7_core/avatar_input_handler/map_case_mode.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7_core/scripts/client/comp7_core/avatar_input_handler/map_case_mode.py
from __future__ import absolute_import
import logging, BigWorld
from Math import Vector2
from AvatarInputHandler.MapCaseMode import _ArenaBoundArtilleryStrikeSelector, _DEFAULT_STRIKE_DIRECTION
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider
_logger = logging.getLogger(__name__)

class Comp7ArenaBoundArtilleryStrikeSelector(_ArenaBoundArtilleryStrikeSelector):
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self, position, equipment, direction=_DEFAULT_STRIKE_DIRECTION):
        super(Comp7ArenaBoundArtilleryStrikeSelector, self).__init__(position, equipment, direction)
        equipmentCtrl = self.__sessionProvider.shared.equipments
        if equipmentCtrl is not None:
            equipmentCtrl.onRoleEquipmentStateChanged += self.__onRoleEquipmentStateChanged
        return

    def destroy(self):
        super(Comp7ArenaBoundArtilleryStrikeSelector, self).destroy()
        equipmentCtrl = self.__sessionProvider.shared.equipments
        if equipmentCtrl is not None:
            equipmentCtrl.onRoleEquipmentStateChanged -= self.__onRoleEquipmentStateChanged
        return

    def _getAreaSize(self):
        radius = self._getRadius()
        return Vector2(radius * 2, radius * 2)

    def _getRadius(self):
        equipmentCtrl = self.__sessionProvider.shared.equipments
        level = equipmentCtrl.getRoleEquipmentState().level
        return self.equipment.getRadiusBasedOnSkillLevel(level)

    def __onRoleEquipmentStateChanged(self, state, previousState=None):
        if state is None or previousState is None:
            return
        if state.level > previousState.level:
            if self.area is not None:
                self.area.updateSize(self._getAreaSize())
        return


class Comp7ArenaBoundPlaneStrikeSelector(Comp7ArenaBoundArtilleryStrikeSelector):

    def __init__(self, position, equipment):
        player = BigWorld.player()
        arenaType = player.arena.arenaType
        reconSettings = getattr(arenaType, 'recon')
        direction = None
        if reconSettings is not None:
            direction = reconSettings.flyDirections.get(player.team)
        if direction is None:
            _logger.error('Missing flyDirection for arena [geometryName=%s, gameplayName=%s]; teamID=%s', arenaType.geometryName, arenaType.gameplayName, player.team)
            direction = _DEFAULT_STRIKE_DIRECTION
        super(Comp7ArenaBoundPlaneStrikeSelector, self).__init__(position, equipment, direction)
        return


class Comp7PoiArtilleryStrikeSelector(_ArenaBoundArtilleryStrikeSelector):

    def _getAreaSize(self):
        radius = self._getRadius()
        return Vector2(radius * 2, radius * 2)

    def _getRadius(self):
        return self.equipment.radius


class Comp7PoiIlluminationFlareStrikeSelector(_ArenaBoundArtilleryStrikeSelector):

    def _getAreaSize(self):
        radius = self._getRadius()
        return Vector2(radius * 2, radius * 2)

    def _getRadius(self):
        return self.equipment.startRadius
