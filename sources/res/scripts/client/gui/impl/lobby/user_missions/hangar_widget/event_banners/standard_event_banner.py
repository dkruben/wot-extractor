# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/user_missions/hangar_widget/event_banners/standard_event_banner.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/user_missions/hangar_widget/event_banners/standard_event_banner.py
from __future__ import absolute_import
import typing
from gui.impl.gen.view_models.views.lobby.user_missions.constants.event_banner_state import EventBannerState
from gui.impl.lobby.user_missions.hangar_widget.event_banners.base_event_banner import BaseEventBanner
if typing.TYPE_CHECKING:
    from gui.impl.gen.view_models.views.lobby.user_missions.widget.event_banner_model import EventBannerModel

class StandardEventBanner(BaseEventBanner):

    @property
    def bannerState(self):
        return EventBannerState.INACTIVE

    @property
    def isMode(self):
        return False

    @property
    def hasRewards(self):
        return False

    @property
    def borderColor(self):
        return ''

    @property
    def title(self):
        return ''

    @property
    def iconsPath(self):
        return ''

    @property
    def videosPath(self):
        return ''

    @property
    def introDescription(self):
        return ''

    @property
    def inProgressDescription(self):
        return ''

    @property
    def timerText(self):
        return ''

    @property
    def timerValue(self):
        return 0

    @property
    def eventStartDate(self):
        return 0

    @property
    def eventEndDate(self):
        return 0

    @property
    def playAppearAnim(self):
        return False

    def fillModel(self, model):
        super(StandardEventBanner, self).fillModel(model)
        model.setIsMode(self.isMode)
        model.setTitle(self.title)
        model.setHasRewards(self.hasRewards)
        model.setIntroDescription(self.introDescription)
        model.setInProgressDescription(self.inProgressDescription)
        model.setBannerState(self.bannerState)
        model.setIconsPath(self.iconsPath)
        model.setVideosPath(self.videosPath)
        model.setBorderColor(self.borderColor)
        model.setTimerText(self.timerText)
        model.setTimerValue(self.timerValue)
        model.setEventEndDate(self.eventEndDate)
        model.setEventStartDate(self.eventStartDate)
