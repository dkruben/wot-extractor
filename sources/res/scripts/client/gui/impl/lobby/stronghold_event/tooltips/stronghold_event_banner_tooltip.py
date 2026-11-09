# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/stronghold_event/tooltips/stronghold_event_banner_tooltip.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/stronghold_event/tooltips/stronghold_event_banner_tooltip.py
from frameworks.wulf import ViewSettings
from gui.impl.gen.view_models.views.lobby.stronghold_event.stronghold_event_banner_tooltip_view_model import StrongholdEventBannerTooltipViewModel
from gui.impl.pub import ViewImpl
from gui.impl.gen import R

class StrongholdEventBannerTooltip(ViewImpl):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        settings = ViewSettings(R.views.mono.stronghold_event.tooltips.event_banner_tooltip())
        settings.model = StrongholdEventBannerTooltipViewModel()
        settings.args = args
        settings.kwargs = kwargs
        super(StrongholdEventBannerTooltip, self).__init__(settings)

    @property
    def viewModel(self):
        return super(StrongholdEventBannerTooltip, self).getViewModel()

    def _onLoading(self, state, startDate, endDate):
        with self.viewModel.transaction() as vm:
            vm.setState(state)
            vm.setStartDate(startDate)
            vm.setEndDate(endDate)
