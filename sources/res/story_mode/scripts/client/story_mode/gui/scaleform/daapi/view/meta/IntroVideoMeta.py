# wot-extractor: codigo DESCOMPILADO de sources/res/story_mode/scripts/client/story_mode/gui/scaleform/daapi/view/meta/IntroVideoMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: story_mode/scripts/client/story_mode/gui/scaleform/daapi/view/meta/IntroVideoMeta.py
from gui.Scaleform.framework.entities.View import View

class IntroVideoMeta(View):

    def onVideoStarted(self):
        self._printOverrideError('onVideoStarted')

    def onVideoComplete(self):
        self._printOverrideError('onVideoComplete')

    def onSkipButtonVisible(self):
        self._printOverrideError('onSkipButtonVisible')

    def onSkipButtonClicked(self):
        self._printOverrideError('onSkipButtonClicked')

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_setCurrentSubtitleS(self, text):
        if self._isDAAPIInited():
            return self.flashObject.as_setCurrentSubtitle(text)

    def as_loadedS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_loaded()

    def as_pausePlaybackS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_pausePlayback()

    def as_resumePlaybackS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_resumePlayback()

    def as_handleKeydownS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_handleKeydown()
