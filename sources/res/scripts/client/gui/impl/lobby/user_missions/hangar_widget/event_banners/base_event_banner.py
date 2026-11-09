# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/user_missions/hangar_widget/event_banners/base_event_banner.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/user_missions/hangar_widget/event_banners/base_event_banner.py
from __future__ import absolute_import
from typing import TYPE_CHECKING
from helpers import time_utils
if TYPE_CHECKING:
    from gui.impl.gen.view_models.views.lobby.user_missions.widget.event_banner_model import EventBannerModel

class BaseEventBanner(object):
    NAME = ''

    def __init__(self):
        super(BaseEventBanner, self).__init__()
        self._isVisible = False

    @property
    def isVisible(self):
        return self._isVisible

    @property
    def showTimerBeforeEventEnd(self):
        hoursBeforeEnd = 72
        return hoursBeforeEnd * time_utils.ONE_HOUR

    @property
    def playAppearAnim(self):
        return False

    def fillModel(self, model):
        model.setName(self.NAME)
        model.setShowTimerBeforeEventEnd(self.showTimerBeforeEventEnd)

    def createToolTipContent(self, event):
        return

    def onClick(self):
        pass

    def onAppearAnimationPlayed(self):
        pass

    def prepare(self):
        pass

    def onAppear(self):
        self._isVisible = True

    def onDisappear(self):
        self._isVisible = False

    def startPersistentListening(self):
        pass

    def stopPersistentListening(self):
        pass
