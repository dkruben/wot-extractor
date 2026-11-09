# wot-extractor: codigo DESCOMPILADO de sources/res/story_mode/scripts/client/StoryModeAccountComponent.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: story_mode/scripts/client/StoryModeAccountComponent.py
from __future__ import absolute_import
import AccountCommands
from BaseAccountExtensionComponent import BaseAccountExtensionComponent
from PlayerEvents import g_playerEvents
from constants import QUEUE_TYPE
from helpers import dependency
from story_mode.skeletons.story_mode_controller import IStoryModeController

class StoryModeAccountComponent(BaseAccountExtensionComponent):
    _storyModeCtrl = dependency.descriptor(IStoryModeController)

    def enqueueBattle(self):
        if not g_playerEvents.isPlayerEntityChanging:
            self.base.doCmdIntArr(AccountCommands.REQUEST_ID_NO_RESPONSE, AccountCommands.CMD_ENQUEUE_IN_BATTLE_QUEUE, (
             QUEUE_TYPE.STORY_MODE, self._storyModeCtrl.selectedMissionId))

    def dequeueBattle(self):
        if not g_playerEvents.isPlayerEntityChanging:
            self.base.doCmdInt(AccountCommands.REQUEST_ID_NO_RESPONSE, AccountCommands.CMD_DEQUEUE_FROM_BATTLE_QUEUE, QUEUE_TYPE.STORY_MODE)
