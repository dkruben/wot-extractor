# wot-extractor: codigo DESCOMPILADO de sources/res/last_stand/scripts/client/last_stand/gui/impl/lobby/tooltips/event_banner_tooltip.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: last_stand/scripts/client/last_stand/gui/impl/lobby/tooltips/event_banner_tooltip.py
from __future__ import absolute_import
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.common.mode_performance_model import PerformanceRiskEnum
from gui.impl.pub import ViewImpl
from helpers import dependency, time_utils
from last_stand.gui.impl.gen.view_models.views.lobby.event_banner_view_model import EventBannerViewModel
from last_stand.gui.shared.utils.performance_analyzer import PerformanceGroup
from last_stand.skeletons.ls_controller import ILSController
PERFORMANCE_MAP = {(PerformanceGroup.LOW_RISK): (PerformanceRiskEnum.LOWRISK), 
   (PerformanceGroup.MEDIUM_RISK): (PerformanceRiskEnum.MEDIUMRISK), 
   (PerformanceGroup.HIGH_RISK): (PerformanceRiskEnum.HIGHRISK)}

class EventBannerTooltipView(ViewImpl):
    lsCtrl = dependency.descriptor(ILSController)
    __slots__ = ('__performanceRisk', )

    def __init__(self, layoutID=R.views.last_stand.mono.lobby.tooltips.banner_tooltip()):
        settings = ViewSettings(layoutID)
        settings.model = EventBannerViewModel()
        super(EventBannerTooltipView, self).__init__(settings)

    @property
    def viewModel(self):
        return super(EventBannerTooltipView, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        super(EventBannerTooltipView, self)._onLoading(*args, **kwargs)
        with self.getViewModel().transaction() as model:
            model.setPerformanceRisk(PERFORMANCE_MAP.get(self.lsCtrl.getPerformanceGroup(), PerformanceRiskEnum.LOWRISK))
            model.setDate(time_utils.getServerUTCTime())
            model.setEndDate(self.lsCtrl.getModeSettings().endDate)
