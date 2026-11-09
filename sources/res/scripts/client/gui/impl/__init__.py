# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/__init__.py
from __future__ import absolute_import
import typing
from skeletons.gui.game_control import IGameStateTracker
from skeletons.gui.impl import IGuiLoader, IFullscreenManager, INotificationWindowController
if typing.TYPE_CHECKING:
    from helpers.dependency import DependencyManager
__all__ = ('getGuiImplConfig', )

def getGuiImplConfig(manager):
    from gui.impl.gui_loader import GuiLoader
    from gui.impl.pub.fullscreen_manager import FullscreenManager
    from gui.impl.pub.notification_window_controller import NotificationWindowController
    from gui.impl.pub.window_loader_controller import WindowLoaderController
    loader = GuiLoader()
    loader.init()
    manager.addInstance(IGuiLoader, loader, finalizer='fini')
    notifications = NotificationWindowController()
    tracker = manager.getService(IGameStateTracker)
    tracker.addController(notifications)
    notifications.init()
    manager.addInstance(INotificationWindowController, notifications, finalizer='fini')
    windowLoader = WindowLoaderController()
    tracker.addController(windowLoader)
    windowLoader.init()
    manager.addInstance(WindowLoaderController, windowLoader, finalizer='fini')
    fullscreen = FullscreenManager()
    fullscreen.init()
    manager.addInstance(IFullscreenManager, fullscreen, finalizer='fini')
