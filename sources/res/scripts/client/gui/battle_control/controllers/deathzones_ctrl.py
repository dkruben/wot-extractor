# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/battle_control/controllers/deathzones_ctrl.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/battle_control/controllers/deathzones_ctrl.py
from __future__ import absolute_import
from collections import namedtuple
from future.utils import viewvalues
import BigWorld
from gui.battle_control.arena_info.interfaces import IArenaLoadController
from gui.battle_control.battle_constants import BATTLE_CTRL_ID
_TimersData = namedtuple('_TimersData', 'timeToStrike waveDuration')

class DeathZonesController(IArenaLoadController):

    def __init__(self):
        self.__timersData = {}
        self.__timeToStrikeInCurrentNotification = None
        self.__playerEnterZone = False
        return

    def startControl(self, battleCtx, arenaVisitor):
        pass

    def stopControl(self):
        pass

    def getControllerID(self):
        return BATTLE_CTRL_ID.DEATHZONES

    def updateDeathZoneWarningNotification(self, zoneId, show, timeToStrike, waveDuration):
        if show:
            self.__timersData[zoneId] = _TimersData(timeToStrike, waveDuration)
        elif zoneId in self.__timersData:
            self.__timersData.pop(zoneId)
        player = BigWorld.player()
        vehicle = player.vehicle if player else None
        if not vehicle:
            return
        else:
            if self.__timersData and vehicle.isAlive():
                closestStrikeData = min(viewvalues(self.__timersData), key=(lambda timersData: timersData.timeToStrike))
                if closestStrikeData.timeToStrike != self.__timeToStrikeInCurrentNotification:
                    player.updateDeathZoneWarningNotification(True, not self.__playerEnterZone, closestStrikeData.timeToStrike, closestStrikeData.waveDuration)
                    self.__timeToStrikeInCurrentNotification = closestStrikeData.timeToStrike
                self.__playerEnterZone = True
            else:
                player.updateDeathZoneWarningNotification(False, False, 0, 0)
                self.__timeToStrikeInCurrentNotification = None
                self.__playerEnterZone = False
            return
