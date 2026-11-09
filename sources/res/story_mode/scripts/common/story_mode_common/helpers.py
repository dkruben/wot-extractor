# wot-extractor: codigo DESCOMPILADO de sources/res/story_mode/scripts/common/story_mode_common/helpers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: story_mode/scripts/common/story_mode_common/helpers.py
from __future__ import absolute_import
import typing
from external_strings_utils import strtobool
from story_mode_common.story_mode_constants import LONG_INT_HALF_SHIFT, MissionType, DISABLE_REGULAR_OPERATIONS
if typing.TYPE_CHECKING:
    from story_mode_common.configs.story_mode_missions import MissionModel

def isTaskCompleted(progress, missionId, taskId):
    return bool(progress.get(missionId, 0) & taskBitMask(taskId))


def isMissionCompleted(progress, missionModel):
    missionProgress = progress.get(missionModel.missionId, 0)
    return missionProgress and all(missionProgress & taskBitMask(task.id) for task in missionModel.tasks)


def taskBitMask(taskId):
    return 1 << taskId - 1


def getRewardActionSetId(missionId, taskId=0):
    return missionId << LONG_INT_HALF_SHIFT | taskId


def isMissionDisabledByABGroup(mission, group, abConfig):
    if abConfig is not None and group in abConfig:
        abGroupProperties = abConfig[group]['properties']
        if mission.missionType == MissionType.REGULAR:
            return strtobool(abGroupProperties.get(DISABLE_REGULAR_OPERATIONS, '0'))
    return False
