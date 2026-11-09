# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/backport/backport_context_menu.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/backport/backport_context_menu.py
from __future__ import absolute_import
import logging
from collections import namedtuple
from frameworks.wulf import Window, WindowSettings, WindowFlags
from helpers import dependency
from skeletons.gui.app_loader import IAppLoader
_logger = logging.getLogger(__name__)
_ContextMenuData = namedtuple('ContextMenuData', ('type', 'args'))

def createContextMenuData(contextMenuType, args=None):
    return _ContextMenuData(contextMenuType, args)


class BackportContextMenuWindow(Window):
    __appLoader = dependency.descriptor(IAppLoader)
    __slots__ = ('__contextMenuData', )

    def __init__(self, contextMenuData, parent):
        self.__contextMenuData = contextMenuData
        settings = WindowSettings()
        settings.flags = WindowFlags.CONTEXT_MENU
        settings.parent = parent
        super(BackportContextMenuWindow, self).__init__(settings)

    def _initialize(self):
        super(BackportContextMenuWindow, self)._initialize()
        contextMenuMgr = self.__appLoader.getApp().contextMenuManager
        if contextMenuMgr is not None:
            contextMenuMgr.show(self.__contextMenuData.type, self.__contextMenuData.args)
            contextMenuMgr.onContextMenuHide += self.__contextMenuHideHandler
        else:
            _logger.error("contextMenuMgr doesn't exist.")
        return

    def _finalize(self):
        contextMenuMgr = self.__appLoader.getApp().contextMenuManager
        if contextMenuMgr is not None:
            contextMenuMgr.onContextMenuHide -= self.__contextMenuHideHandler
            contextMenuMgr.pyHide()
        super(BackportContextMenuWindow, self)._finalize()
        return

    def __contextMenuHideHandler(self):
        self.destroy()
