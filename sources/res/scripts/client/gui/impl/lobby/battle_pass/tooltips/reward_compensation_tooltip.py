# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/battle_pass/tooltips/reward_compensation_tooltip.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/battle_pass/tooltips/reward_compensation_tooltip.py
from __future__ import absolute_import
from frameworks.wulf import ViewSettings
from gui.battle_pass.battle_pass_bonuses_packers import packBonusModelAndTooltipData
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.battle_pass.tooltips.reward_compensation_tooltip_model import RewardCompensationTooltipModel
from gui.impl.pub import ViewImpl

class RewardCompensationTooltip(ViewImpl):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        settings = ViewSettings(R.views.mono.battle_pass.tooltips.reward_compensation(), model=RewardCompensationTooltipModel(), args=args, kwargs=kwargs)
        super(RewardCompensationTooltip, self).__init__(settings)

    @property
    def viewModel(self):
        return super(RewardCompensationTooltip, self).getViewModel()

    def _onLoading(self, initialBonus, compensationBonus, *args, **kwargs):
        with self.viewModel.transaction() as model:
            packBonusModelAndTooltipData([initialBonus], model.initialReward)
            packBonusModelAndTooltipData([compensationBonus], model.compensationReward)
