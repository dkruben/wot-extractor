# wot-extractor: codigo DESCOMPILADO de sources/res/story_mode/scripts/client/story_mode/visual_script/arena_blocks.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: story_mode/scripts/client/story_mode/visual_script/arena_blocks.py
from __future__ import absolute_import
from story_mode_common.story_mode_constants import MissionId, MissionsDifficulty
from visual_script import ASPECT
from visual_script.arena_blocks import ArenaMeta
from visual_script.block import Block
from visual_script.dependency import dependencyImporter
from visual_script.slot_types import SLOT_TYPE
story_mode_missions, = dependencyImporter('story_mode_common.configs.story_mode_missions')

class GetStoryModeDifficulty(Block, ArenaMeta):

    def __init__(self, *args, **kwargs):
        super(GetStoryModeDifficulty, self).__init__(*args, **kwargs)
        self._arena = self._makeDataInputSlot('arena', SLOT_TYPE.ARENA)
        self._result = self._makeDataOutputSlot('result', SLOT_TYPE.STR, self._getResult)

    def _getResult(self):
        difficulty = MissionsDifficulty.UNDEFINED.value
        missionId = self._arena.getValue().extraData.get('missionId', MissionId.UNDEFINED)
        if missionId != MissionId.UNDEFINED:
            missionSettings = story_mode_missions.missionsSchema.getModel()
            if missionSettings is not None:
                mission = missionSettings.getMission(missionId)
                if mission is not None:
                    difficulty = mission.difficulty.value
        self._result.setValue(difficulty)
        return

    @classmethod
    def blockAspects(cls):
        return [ASPECT.CLIENT]
