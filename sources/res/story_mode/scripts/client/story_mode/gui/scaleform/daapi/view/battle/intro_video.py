# wot-extractor: codigo DESCOMPILADO de sources/res/story_mode/scripts/client/story_mode/gui/scaleform/daapi/view/battle/intro_video.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: story_mode/scripts/client/story_mode/gui/scaleform/daapi/view/battle/intro_video.py
from __future__ import absolute_import
import BattleReplay
from gui.battle_control.arena_info.interfaces import IArenaLoadController
from gui.game_loading import loading
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider
from story_mode.gui.fade_in_out import UseStoryModeFading
from story_mode.gui.scaleform.daapi.view.common.base_video import BaseVideo
from story_mode.gui.scaleform.daapi.view.model.video_settings_model import getIntroVideoSettings
from story_mode.gui.shared.event_dispatcher import showPrebattleWindow
from story_mode.uilogging.story_mode.loggers import IntroVideoLogger

class IntroVideo(BaseVideo, IArenaLoadController):
    _sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def spaceLoadCompleted(self):
        loading.getLoader().idle()
        if BattleReplay.isPlaying():
            self._storyModeCtrl.goToBattle()
            self.destroy()
        else:
            self.as_loadedS()

    @UseStoryModeFading(hide=False)
    def onVideoComplete(self):
        super(IntroVideo, self).onVideoComplete()
        showPrebattleWindow(self._missionId)

    def _populate(self):
        super(IntroVideo, self)._populate()
        self._sessionProvider.addArenaCtrl(self)

    def _dispose(self):
        self._sessionProvider.removeArenaCtrl(self)
        super(IntroVideo, self)._dispose()

    def _getSettings(self):
        return getIntroVideoSettings()

    def _getLogger(self):
        return IntroVideoLogger()
