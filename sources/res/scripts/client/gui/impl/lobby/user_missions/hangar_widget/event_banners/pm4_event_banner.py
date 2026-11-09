# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/user_missions/hangar_widget/event_banners/pm4_event_banner.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/user_missions/hangar_widget/event_banners/pm4_event_banner.py
from __future__ import absolute_import
from account_helpers.settings_core.settings_constants import PersonalMission4
from gui.impl import backport
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.user_missions.constants.event_banner_state import EventBannerState
from gui.impl.lobby.personal_missions_30.personal_mission_constants import OperationIDs
from gui.impl.lobby.personal_missions_30.views_helpers import isPM4BannerAnimationShown, isIntroShown, markPM4BannerAnimationShown
from gui.impl.lobby.user_missions.hangar_widget.event_banners.standard_event_banner import StandardEventBanner
from gui.impl.lobby.user_missions.tooltips.pm4_banner_tooltip import PM4BannerTooltipView
from gui.shared.event_dispatcher import showPersonalMissionMainWindow
from personal_missions import PM_BRANCH

class PM4EventBunner(StandardEventBanner):
    NAME = 'PM4EntryPoint'

    @property
    def playAppearAnim(self):
        return not isPM4BannerAnimationShown()

    @property
    def bannerState(self):
        return EventBannerState.INTRO

    @property
    def introDescription(self):
        return backport.text(R.strings.hangar_event_banners.event.PM4EntryPoint.description())

    @property
    def borderColor(self):
        if isIntroShown(PersonalMission4.INTRO_OP_11, PM_BRANCH.PERSONAL_MISSION_4):
            return ''
        return '#00FFAE'

    def createToolTipContent(self, event):
        return PM4BannerTooltipView()

    def onAppearAnimationPlayed(self):
        markPM4BannerAnimationShown()

    def onClick(self):
        showPersonalMissionMainWindow(OperationIDs.OPERATION_FOURTH.value)
