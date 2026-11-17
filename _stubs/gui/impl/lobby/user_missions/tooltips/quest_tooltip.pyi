# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/user_missions/tooltips/quest_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.user_missions.widget.widget_quest_model import WidgetQuestModel as WidgetQuestModel
from gui.impl.pub import ViewImpl as ViewImpl
from gui.shared.missions.packers.bonus import weeklyBonusSortKey as weeklyBonusSortKey
from gui.shared.missions.packers.events import packQuestBonusModel as packQuestBonusModel
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache

class BaseQuestTooltip(ViewImpl):
    _itemsCache: Any
    _quest: Any
    _tooltipData: Any
    def __init__(self, quest):
        ...
    def _getSettings(self):
        ...
    def _finalize(self):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _fillViewModel(self):
        ...
    def _packBonuses(self, model, data, bonusPacker):
        ...
    def _getRewardsSortKey(self):
        ...

class DailyQuestTooltip(BaseQuestTooltip):
    def _getSettings(self):
        ...
    def _getRewardsSortKey(self):
        ...

class WeeklyQuestTooltip(BaseQuestTooltip):
    def _getSettings(self):
        ...
    def _getRewardsSortKey(self):
        ...
