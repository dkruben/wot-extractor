# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/impl/lobby/views/quests_packer.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from battle_royale.gui.impl.lobby.views.bonus_packer import getBonusPacker as getBonusPacker
import constants as constants
from gui.impl.gen.view_models.common.missions.daily_quest_model import DailyQuestModel as DailyQuestModel
from gui.shared.missions.packers.bonus import BonusUIPacker as BonusUIPacker
from gui.shared.missions.packers.events import BattleQuestUIDataPacker as BattleQuestUIDataPacker, packQuestBonusModelAndTooltipData as packQuestBonusModelAndTooltipData, findFirstConditionModel as findFirstConditionModel
from gui.server_events.formatters import DECORATION_SIZES as DECORATION_SIZES
from skeletons.gui.server_events import IEventsCache as IEventsCache
from helpers import dependency as dependency
from gui.impl.gen.view_models.common.missions.conditions.preformatted_condition_model import PreformattedConditionModel as PreformattedConditionModel
_logger: Any

class BRDailyQuestUIDataPacker(BattleQuestUIDataPacker):
    eventsCache: Any
    _tooltipData: Any
    def _packBonuses(self, model):
        ...
    def pack(self, model=None):
        ...
    def __resolveQuestIcon(self, model):
        ...

def getEventUIDataPacker(event):
    ...
