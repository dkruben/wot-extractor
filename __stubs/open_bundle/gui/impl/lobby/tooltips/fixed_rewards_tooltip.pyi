# wot-extractor: STUB (.pyi) gerado a partir de sources/res/open_bundle/scripts/client/open_bundle/gui/impl/lobby/tooltips/fixed_rewards_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewvalues as viewvalues
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.pub import ViewImpl as ViewImpl
from helpers import dependency as dependency
from open_bundle.gui.impl.gen.view_models.views.lobby.tooltips.fixed_rewards_tooltip_model import FixedRewardsTooltipModel as FixedRewardsTooltipModel
from open_bundle.gui.impl.gen.view_models.views.lobby.tooltips.step_model import StepModel as StepModel
from open_bundle.helpers.bonuses.bonus_packers import composeBonuses as composeBonuses, packBonusModelAndTooltipData as packBonusModelAndTooltipData
from open_bundle.skeletons.open_bundle_controller import IOpenBundleController as IOpenBundleController

class FixedRewardsTooltip(ViewImpl):
    __openBundle: Any
    __bundle: Any
    def __init__(self, bundle):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def __fillStepsFixedRewards(self, model):
        ...
    def __fillBonuses(self, stepModel, stepInfo):
        ...
