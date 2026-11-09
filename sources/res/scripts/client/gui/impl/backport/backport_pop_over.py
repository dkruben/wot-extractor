# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/backport/backport_pop_over.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/backport/backport_pop_over.py
from __future__ import absolute_import
from collections import namedtuple
import logging
from frameworks.wulf import ViewSettings, ViewModel
from gui.impl.gen import R
from gui.impl.pub import PopOverViewImpl
from gui.shared import g_eventBus
from gui.shared.events import HidePopoverEvent
from helpers import dependency
from skeletons.gui.app_loader import IAppLoader
_logger = logging.getLogger(__name__)
_PopOverData = namedtuple('PopOverData', ('alias', 'args'))

def createPopOverData(alias, args=None):
    return _PopOverData(alias, args)


class BackportPopOverContent(PopOverViewImpl):
    __appLoader = dependency.descriptor(IAppLoader)
    __slots__ = ()

    def __init__(self, popOverData):
        settings = ViewSettings(R.views.common.pop_over_window.backport_pop_over.BackportPopOverContent())
        settings.model = ViewModel()
        settings.kwargs = {'alias': (popOverData.alias), 'data': (popOverData.args)}
        super(BackportPopOverContent, self).__init__(settings)

    def _initialize(self, alias, data):
        super(BackportPopOverContent, self)._initialize()
        popoverManager = self.__appLoader.getApp().popoverManager
        if popoverManager is None:
            _logger.error("popoverManager doesn't exist.")
            return
        else:
            popoverManager.requestShowPopover(alias, data)
            g_eventBus.addListener(HidePopoverEvent.POPOVER_DESTROYED, self.__onPopOverDestroy)
            return

    def _finalize(self):
        g_eventBus.removeListener(HidePopoverEvent.POPOVER_DESTROYED, self.__onPopOverDestroy)
        popoverManager = self.__appLoader.getApp().popoverManager
        if popoverManager is not None:
            popoverManager.requestHidePopover()
        super(BackportPopOverContent, self)._finalize()
        return

    def __onPopOverDestroy(self, _):
        self.destroyWindow()
