# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/pub/window_loader_controller.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/pub/window_loader_controller.py
from __future__ import absolute_import
import logging
from frameworks.wulf import WindowStatus, WindowFlags
from gui.Scaleform.Waiting import Waiting
from helpers import dependency
from skeletons.gui.impl import IWindowLoaderController, IGuiLoader
_logger = logging.getLogger(__name__)

class WindowLoaderController(IWindowLoaderController):
    __slots__ = ('__callbackID', '__loadingWindows', '__isWaitingShown')
    __gui = dependency.descriptor(IGuiLoader)

    def __init__(self):
        super(WindowLoaderController, self).__init__()
        self.__loadingWindows = []
        self.__isWaitingShown = False

    def init(self):
        self.__gui.windowsManager.onWindowStatusChanged += self.__windowStatusChanged

    def fini(self):
        self.__gui.windowsManager.onWindowStatusChanged -= self.__windowStatusChanged

    def __windowStatusChanged(self, uniqueID, newStatus):
        from gui.Scaleform.framework.entities.sf_window import SFWindow
        window = self.__gui.windowsManager.getWindow(uniqueID)
        if window is None or window.modalityFlag != WindowFlags.WINDOW_MODAL:
            return
        isSFWindow = isinstance(window, SFWindow)
        if newStatus == WindowStatus.LOADING:
            if isSFWindow:
                window.onContentLoaded += self.__onDAAPIContentLoaded
            self.__loadingWindows.append(uniqueID)
            self.__triggerWaiting()
        elif newStatus == WindowStatus.LOADED and not isSFWindow:
            self.__loadingWindows.remove(uniqueID)
            self.__triggerWaiting()
        elif newStatus == WindowStatus.DESTROYING and uniqueID in self.__loadingWindows:
            if isSFWindow:
                window.onContentLoaded -= self.__onDAAPIContentLoaded
            self.__loadingWindows.remove(uniqueID)
            self.__triggerWaiting()
        return

    def __triggerWaiting(self):
        self.__callbackID = None
        hasLoading = bool(self.__loadingWindows)
        if self.__isWaitingShown:
            if not hasLoading:
                self.__isWaitingShown = False
                Waiting.hide('loadModalWindow')
                _logger.debug('Release screen from waiting.')
        elif hasLoading:
            self.__isWaitingShown = True
            _logger.debug('Lock screen with waiting.')
            Waiting.show('loadModalWindow', softStart=True)
        return

    def __onDAAPIContentLoaded(self, window):
        window.onContentLoaded -= self.__onDAAPIContentLoaded
        self.__loadingWindows.remove(window.uniqueID)
        self.__triggerWaiting()
