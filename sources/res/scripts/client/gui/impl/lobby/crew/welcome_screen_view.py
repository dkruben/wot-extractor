# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/crew/welcome_screen_view.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/crew/welcome_screen_view.py
from PlayerEvents import g_playerEvents
from base_crew_view import BaseCrewSubView
from frameworks.wulf import ViewFlags, ViewSettings, WindowFlags, WindowLayer
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.crew.welcome_screen_view_model import WelcomeScreenViewModel
from gui.impl.pub import WindowImpl

class WelcomeScreenView(BaseCrewSubView):
    __slots__ = ('__navigateFrom', '__onCloseCallback')

    def __init__(self, layoutID=R.views.mono.crew.welcome_screen(), navigateFrom=None, onCloseCallback=None):
        settings = ViewSettings(layoutID)
        settings.flags = ViewFlags.VIEW
        settings.model = WelcomeScreenViewModel()
        self.__navigateFrom = navigateFrom
        self.__onCloseCallback = onCloseCallback
        super(WelcomeScreenView, self).__init__(settings)

    @property
    def viewModel(self):
        return super(WelcomeScreenView, self).getViewModel()

    def _getEvents(self):
        return (
         (
          self.viewModel.onClose, self._onViewClose),
         (
          g_playerEvents.onDisconnected, self._onDisconnected))

    def _onViewClose(self):
        if callable(self.__onCloseCallback):
            self.__onCloseCallback()
        self.destroyWindow()

    def _onDisconnected(self):
        self.destroyWindow()


class WelcomeScreenViewWindow(WindowImpl):

    def __init__(self, navigateFrom=None, parent=None, onCloseCallback=None):
        super(WelcomeScreenViewWindow, self).__init__(WindowFlags.WINDOW | WindowFlags.WINDOW_FULLSCREEN, layer=WindowLayer.TOP_WINDOW, content=WelcomeScreenView(navigateFrom=navigateFrom, onCloseCallback=onCloseCallback), parent=parent)
