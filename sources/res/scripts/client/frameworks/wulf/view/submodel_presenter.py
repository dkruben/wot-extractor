# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/frameworks/wulf/view/submodel_presenter.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/frameworks/wulf/view/submodel_presenter.py
from __future__ import absolute_import
import logging, weakref, typing
from helpers.events_handler import EventsHandler
if typing.TYPE_CHECKING:
    from typing import Optional
    from frameworks.wulf import View, ViewEvent, Window
_logger = logging.getLogger(__name__)

class SubModelPresenter(EventsHandler):
    __slots__ = ('__viewModel', '__isLoaded', '__parentView')

    def __init__(self, viewModel, parentView):
        self.__parentView = parentView
        self.__viewModel = weakref.proxy(viewModel)
        self.__isLoaded = False

    @property
    def isLoaded(self):
        return self.__isLoaded

    @property
    def parentView(self):
        return self.__parentView

    def getParentWindow(self):
        return self.parentView.getParentWindow()

    def getViewModel(self):
        return self.__viewModel

    def initialize(self, *args, **kwargs):
        self._subscribe()
        self.__isLoaded = True

    def finalize(self):
        if not self.__isLoaded:
            _logger.warning('Try to destroy %r which is not loaded', type(self))
            return
        self.__isLoaded = False
        self._unsubscribe()

    def clear(self):
        self.__viewModel = None
        return

    def createToolTipContent(self, event, contentID):
        return

    def createPopOverContent(self, event):
        return

    def createContextMenuContent(self, event):
        return

    def createToolTip(self, event):
        return

    def createPopOver(self, event):
        return

    def createContextMenu(self, event):
        return
