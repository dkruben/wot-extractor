# wot-extractor: codigo DESCOMPILADO de sources/res/halloween/scripts/client/halloween/gui/impl/battle/help_view.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: halloween/scripts/client/halloween/gui/impl/battle/help_view.py
from __future__ import absolute_import
import logging
from frameworks.wulf import ViewSettings, WindowFlags, WindowLayer, ViewModel
from gui.app_loader.settings import APP_NAME_SPACE
from gui.impl.gen import R
from gui.impl.pub import ViewImpl, WindowImpl
from helpers import dependency
from skeletons.gui.app_loader import IAppLoader
_logger = logging.getLogger(__name__)

class HelpView(ViewImpl):
    appLoader = dependency.descriptor(IAppLoader)

    def __init__(self, layoutID=R.views.halloween.mono.battle.help()):
        settings = ViewSettings(layoutID=layoutID, model=ViewModel())
        super(HelpView, self).__init__(settings)

    @property
    def _battleApp(self):
        return self.appLoader.getApp(APP_NAME_SPACE.SF_BATTLE)

    def _initialize(self, *args, **kwargs):
        super(HelpView, self)._initialize(*args, **kwargs)
        self._battleApp.enterGuiControlMode(R.views.halloween.mono.battle.help(), cursorVisible=True, enableAiming=False)

    def _finalize(self):
        self._battleApp.leaveGuiControlMode(R.views.halloween.mono.battle.help())
        super(HelpView, self)._finalize()


class HelpWindow(WindowImpl):
    __slots__ = ()

    def __init__(self, parent=None):
        super(HelpWindow, self).__init__(wndFlags=WindowFlags.WINDOW_FULLSCREEN | WindowFlags.WINDOW | WindowFlags.WINDOW_MODALITY_MASK, content=HelpView(), layer=WindowLayer.OVERLAY, parent=parent)
