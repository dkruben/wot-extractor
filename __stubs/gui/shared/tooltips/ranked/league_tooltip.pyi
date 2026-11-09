# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/tooltips/ranked/league_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.shared.formatters import text_styles as text_styles
from gui.shared.tooltips import TOOLTIP_TYPE as TOOLTIP_TYPE, formatters as formatters
from gui.shared.tooltips.common import BlocksTooltipData as BlocksTooltipData
from gui.impl import backport as backport
from gui.impl.gen import R as R
from helpers import dependency as dependency
from gui.ranked_battles import ranked_formatters as ranked_formatters
from skeletons.gui.game_control import IRankedBattlesController as IRankedBattlesController
from gui.Scaleform.genConsts.BLOCKS_TOOLTIP_TYPES import BLOCKS_TOOLTIP_TYPES as BLOCKS_TOOLTIP_TYPES
from gui.ranked_battles.ranked_helpers.web_season_provider import UNDEFINED_LEAGUE_ID as UNDEFINED_LEAGUE_ID

class BonusTooltipData(BlocksTooltipData):
    __rankedController: Any
    def __init__(self, context):
        ...
    def _packBlocks(self, *args, **kwargs):
        ...
    def __packPersistentCount(self, persistentCount):
        ...
    def __packDailyCount(self, dailyCount, income):
        ...

class LeagueTooltipData(BlocksTooltipData):
    __rankedController: Any
    def __init__(self, context):
        ...
    def _packBlocks(self, *args, **kwargs):
        ...

class EfficiencyTooltipData(BlocksTooltipData):
    __rankedController: Any
    def __init__(self, context):
        ...
    def _packBlocks(self, *args, **kwargs):
        ...
    def __getEfficiencyBlock(self, efficiency, updateTime, resID):
        ...

class PositionTooltipData(BlocksTooltipData):
    __rankedController: Any
    def __init__(self, context):
        ...
    def _packBlocks(self, *args, **kwargs):
        ...
