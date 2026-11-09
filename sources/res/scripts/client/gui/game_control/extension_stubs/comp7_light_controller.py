# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/game_control/extension_stubs/comp7_light_controller.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/game_control/extension_stubs/comp7_light_controller.py
from __future__ import absolute_import
import Event
from skeletons.gui.game_control import IComp7LightController
from gui.periodic_battles.models import PrimeTimeStatus

class Comp7LightController(IComp7LightController):

    def __init__(self):
        super(Comp7LightController, self).__init__()
        self.__eventsManager = em = Event.EventManager()
        self.onStatusUpdated = Event.Event(em)
        self.onStatusTick = Event.Event(em)
        self.onComp7LightConfigChanged = Event.Event(em)

    @property
    def isBanned(self):
        return False

    @property
    def isOffline(self):
        return False

    @property
    def battleModifiers(self):
        return ()

    def fini(self):
        self.__eventsManager.clear()
        super(Comp7LightController, self).fini()

    def isBattlesPossible(self):
        return False

    def isInPrimeTime(self):
        return False

    def isNotSet(self, now=None, peripheryID=None):
        return True

    def isWithinSeasonTime(self, seasonID):
        return False

    def hasAnySeason(self):
        return False

    def hasAvailablePrimeTimeServers(self, now=None):
        return False

    def hasConfiguredPrimeTimeServers(self, now=None):
        return False

    def hasPrimeTimesLeftForCurrentCycle(self):
        return False

    def hasPrimeTimesPassedForCurrentCycle(self):
        return False

    def getClosestStateChangeTime(self, now=None):
        return 0

    def getCurrentCycleID(self):
        return

    def getCurrentCycleInfo(self):
        return (
         None, False)

    def getCurrentSeason(self, now=None, includePreannounced=False):
        return

    def getCurrentOrNextActiveCycleNumber(self, season):
        return 0

    def getEventEndTimestamp(self):
        return

    def getModeSettings(self):
        return

    def getNextSeason(self, now=None):
        return

    def getPeriodInfo(self, now=None, peripheryID=None):
        return

    def getPrimeTimes(self):
        return {}

    def getPrimeTimesForDay(self, selectedTime, groupIdentical=False):
        return {}

    def getPrimeTimeStatus(self, now=None, peripheryID=None):
        return (PrimeTimeStatus.NOT_SET, 0, False)

    def getPreviousSeason(self, now=None):
        return

    def getSeason(self, seasonID):
        return

    def getSeasonsPassed(self, now=None):
        return []

    def getAllSeasons(self):
        return []

    def getTimer(self, now=None, peripheryID=None):
        return 0

    def getLeftTimeToPrimeTimesEnd(self, now=None):
        return 0

    def getQuestsTimerLeft(self):
        return 0

    def isEnabled(self):
        return False

    def isFrozen(self):
        return True

    def isAvailable(self):
        return False

    def isSuitableVehicle(self, vehicle):
        return False

    def hasSuitableVehicles(self):
        return False

    def isModePrbActive(self):
        return False

    def isProgressionActive(self):
        return False

    def vehicleIsAvailableForBuy(self):
        return False

    def vehicleIsAvailableForRestore(self):
        return False

    def getPreannouncedSeason(self):
        return

    def getRoleEquipmentKey(self, vehType):
        return ''

    def getRoleEquipment(self, roleName):
        return

    def getEquipmentStartLevel(self, roleName):
        return

    def getRoleEquipmentOverrides(self, roleName):
        return

    def getPoiEquipmentOverrides(self, poiName):
        return

    def isBattleModifiersAvailable(self):
        return False
