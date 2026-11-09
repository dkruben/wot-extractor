# wot-extractor: codigo DESCOMPILADO de sources/res/last_stand/scripts/client/last_stand/gui/battle_control/controllers/hit_direction_ctrl/ls_ctrl.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: last_stand/scripts/client/last_stand/gui/battle_control/controllers/hit_direction_ctrl/ls_ctrl.py
from __future__ import absolute_import
from gui.battle_control.controllers.hit_direction_ctrl.ctrl import HitDirectionController
from gui.battle_control.controllers.hit_direction_ctrl.hit_data import HitData
from gui.battle_control.controllers.hit_direction_ctrl.base import HitType
from last_stand.gui.ls_vehicle_role_helper import getVehicleRole
from last_stand_common.last_stand_constants import LS_ROLE_PREFIX

class LSHitDirectionController(HitDirectionController):

    def addHit(self, hitDirYaw, attackerID, damage, isBlocked, critFlags, isHighExplosive, damagedID, attackReasonID):
        arenaDP = self._HitDirectionController__arenaDP
        atackerVehInfo = arenaDP.getVehicleInfo(attackerID)
        atackerVehType = atackerVehInfo.vehicleType
        atackerVehName = atackerVehType.shortNameWithPrefix
        isAlly = arenaDP.isAllyTeam(atackerVehInfo.team)
        playerVehType = arenaDP.getVehicleInfo(damagedID).vehicleType
        classTag = atackerVehType.classTag
        role = getVehicleRole(atackerVehType)
        if role:
            classTag = LS_ROLE_PREFIX + role
        if atackerVehInfo.isEnemy():
            atackerVehName = atackerVehType.name
        hitData = HitData(yaw=hitDirYaw, attackerID=attackerID, isAlly=isAlly, damage=damage, attackerVehName=atackerVehName, isBlocked=isBlocked, attackerVehClassTag=classTag, critFlags=critFlags, playerVehMaxHP=playerVehType.maxHealth, isHighExplosive=isHighExplosive, attackReasonID=attackReasonID, friendlyFireMode=self._HitDirectionController__isFriendlyFireMode())
        uiHitComponents = self._HitDirectionController__uiHitComponents
        return uiHitComponents[HitType.HIT_DAMAGE].pull.addHit(hitData)


class LSHitDirectionControllerPlayer(LSHitDirectionController):

    def stopControl(self):
        self._hideAllHits()
        super(LSHitDirectionControllerPlayer, self).stopControl()
