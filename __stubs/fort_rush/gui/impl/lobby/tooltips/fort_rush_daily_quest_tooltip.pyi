# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/client/fort_rush/gui/impl/lobby/tooltips/fort_rush_daily_quest_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from fort_rush.gui.impl.lobby.bonus_packers import getFortRushMissionBonusPacker as getFortRushMissionBonusPacker
from fort_rush.gui.impl.lobby.quest_packers import FortRushDailyQuestUIDataPacker as FortRushDailyQuestUIDataPacker
from fort_rush.skeletons.battle_controller import IFortRushBattleController as IFortRushBattleController
from frameworks.wulf import ViewSettings as ViewSettings
from gui.Scaleform.genConsts.MISSIONS_STATES import MISSIONS_STATES as MISSIONS_STATES
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.user_missions.widget.widget_quest_model import WidgetQuestModel as WidgetQuestModel
from gui.impl.lobby.user_missions.tooltips.quest_tooltip import BaseQuestTooltip as BaseQuestTooltip
from gui.shared.missions.packers.events import findFirstConditionModel as findFirstConditionModel, packQuestBonusModelAndTooltipData as packQuestBonusModelAndTooltipData
from helpers import dependency as dependency
from helpers.time_utils import getDayTimeLeft as getDayTimeLeft

class FortRushProgressionQuestTooltip(BaseQuestTooltip):
    __ctrl: Any
    def _getSettings(self):
        ...
    def _getRewardsSortKey(self):
        ...
    def _fillViewModel(self):
        ...
    @staticmethod
    def __getFirstConditionModel(questModel):
        ...
