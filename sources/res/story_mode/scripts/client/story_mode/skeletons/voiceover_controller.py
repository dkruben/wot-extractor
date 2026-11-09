# wot-extractor: codigo DESCOMPILADO de sources/res/story_mode/scripts/client/story_mode/skeletons/voiceover_controller.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: story_mode/scripts/client/story_mode/skeletons/voiceover_controller.py
from __future__ import absolute_import
import typing
from skeletons.gui.game_control import IGameController
if typing.TYPE_CHECKING:
    from Event import Event

class IVoiceoverManager(IGameController):
    if typing.TYPE_CHECKING:
        onSubtitleShow = None
        onSubtitleHide = None
        onStarted = None
        onStopped = None

    @property
    def currentSubtitle(self):
        raise NotImplementedError

    @property
    def currentCtx(self):
        raise NotImplementedError

    @property
    def isPlaying(self):
        raise NotImplementedError

    def stopVoiceover(self):
        raise NotImplementedError

    def playVoiceover(self, voiceoverId, ctx=None, delay=None):
        raise NotImplementedError
