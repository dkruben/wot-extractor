# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/personal_missions_30/intro_view.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/personal_missions_30/intro_view.py
from __future__ import absolute_import
import SoundGroups
from frameworks.wulf import ViewFlags, ViewSettings, WindowFlags, WindowLayer
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.personal_missions_30.intro_screen_model import IntroScreenModel
from gui.impl.lobby.personal_missions_30.personal_mission_constants import IntroKeys
from gui.impl.lobby.personal_missions_30.views_helpers import setVideoOverlayOff, setVideoOverlayOn
from gui.impl.pub import ViewImpl, WindowImpl
from helpers import dependency
from skeletons.account_helpers.settings_core import ISettingsCore
from skeletons.gui.impl import IGuiLoader

class IntroView(ViewImpl):

    def __init__(self, layoutID, videoKey=None, operationID=None):
        self.videoKey = videoKey
        self.operationID = operationID
        settings = ViewSettings(layoutID)
        settings.flags = ViewFlags.VIEW
        settings.model = IntroScreenModel()
        super(IntroView, self).__init__(settings)

    @property
    def viewModel(self):
        return super(IntroView, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        setVideoOverlayOn()
        with self.viewModel.transaction() as tx:
            tx.setVideoPath(self.videoKey.lower())

    def _finalize(self):
        SoundGroups.g_instance.playSound2D('vid_pm_stop')
        setVideoOverlayOff()
        super(IntroView, self)._finalize()


class IntroViewWindow(WindowImpl):
    settingsCore = dependency.descriptor(ISettingsCore)
    gui = dependency.descriptor(IGuiLoader)
    introKey = None

    def __init__(self, operationID=None):
        super(IntroViewWindow, self).__init__(WindowFlags.WINDOW | WindowFlags.WINDOW_FULLSCREEN, content=IntroView(R.views.mono.personal_missions_30.intro_screen(), self.introKey, operationID), layer=WindowLayer.FULLSCREEN_WINDOW)


class MainIntroViewWindow(IntroViewWindow):

    def __init__(self):
        self.introKey = IntroKeys.PM3_MAIN_INTRO_VIEW.value
        super(MainIntroViewWindow, self).__init__()


class OperationIntroViewWindow(IntroViewWindow):

    def __init__(self, operationID):
        self.introKey = IntroKeys.OPERATION_INTRO_VIEW.value % operationID
        super(OperationIntroViewWindow, self).__init__(operationID)
