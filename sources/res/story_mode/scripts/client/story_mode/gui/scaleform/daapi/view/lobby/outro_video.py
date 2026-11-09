# wot-extractor: codigo DESCOMPILADO de sources/res/story_mode/scripts/client/story_mode/gui/scaleform/daapi/view/lobby/outro_video.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: story_mode/scripts/client/story_mode/gui/scaleform/daapi/view/lobby/outro_video.py
from __future__ import absolute_import
import typing
from story_mode.gui.scaleform.daapi.view.common.base_video import BaseVideo
from story_mode.gui.scaleform.daapi.view.model.video_settings_model import getOutroVideoSettings
from story_mode.uilogging.story_mode.loggers import OutroVideoLogger

class OutroVideo(BaseVideo):

    def __init__(self, ctx):
        super(OutroVideo, self).__init__(ctx)
        self._arenaUniqueID = ctx.get('arenaUniqueID')

    def onVideoComplete(self):
        super(OutroVideo, self).onVideoComplete()
        self._storyModeCtrl.onOutroVideoComplete(self._arenaUniqueID)

    def _populate(self):
        super(OutroVideo, self)._populate()
        self.as_loadedS()

    def _getSettings(self):
        return getOutroVideoSettings()

    def _getLogger(self):
        return OutroVideoLogger()

    def _getLoadingImage(self):
        return ''
