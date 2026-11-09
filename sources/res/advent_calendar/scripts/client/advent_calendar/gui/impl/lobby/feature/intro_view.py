# wot-extractor: codigo DESCOMPILADO de sources/res/advent_calendar/scripts/client/advent_calendar/gui/impl/lobby/feature/intro_view.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: advent_calendar/scripts/client/advent_calendar/gui/impl/lobby/feature/intro_view.py
from __future__ import absolute_import
import logging
from account_helpers.AccountSettings import AdventCalendar
from advent_calendar.gui.impl.gen.view_models.views.lobby.intro_screen_model import IntroScreenModel
from advent_calendar.gui.impl.lobby.feature.advent_helper import isAdventAnimationEnabled, setAdventCalendarSetting
from advent_calendar.gui.shared import events
from advent_calendar.skeletons import IAdventCalendarController
from frameworks.wulf import ViewSettings, WindowFlags, WindowLayer
from gui.impl.gen import R
from gui.impl.pub import ViewImpl
from gui.impl.pub.lobby_window import LobbyWindow
from gui.shared import g_eventBus, EVENT_BUS_SCOPE
from helpers import dependency
_logger = logging.getLogger(__name__)

class AdventCalendarIntroView(ViewImpl):
    __adventController = dependency.descriptor(IAdventCalendarController)

    def __init__(self, *args, **kwargs):
        settings = ViewSettings(R.views.advent_calendar.mono.lobby.intro_screen_view(), model=IntroScreenModel(), args=args, kwargs=kwargs)
        super(AdventCalendarIntroView, self).__init__(settings)

    @property
    def viewModel(self):
        return self.getViewModel()

    def _getEvents(self):
        return (
         (
          self.viewModel.onClose, self.__onClose),
         (
          self.viewModel.onCloseAnimationStarted, self.__onCloseAnimationStarted))

    def _onLoading(self, *args, **kwargs):
        isFirstTime = kwargs.pop('isFirstTime', False)
        super(AdventCalendarIntroView, self)._onLoading(*args, **kwargs)
        config = self.__adventController.config
        with self.viewModel.transaction() as tx:
            tx.setStartDate(config.startDate)
            tx.setEndDate(config.postEventStartDate)
            tx.setDoorsCount(config.doorsCount)
            tx.setIsAnimationEnabled(isAdventAnimationEnabled())
            tx.setIsOpenedFirstTime(isFirstTime)
        if isFirstTime:
            setAdventCalendarSetting(AdventCalendar.INTRO_SHOWN, True)

    @staticmethod
    def __onCloseAnimationStarted():
        g_eventBus.handleEvent(events.AdventCalendarEvent(events.AdventCalendarEvent.INTRO_CLOSE_STARTED), scope=EVENT_BUS_SCOPE.LOBBY)

    def __onClose(self):
        self.destroyWindow()


class AdventCalendarIntroWindow(LobbyWindow):

    def __init__(self, parent=None, **kwargs):
        super(AdventCalendarIntroWindow, self).__init__(WindowFlags.WINDOW | WindowFlags.WINDOW_FULLSCREEN, layer=WindowLayer.TOP_WINDOW, content=AdventCalendarIntroView(**kwargs), parent=parent)
