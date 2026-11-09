# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/pub/main_window.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/pub/main_window.py
from __future__ import absolute_import
import typing
from frameworks.wulf import WindowFlags
from gui.impl.gen import R
from gui.impl.pub.window_impl import WindowImpl
if typing.TYPE_CHECKING:
    from gui.impl.pub.main_view import MainView

class MainWindow(WindowImpl):

    def __init__(self, content=None):
        super(MainWindow, self).__init__(WindowFlags.MAIN_WINDOW, content=content)

    def _initialize(self):
        super(MainWindow, self)._initialize()
        self.gui.windowsManager.addWindowsArea(R.areas.default())
        self.gui.windowsManager.addWindowsArea(R.areas.specific())
        self.gui.windowsManager.addWindowsArea(R.areas.pop_over())
        self.gui.windowsManager.addWindowsArea(R.areas.context_menu())
        self.gui.windowsManager.addWindowsArea(R.areas.flattening_window())

    def _finalize(self):
        self.gui.windowsManager.removeWindowsArea(R.areas.default())
        self.gui.windowsManager.removeWindowsArea(R.areas.specific())
        self.gui.windowsManager.removeWindowsArea(R.areas.pop_over())
        self.gui.windowsManager.removeWindowsArea(R.areas.context_menu())
        self.gui.windowsManager.removeWindowsArea(R.areas.flattening_window())
        super(MainWindow, self)._finalize()
