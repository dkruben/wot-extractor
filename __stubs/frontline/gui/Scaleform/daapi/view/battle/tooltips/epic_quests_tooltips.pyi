# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline/gui/Scaleform/daapi/view/battle/tooltips/epic_quests_tooltips.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from gui.Scaleform.genConsts.BLOCKS_TOOLTIP_TYPES import BLOCKS_TOOLTIP_TYPES as BLOCKS_TOOLTIP_TYPES
from gui.impl import backport as backport
from gui.impl.backport import getTillTimeStringByRClass as getTimeStr
from gui.impl.gen import R as R
from gui.server_events.awards_formatters import AWARDS_SIZES as AWARDS_SIZES, getEpicViewAwardPacker as getEpicViewAwardPacker
from gui.server_events.events_helpers import isDailyEpic as isDailyEpic
from gui.shared.formatters import text_styles as text_styles, icons as icons
from gui.shared.tooltips import TOOLTIP_TYPE as TOOLTIP_TYPE, formatters as formatters
from gui.shared.tooltips.common import BlocksTooltipData as BlocksTooltipData
from helpers import dependency as dependency, time_utils as time_utils
from skeletons.gui.game_control import IEpicBattleMetaGameController as IEpicBattleMetaGameController, IQuestsController as IQuestsController
_R_EPIC_BATTLE = R.strings.epic_battle.questsTooltip.epicBattle

class EpicBattleQuestsTooltipData(BlocksTooltipData):
    __questController: Any
    __epicController: Any
    __slots__: tuple
    def __init__(self, context):
        ...
    def _packBlocks(self, *args, **kwargs):
        ...
    def _packHeader(self, quests):
        ...
    @classmethod
    def _isQuestCompleted(cls, quest):
        ...
    def __packQuest(self, quest):
        ...
    def __packQuestInfo(self, quest):
        ...
    def __packQuestRewards(self, quest):
        ...
    def __packQuestReward(self, bonus):
        ...
    def __formatDescription(self, quests):
        ...
    def __getQuestForVehicle(self, vehicle, sortByPriority=False, questIDs=None):
        ...

class CompletedQuestsTooltipData(EpicBattleQuestsTooltipData):
    def _packHeader(self, quests):
        ...
    @classmethod
    def _isQuestCompleted(cls, _):
        ...
