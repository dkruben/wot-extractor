# wot-extractor: codigo DESCOMPILADO de sources/res/story_mode/scripts/client/story_mode/gui/impl/lobby/story_mode_event_banner.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: story_mode/scripts/client/story_mode/gui/impl/lobby/story_mode_event_banner.py
from __future__ import absolute_import
import typing
from gui.impl import backport
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.user_missions.constants.event_banner_state import EventBannerState
from gui.impl.lobby.user_missions.hangar_widget.event_banners.event_banners_container import EventBannersContainer
from gui.impl.lobby.user_missions.hangar_widget.event_banners.standard_event_banner import StandardEventBanner
from helpers import dependency
from helpers.time_utils import getTimestampFromUTC, getServerUTCTime, ONE_DAY, ONE_MINUTE
from story_mode.account_settings import setEventEntryPointShown, getEventEntryPointShown, getEventVisited, getNewbieEntryPointAnimationSeenId, setNewbieEntryPointAnimationSeenId
from story_mode.gui.impl.lobby.event_banner_tooltip import EventBannerTooltip
from story_mode.gui.impl.lobby.newbie_banner_tooltip import NewbieBannerTooltip
from story_mode.skeletons.story_mode_controller import IStoryModeController
from story_mode.uilogging.story_mode.loggers import EntryPointLogger, NewbieEntryPointLogger
from story_mode_common.configs.story_mode_settings import settingsSchema
if typing.TYPE_CHECKING:
    from frameworks.wulf import ViewEvent

class StoryModeNewbieBanner(StandardEventBanner):
    NAME = 'StoryModeNewbieEntryPoint'
    _controller = dependency.descriptor(IStoryModeController)

    def __init__(self):
        super(StoryModeNewbieBanner, self).__init__()
        self._uiLogger = NewbieEntryPointLogger()

    @property
    def isMode(self):
        return True

    @property
    def borderColor(self):
        return '#F5C87C'

    @property
    def bannerState(self):
        if self._controller.isNewNeededForNewbies():
            return EventBannerState.INTRO
        return EventBannerState.IN_PROGRESS

    @property
    def playAppearAnim(self):
        newMissionIdForNewbies = self._controller.newMissionIdForNewbies
        if getNewbieEntryPointAnimationSeenId() < newMissionIdForNewbies:
            setNewbieEntryPointAnimationSeenId(newMissionIdForNewbies)
            return True
        return False

    @property
    def introDescription(self):
        return backport.text(R.strings.hangar_event_banners.event.StoryModeNewbieEntryPoint.introDescription())

    @property
    def inProgressDescription(self):
        return backport.text(R.strings.hangar_event_banners.event.StoryModeNewbieEntryPoint.inProgressDescription())

    def createToolTipContent(self, event):
        return NewbieBannerTooltip()

    def onClick(self):
        self._uiLogger.logClick()
        self._controller.switchPrb()


class StoryModeEventBanner(StandardEventBanner):
    NAME = 'StoryModeEventEntryPoint'
    _controller = dependency.descriptor(IStoryModeController)

    def __init__(self):
        super(StoryModeEventBanner, self).__init__()
        self._uiLogger = EntryPointLogger()

    @property
    def isMode(self):
        return True

    @property
    def borderColor(self):
        return '#37B4CA'

    @property
    def bannerState(self):
        if getEventVisited():
            return EventBannerState.IN_PROGRESS
        return EventBannerState.INTRO

    @property
    def timerValue(self):
        settings = settingsSchema.getModel()
        if settings is not None:
            timeLeft = int(getTimestampFromUTC(settings.entryPoint.eventEndAt.timetuple()) - getServerUTCTime())
            return max(timeLeft, ONE_MINUTE)
        else:
            return 0

    @property
    def showTimerBeforeEventEnd(self):
        return ONE_DAY

    @property
    def playAppearAnim(self):
        if not getEventEntryPointShown():
            setEventEntryPointShown()
            return True
        return False

    @property
    def introDescription(self):
        return backport.text(R.strings.hangar_event_banners.event.StoryModeEventEntryPoint.introDescription())

    @property
    def inProgressDescription(self):
        return backport.text(R.strings.hangar_event_banners.event.StoryModeEventEntryPoint.inProgressDescription())

    def createToolTipContent(self, event):
        return EventBannerTooltip()

    def onClick(self):
        self._uiLogger.logClick()
        self._controller.switchPrb()

    def onAppear(self):
        super(StoryModeEventBanner, self).onAppear()
        self._controller.onSettingsUpdated += self._onSettingsUpdated

    def onDisappear(self):
        self._controller.onSettingsUpdated -= self._onSettingsUpdated
        super(StoryModeEventBanner, self).onDisappear()

    def _onSettingsUpdated(self):
        EventBannersContainer().onBannerUpdate(self)
