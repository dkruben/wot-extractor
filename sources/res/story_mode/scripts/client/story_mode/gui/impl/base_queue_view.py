# wot-extractor: codigo DESCOMPILADO de sources/res/story_mode/scripts/client/story_mode/gui/impl/base_queue_view.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: story_mode/scripts/client/story_mode/gui/impl/base_queue_view.py
from __future__ import absolute_import
import BigWorld
from PlayerEvents import g_playerEvents
from helpers import dependency
from gui.impl.pub import ViewImpl
from shared_utils import safeCancelCallback
from story_mode.skeletons.story_mode_controller import IStoryModeController

class BaseWaitQueueView(ViewImpl):
    __slots__ = ('_timerCallback', )
    storyModeCtrl = dependency.descriptor(IStoryModeController)

    def __init__(self, *args, **kwargs):
        super(BaseWaitQueueView, self).__init__(*args, **kwargs)
        self._timerCallback = None
        return

    def startWaitQueue(self):
        if self._timerCallback is None:
            self._timerCallback = BigWorld.callback(self.storyModeCtrl.settings.waitTimeQueue, self._onWaitQueueTimeout)
        return

    def _onLoading(self, *args, **kwargs):
        super(BaseWaitQueueView, self)._onLoading(*args, **kwargs)
        g_playerEvents.onArenaCreated += self._onArenaCreated

    def _finalize(self):
        self._stopTimer()
        g_playerEvents.onArenaCreated -= self._onArenaCreated
        super(BaseWaitQueueView, self)._finalize()

    def _onArenaCreated(self):
        self._stopTimer()

    def _stopTimer(self):
        if self._timerCallback is not None:
            safeCancelCallback(self._timerCallback)
            self._timerCallback = None
        return

    def _onWaitQueueTimeout(self):
        self._timerCallback = None
        return
