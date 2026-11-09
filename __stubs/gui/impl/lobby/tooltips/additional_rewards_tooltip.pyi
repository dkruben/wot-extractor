# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/tooltips/additional_rewards_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from frameworks.wulf import ViewSettings as ViewSettings
from frameworks.wulf.view.array import fillViewModelsArray as fillViewModelsArray
from gui.impl.gen import R as R
from gui.impl.gen.view_models.common.missions.bonuses.icon_bonus_model import IconBonusModel as IconBonusModel
from gui.impl.gen.view_models.views.lobby.tooltips.additional_rewards_tooltip_model import AdditionalRewardsTooltipModel as AdditionalRewardsTooltipModel
from gui.impl.pub import ViewImpl as ViewImpl
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE, GUI_ITEM_TYPE_NAMES as GUI_ITEM_TYPE_NAMES

class AdditionalRewardsTooltip(ViewImpl):
    __slots__: tuple
    def __init__(self, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, packedBonuses, showCount=0, *args, **kwargs):
        ...
    @classmethod
    def _getHeader(cls):
        ...
    @classmethod
    def _getHeaderWithCount(cls):
        ...
    @classmethod
    def _getHeaderCount(cls):
        ...
    @staticmethod
    def _fillBonusesArray(bonusModels, array):
        ...

class AdditionalBattlePassRewardsTooltip(ViewImpl):
    def __init__(self, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, packedBonuses, *args, **kwargs):
        ...
