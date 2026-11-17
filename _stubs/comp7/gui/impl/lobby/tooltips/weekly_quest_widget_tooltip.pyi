# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/tooltips/weekly_quest_widget_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from comp7.gui.impl.gen.view_models.views.lobby.tooltips.weekly_quest_widget_tooltip_model import WeeklyQuestWidgetTooltipModel as WeeklyQuestWidgetTooltipModel, State as State
from comp7.gui.impl.lobby.comp7_helpers.comp7_bonus_packer import getComp7BonusPacker as getComp7BonusPacker, packQuestBonuses as packQuestBonuses
from comp7.gui.shared.missions.packers.events import Comp7WeeklyQuestPacker as Comp7WeeklyQuestPacker
from comp7.skeletons.gui.game_control import IComp7WeeklyQuestsController as IComp7WeeklyQuestsController
from frameworks.wulf import ViewSettings as ViewSettings
from frameworks.wulf.view.array import fillViewModelsArray as fillViewModelsArray, fillIntsArray as fillIntsArray
from gui.impl.gen import R as R
from gui.impl.pub import ViewImpl as ViewImpl
from helpers import dependency as dependency

class WeeklyQuestWidgetTooltip(ViewImpl):
    __comp7WeeklyQuestsCtrl: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self):
        ...
    def __updateModel(self):
        ...
    def __getQuestsState(self):
        ...
