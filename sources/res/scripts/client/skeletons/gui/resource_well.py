# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/skeletons/gui/resource_well.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/skeletons/gui/resource_well.py
from __future__ import absolute_import
from typing import Dict, Optional, Set, List
from Event import Event
from skeletons.gui.game_control import IGameController

class IResourceWellController(IGameController):
    onEventUpdated = None
    onSettingsChanged = None
    onNumberRequesterUpdated = None

    @property
    def config(self):
        raise NotImplementedError

    def isEnabled(self):
        raise NotImplementedError

    def isActive(self):
        raise NotImplementedError

    def isStarted(self):
        raise NotImplementedError

    def isFinished(self):
        raise NotImplementedError

    def isPaused(self):
        raise NotImplementedError

    def isNotStarted(self):
        raise NotImplementedError

    def isForbiddenAccount(self):
        raise NotImplementedError

    def isSeasonNumberDefault(self):
        raise NotImplementedError

    def getRewardLimit(self, rewardID):
        raise NotImplementedError

    def getCurrentPoints(self):
        raise NotImplementedError

    def isRewardReceived(self, rewardID):
        raise NotImplementedError

    def getReceivedRewardIDs(self):
        raise NotImplementedError

    def getBalance(self):
        raise NotImplementedError

    def getPurchaseMode(self):
        raise NotImplementedError

    def getRewardVehicle(self, rewardID):
        raise NotImplementedError

    def getRewardStyleID(self, rewardID):
        raise NotImplementedError

    def getCurrentRewardID(self):
        raise NotImplementedError

    def getRewardSequence(self, rewardID):
        raise NotImplementedError

    def getRewardLeftCount(self, rewardID):
        raise NotImplementedError

    def isParentRewardAvailable(self, rewardID):
        raise NotImplementedError

    def isRewardAvailable(self, rewardID):
        raise NotImplementedError

    def isRewardCountAvailable(self, rewardID):
        raise NotImplementedError

    def getAvailableRewards(self):
        raise NotImplementedError

    def isRewardsOver(self):
        raise NotImplementedError

    def isRewardVehicle(self, vehicleCD):
        raise NotImplementedError

    def startNumberRequesters(self):
        raise NotImplementedError

    def stopNumberRequesters(self):
        raise NotImplementedError
