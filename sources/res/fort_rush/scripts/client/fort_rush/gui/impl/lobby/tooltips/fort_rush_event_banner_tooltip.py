# wot-extractor: codigo DESCOMPILADO de sources/res/fort_rush/scripts/client/fort_rush/gui/impl/lobby/tooltips/fort_rush_event_banner_tooltip.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fort_rush/scripts/client/fort_rush/gui/impl/lobby/tooltips/fort_rush_event_banner_tooltip.py
from __future__ import absolute_import
from fort_rush.gui.impl.gen.view_models.views.lobby.fort_rush_event_banner_view_model import FortRushEventBannerViewModel, State, PerformanceRiskEnum
from fort_rush.gui.impl.lobby.mode_selector.fort_rush_mode_selector_item import PERFORMANCE_MAP
from fort_rush.skeletons.battle_controller import IFortRushBattleController
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.user_missions.constants.event_banner_state import EventBannerState
from gui.impl.pub import ViewImpl
from helpers import dependency, time_utils
_BANNER_STATE_TO_TOOLTIP_STATE = {(EventBannerState.INACTIVE): (State.FROZEN), 
   (EventBannerState.INTRO): (State.INTRO), 
   (EventBannerState.IN_PROGRESS): (State.INPROGRESS)}

class FortRushEventBannerTooltipView(ViewImpl):
    __frCtrl = dependency.descriptor(IFortRushBattleController)

    def __init__(self, bannerState=EventBannerState.INACTIVE):
        self.__bannerState = bannerState
        settings = ViewSettings(R.views.fort_rush.mono.lobby.tooltips.banner_tooltip())
        settings.model = FortRushEventBannerViewModel()
        super(FortRushEventBannerTooltipView, self).__init__(settings)

    @property
    def viewModel(self):
        return super(FortRushEventBannerTooltipView, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        super(FortRushEventBannerTooltipView, self)._onLoading(*args, **kwargs)
        with self.viewModel.transaction() as model:
            ctrl = self.__frCtrl
            group = ctrl.getPerformanceGroup()
            model.setPerformanceRisk(PERFORMANCE_MAP.get(group, PerformanceRiskEnum.LOWRISK))
            model.setDate(time_utils.getServerUTCTime())
            model.setEndDate(time_utils.getTimestampFromUTC(ctrl.getConfig().endDatetime.timetuple()))
            tooltipState = _BANNER_STATE_TO_TOOLTIP_STATE.get(self.__bannerState, State.FROZEN)
            model.setState(tooltipState)
            if not ctrl.isProgressionCompleted():
                currentPoints, stageTotal = ctrl.getCurrentStagePoints()
                model.setCurPoints(currentPoints)
                model.setMaxPoints(stageTotal)
                model.setCurLevel(ctrl.getCurrentStageIndex())
                model.setMaxLevel(len(ctrl.getConfig().progression.stage))
