# wot-extractor: codigo DESCOMPILADO de sources/res/open_bundle/scripts/client/open_bundle/gui/impl/lobby/tooltips/fixed_rewards_tooltip.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: open_bundle/scripts/client/open_bundle/gui/impl/lobby/tooltips/fixed_rewards_tooltip.py
from __future__ import absolute_import
from future.utils import viewvalues
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.pub import ViewImpl
from helpers import dependency
from open_bundle.gui.impl.gen.view_models.views.lobby.tooltips.fixed_rewards_tooltip_model import FixedRewardsTooltipModel
from open_bundle.gui.impl.gen.view_models.views.lobby.tooltips.step_model import StepModel
from open_bundle.helpers.bonuses.bonus_packers import composeBonuses, packBonusModelAndTooltipData
from open_bundle.skeletons.open_bundle_controller import IOpenBundleController

class FixedRewardsTooltip(ViewImpl):
    __openBundle = dependency.descriptor(IOpenBundleController)

    def __init__(self, bundle):
        settings = ViewSettings(R.views.open_bundle.mono.lobby.tooltips.fixed_rewards())
        settings.model = FixedRewardsTooltipModel()
        super(FixedRewardsTooltip, self).__init__(settings)
        self.__bundle = bundle

    @property
    def viewModel(self):
        return super(FixedRewardsTooltip, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        super(FixedRewardsTooltip, self)._onLoading(*args, **kwargs)
        with self.getViewModel().transaction() as model:
            model.setBundleType(self.__bundle.type)
            self.__fillStepsFixedRewards(model)

    def __fillStepsFixedRewards(self, model):
        steps = model.getSteps()
        steps.clear()
        for stepInfo in viewvalues(self.__bundle.steps):
            stepModel = StepModel()
            stepModel.setStepNumber(stepInfo.number)
            self.__fillBonuses(stepModel, stepInfo)
            steps.addViewModel(stepModel)

        steps.invalidate()

    def __fillBonuses(self, stepModel, stepInfo):
        bonuses = composeBonuses([stepInfo.fixedBonus])
        rewardModels = stepModel.getFixedRewards()
        rewardModels.clear()
        packBonusModelAndTooltipData(bonuses, rewardModels)
