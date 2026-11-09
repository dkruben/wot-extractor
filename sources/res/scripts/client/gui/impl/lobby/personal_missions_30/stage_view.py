# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/personal_missions_30/stage_view.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/personal_missions_30/stage_view.py
from __future__ import absolute_import
from typing import TYPE_CHECKING
import SoundGroups
from frameworks.wulf import ViewFlags, ViewSettings, WindowFlags, WindowLayer
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.personal_missions_30.assembling_video_view_model import AssemblingVideoViewModel
from gui.impl.lobby.personal_missions_30.views_helpers import setVideoOverlayOn, setVideoOverlayOff
from gui.impl.pub import ViewImpl, WindowImpl
if TYPE_CHECKING:
    from typing import Callable, Optional

class AssemblingVideoView(ViewImpl):

    def __init__(self, layoutID, operationID, stageNumber, closingCallback=None):
        self.operationID = operationID
        self.stageNumber = stageNumber
        self.closingCallback = closingCallback
        settings = ViewSettings(layoutID, flags=ViewFlags.VIEW, model=AssemblingVideoViewModel())
        super(AssemblingVideoView, self).__init__(settings)

    @property
    def viewModel(self):
        return super(AssemblingVideoView, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        super(AssemblingVideoView, self)._onLoading()
        setVideoOverlayOn()
        with self.viewModel.transaction() as tx:
            tx.setOperationID(self.operationID)
            tx.setStageNumber(self.stageNumber)

    def _finalize(self):
        self.__startAssembling()
        SoundGroups.g_instance.playSound2D('vid_pm_stop')
        setVideoOverlayOff()
        super(AssemblingVideoView, self)._finalize()

    def _getEvents(self):
        return super(AssemblingVideoView, self)._getEvents() + (
         (
          self.viewModel.startAssembling, self.__startAssembling),)

    def __startAssembling(self):
        if self.closingCallback is not None:
            self.closingCallback()
            self.closingCallback = None
        return


class AssemblingVideoViewWindow(WindowImpl):

    def __init__(self, operationID, stageNumber, closingCallback=None):
        super(AssemblingVideoViewWindow, self).__init__(WindowFlags.WINDOW | WindowFlags.WINDOW_FULLSCREEN, content=AssemblingVideoView(R.views.mono.personal_missions_30.assembling_video(), operationID, stageNumber, closingCallback=closingCallback), layer=WindowLayer.FULLSCREEN_WINDOW)
