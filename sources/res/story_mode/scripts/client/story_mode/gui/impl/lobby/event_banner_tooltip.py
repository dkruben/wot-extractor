# wot-extractor: codigo DESCOMPILADO de sources/res/story_mode/scripts/client/story_mode/gui/impl/lobby/event_banner_tooltip.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: story_mode/scripts/client/story_mode/gui/impl/lobby/event_banner_tooltip.py
from __future__ import absolute_import
from frameworks.wulf.view.view import ViewSettings
from gui.impl.gen import R
from gui.impl.pub import ViewImpl
from helpers.time_utils import getTimestampFromUTC, getServerUTCTime
from story_mode.uilogging.story_mode.loggers import EventEntryPointTooltipLogger
from story_mode_common.configs.story_mode_settings import settingsSchema
from story_mode.gui.impl.gen.view_models.views.lobby.event_banner_tooltip_model import EventBannerTooltipModel

class EventBannerTooltip(ViewImpl):

    def __init__(self):
        super(EventBannerTooltip, self).__init__(ViewSettings(R.views.story_mode.mono.lobby.tooltips.event_banner_tooltip(), model=EventBannerTooltipModel()))
        self._uiLogger = EventEntryPointTooltipLogger()
        self._uiLogger.start()

    @property
    def viewModel(self):
        return super(EventBannerTooltip, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        super(EventBannerTooltip, self)._onLoading(*args, **kwargs)
        settings = settingsSchema.getModel()
        if settings is not None:
            self.viewModel.setTimerValue(getTimestampFromUTC(settings.entryPoint.eventEndAt.timetuple()) - getServerUTCTime())
        return

    def _finalize(self):
        self._uiLogger.stop()
        super(EventBannerTooltip, self)._finalize()
