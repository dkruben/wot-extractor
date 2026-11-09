# wot-extractor: codigo DESCOMPILADO de sources/res/story_mode/scripts/client/story_mode/gui/scaleform/daapi/view/battle/subtitles.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: story_mode/scripts/client/story_mode/gui/scaleform/daapi/view/battle/subtitles.py
from __future__ import absolute_import
from helpers import dependency
from story_mode.gui.scaleform.daapi.view.meta.StoryModeSubtitlesMeta import StoryModeSubtitlesMeta
from story_mode.skeletons.story_mode_controller import IStoryModeController
from story_mode.skeletons.voiceover_controller import IVoiceoverManager

class BattleSubtitles(StoryModeSubtitlesMeta):
    _voiceoverManager = dependency.descriptor(IVoiceoverManager)
    _storyModeCtrl = dependency.descriptor(IStoryModeController)

    def _populate(self):
        super(BattleSubtitles, self)._populate()
        self._voiceoverManager.onSubtitleShow += self._showSubtitleHandler
        self._voiceoverManager.onSubtitleHide += self._hideSubtitleHandler
        if not self._storyModeCtrl.isSelectedMissionOnboarding:
            self.as_setNonOnboardingS()
        if self._voiceoverManager.currentSubtitle:
            self.as_showS(self._voiceoverManager.currentSubtitle)

    def _destroy(self):
        super(BattleSubtitles, self)._destroy()
        self._voiceoverManager.onSubtitleShow -= self._showSubtitleHandler
        self._voiceoverManager.onSubtitleHide -= self._hideSubtitleHandler

    def _showSubtitleHandler(self):
        self.as_showS(self._voiceoverManager.currentSubtitle)

    def _hideSubtitleHandler(self):
        self.as_hideS()
