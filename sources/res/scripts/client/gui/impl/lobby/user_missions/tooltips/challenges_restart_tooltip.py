# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/user_missions/tooltips/challenges_restart_tooltip.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/user_missions/tooltips/challenges_restart_tooltip.py
from __future__ import absolute_import
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.user_missions.tooltips.challenges_restart_tooltip_model import ChallengesRestartTooltipModel
from gui.impl.pub import ViewImpl
from shared_utils import first

class ChallengesRestartTooltip(ViewImpl):

    def __init__(self, challenge):
        settings = ViewSettings(R.views.mono.user_missions.tooltips.challenges_restart_tooltip())
        settings.model = ChallengesRestartTooltipModel()
        super(ChallengesRestartTooltip, self).__init__(settings)
        self.__challenge = challenge

    @property
    def viewModel(self):
        return super(ChallengesRestartTooltip, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        super(ChallengesRestartTooltip, self)._onLoading(*args, **kwargs)
        with self.viewModel as model:
            model.setFreeRestarts(self.__challenge.freeRestartsPerCompletion)
            model.setUsedFreeRestarts(self.__challenge.usedFreeRestarts)
            currency, cost = first(self.__challenge.restartPrice.items())
            model.setCurrency(currency)
            model.setRestartCost(cost)
