# wot-extractor: codigo DESCOMPILADO de sources/res/frontline/scripts/client/frontline/gui/impl/lobby/views/welcome_view.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: frontline/scripts/client/frontline/gui/impl/lobby/views/welcome_view.py
from __future__ import absolute_import
from frameworks.wulf import ViewFlags, ViewSettings, WindowFlags, WindowLayer
from gui.impl.pub import ViewImpl, WindowImpl
from gui.impl.gen import R
from frontline.gui.impl.gen.view_models.views.lobby.views.welcome_view_model import WelcomeViewModel

class WelcomeView(ViewImpl):

    def __init__(self):
        settings = ViewSettings(R.views.frontline.lobby.WelcomeView(), ViewFlags.VIEW, WelcomeViewModel())
        super(WelcomeView, self).__init__(settings)

    @property
    def viewModel(self):
        return super(WelcomeView, self).getViewModel()

    def _getEvents(self):
        return (
         (
          self.viewModel.onClose, self.__onViewClose),)

    def __onViewClose(self):
        self.destroyWindow()


class WelcomeViewWindow(WindowImpl):

    def __init__(self):
        super(WelcomeViewWindow, self).__init__(WindowFlags.WINDOW | WindowFlags.WINDOW_FULLSCREEN, layer=WindowLayer.TOP_WINDOW, content=WelcomeView())
