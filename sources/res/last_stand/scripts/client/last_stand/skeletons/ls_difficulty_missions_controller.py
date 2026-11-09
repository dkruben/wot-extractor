# wot-extractor: codigo DESCOMPILADO de sources/res/last_stand/scripts/client/last_stand/skeletons/ls_difficulty_missions_controller.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: last_stand/scripts/client/last_stand/skeletons/ls_difficulty_missions_controller.py
from __future__ import absolute_import
import typing
from skeletons.gui.game_control import IGameController
if typing.TYPE_CHECKING:
    from last_stand.gui.game_control.ls_difficulty_missions_controller import DifficultyMission
    from gui.server_events.bonuses import SimpleBonus

class ILSDifficultyMissionsController(IGameController):
    onDifficultyMissionsStatusUpdated = None

    def isEnabled(self):
        raise NotImplementedError

    def missionsSorted(self, difficulty):
        raise NotImplementedError

    def isProgressCompleted(self):
        raise NotImplementedError

    def getMission(self, missionID):
        raise NotImplementedError

    def getMissionsCount(self, difficulty):
        raise NotImplementedError

    def getCompletedMissionsIndexByDifficulty(self, difficulty):
        raise NotImplementedError

    def getIndexes(self, missionID):
        raise NotImplementedError

    def getMissionByIndex(self, difficulty, index):
        raise NotImplementedError

    def getMissionIDByIndex(self, difficulty, index):
        raise NotImplementedError

    def getAggregatedMissionRewards(self, difficulty):
        raise NotImplementedError

    def addArenaIDToCache(self, arenaID):
        raise NotImplementedError

    def isArenaIDInCache(self, arenaID):
        raise NotImplementedError
