# wot-extractor: codigo DESCOMPILADO de sources/res/story_mode/scripts/client/story_mode/gui/impl/lobby/difficulty_hint_checker.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: story_mode/scripts/client/story_mode/gui/impl/lobby/difficulty_hint_checker.py
from __future__ import absolute_import
from helpers import dependency
from shared_utils import first
from story_mode.skeletons.story_mode_controller import IStoryModeController
from story_mode_common.story_mode_constants import MissionType, MissionLockCondition

class DifficultyHintChecker(object):

    def check(self, _):
        storyModeCtrl = dependency.instance(IStoryModeController)
        for mission in storyModeCtrl.filterMissions(missionType=MissionType.EVENT):
            if mission.missionLocker is not None and mission.missionLocker.active == MissionLockCondition.BY_MISSION:
                lockingMission = storyModeCtrl.missions.getMission(mission.missionLocker.byMission.missionId)
                firstTask = first(lockingMission.tasks) if lockingMission is not None else None
                if firstTask is not None and storyModeCtrl.isMissionTaskCompleted(lockingMission.missionId, firstTask.id):
                    return True

        return False
