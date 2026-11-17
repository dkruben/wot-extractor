# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/veh_skill_tree/tooltips/prestige_reward_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.lobby.common.view_helpers import packBonusModelAndTooltipData as packBonusModelAndTooltipData
from gui.impl.lobby.vehicle_hub.sub_presenters.veh_skill_tree.utils import getVehSkillTreeRewardTooltipViewBonusPacker as getVehSkillTreeRewardTooltipViewBonusPacker
from gui.impl.gen.view_models.views.lobby.veh_skill_tree.tooltips.prestige_reward_tooltip_model import PrestigeRewardTooltipModel as PrestigeRewardTooltipModel

class PrestigeRewardTooltipView(ViewImpl):
    def __init__(self, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, bonus, *args, **kwargs):
        ...
