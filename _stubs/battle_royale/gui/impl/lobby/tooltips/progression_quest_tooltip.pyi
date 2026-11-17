# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/impl/lobby/tooltips/progression_quest_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from battle_royale.gui.impl.lobby.views.bonus_packer import getBonusPacker as getBonusPacker, packMissionItem as packMissionItem, packQuestBonuses as packQuestBonuses
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.user_missions.widget.widget_quest_model import WidgetQuestModel as WidgetQuestModel
from gui.impl.lobby.user_missions.tooltips.quest_tooltip import BaseQuestTooltip as BaseQuestTooltip
from frameworks.wulf import ViewSettings as ViewSettings
from frameworks.wulf.view.array import fillViewModelsArray as fillViewModelsArray
from gui.shared.missions.packers.events import DailyQuestUIDataPacker as DailyQuestUIDataPacker
from helpers import dependency as dependency
from skeletons.gui.game_control import IBattleRoyaleController as IBattleRoyaleController

class BattleRoyaleProgressionQuestTooltip(BaseQuestTooltip):
    __battleRoyale: Any
    def _getSettings(self):
        ...
    def _fillViewModel(self):
        ...
    def _getRewardsSortKey(self):
        ...
