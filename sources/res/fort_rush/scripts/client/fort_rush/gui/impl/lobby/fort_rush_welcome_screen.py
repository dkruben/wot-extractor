# wot-extractor: codigo DESCOMPILADO de sources/res/fort_rush/scripts/client/fort_rush/gui/impl/lobby/fort_rush_welcome_screen.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fort_rush/scripts/client/fort_rush/gui/impl/lobby/fort_rush_welcome_screen.py
from __future__ import absolute_import
from fort_rush.account_helpers.account_settings import setWelcomeScreenSeen, isWelcomeScreenSeen
from fort_rush.gui.impl.gen.view_models.views.lobby.fort_rush_welcome_screen_view_model import FortRushWelcomeScreenViewModel
from fort_rush.gui.sounds.sound_constants import FORT_RUSH_PROMO_SOUND_SPACE
from frameworks.wulf import ViewFlags, ViewSettings, WindowFlags, WindowLayer
from gui import GUI_SETTINGS
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.impl.gen import R
from gui.impl.pub import ViewImpl, WindowImpl
from gui.shared import g_eventBus, events
from gui.shared.event_dispatcher import showBrowserOverlayView
from gui.sounds.filters import switchVideoOverlaySoundFilter

class FortRushWelcomeScreenView(ViewImpl):
    LAYOUT_ID = R.views.fort_rush.mono.lobby.welcome_screen_view()
    _COMMON_SOUND_SPACE = FORT_RUSH_PROMO_SOUND_SPACE

    def __init__(self, layoutID=LAYOUT_ID, *args, **kwargs):
        settings = ViewSettings(layoutID, ViewFlags.VIEW, FortRushWelcomeScreenViewModel(), *args, **kwargs)
        super(FortRushWelcomeScreenView, self).__init__(settings)

    @property
    def viewModel(self):
        return super(FortRushWelcomeScreenView, self).getViewModel()

    def _getEvents(self):
        return (
         (
          self.viewModel.onClose, self._onClose),
         (
          self.viewModel.onVideoPlay, self._onVideoPlay),
         (
          self.viewModel.onViewLoaded, self._onViewLoaded))

    def _onViewLoaded(self):
        g_eventBus.handleEvent(events.ViewReadyEvent(self.layoutID))
        if not isWelcomeScreenSeen():
            setWelcomeScreenSeen()

    def _onClose(self):
        self.destroyWindow()
        if not isWelcomeScreenSeen():
            setWelcomeScreenSeen()

    def _onVideoPlay(self):
        url = GUI_SETTINGS.lookup('frEventIntroVideo') or GUI_SETTINGS.lookup('frEventInfoPage')
        if not url:
            return
        switchVideoOverlaySoundFilter(on=True)
        showBrowserOverlayView(url, alias=VIEW_ALIAS.WEB_VIEW_TRANSPARENT, parent=self.getParentWindow(), hiddenLayers=(
         WindowLayer.MARKER, WindowLayer.VIEW, WindowLayer.WINDOW), callbackOnClose=self._onBrowserClosed)

    def _onBrowserClosed(self):
        switchVideoOverlaySoundFilter(on=False)


class FortRushWelcomeScreenViewWindow(WindowImpl):

    def __init__(self, parent=None):
        super(FortRushWelcomeScreenViewWindow, self).__init__(WindowFlags.WINDOW | WindowFlags.WINDOW_FULLSCREEN, content=FortRushWelcomeScreenView(), layer=WindowLayer.FULLSCREEN_WINDOW, parent=parent)
