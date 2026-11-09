# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/user_missions/tooltips/daily_reroll_tooltip.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/user_missions/tooltips/daily_reroll_tooltip.py
from __future__ import absolute_import
from frameworks.wulf.view.view import ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.user_missions.tooltips.daily_reroll_tooltip_model import DailyRerollTooltipModel
from gui.impl.pub import ViewImpl

class DailyRerollTooltip(ViewImpl):
    __slots__ = ('_timeLeft', '_rerollInterval')

    def __init__(self, timeLeft, rerollInterval):
        self._timeLeft = timeLeft
        self._rerollInterval = rerollInterval
        settings = ViewSettings(R.views.mono.user_missions.tooltips.daily_reroll_tooltip(), model=DailyRerollTooltipModel())
        super(DailyRerollTooltip, self).__init__(settings)

    @property
    def viewModel(self):
        return super(DailyRerollTooltip, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        self.viewModel.setTimeLeft(self._timeLeft)
        self.viewModel.setRerollInterval(self._rerollInterval)
