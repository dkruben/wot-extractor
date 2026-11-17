# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/tooltips/ranked/ranked_quests_preview_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import listvalues as listvalues
from gui.impl.gen import R as R
from gui.impl import backport as backport
from gui.Scaleform.genConsts.BLOCKS_TOOLTIP_TYPES import BLOCKS_TOOLTIP_TYPES as BLOCKS_TOOLTIP_TYPES
from gui.server_events.events_helpers import isRankedDaily as isRankedDaily, EventInfoModel as EventInfoModel
from gui.server_events.awards_formatters import AWARDS_SIZES as AWARDS_SIZES, getDefaultAwardFormatter as getDefaultAwardFormatter
from gui.shared.formatters import text_styles as text_styles, icons as icons
from gui.shared.tooltips import TOOLTIP_TYPE as TOOLTIP_TYPE, formatters as formatters
from gui.shared.tooltips.common import BlocksTooltipData as BlocksTooltipData
from helpers import dependency as dependency, time_utils as time_utils
from skeletons.gui.game_control import IRankedBattlesController as IRankedBattlesController
from skeletons.gui.server_events import IEventsCache as IEventsCache
_TOOLTIP_WIDTH = 322
_MAX_VISIBLE_QUESTS = 3

class RankedQuestsPreviewTooltip(BlocksTooltipData):
    __eventsCache: Any
    __rankedController: Any
    def __init__(self, context):
        ...
    def _packBlocks(self, *args, **kwargs):
        ...
    def __packBottom(self, diff):
        ...
    def __packDescription(self, quests, season, isLeagues, isAnyPrimeNow, isAnyPrimeLeftTotal):
        ...
    def __packHeader(self, description):
        ...
    def __packQuest(self, quest, isGlobalAvailable, awardsFormatter):
        ...
    def __packQuestInfo(self, quest, isGlobalAvailable):
        ...
    def __packQuestRewards(self, quest, awardsFormatter):
        ...
    def __packSingleReward(self, bonus):
        ...
