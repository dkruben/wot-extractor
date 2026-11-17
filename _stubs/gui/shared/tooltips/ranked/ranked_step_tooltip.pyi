# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/tooltips/ranked/ranked_step_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.genConsts.BLOCKS_TOOLTIP_TYPES import BLOCKS_TOOLTIP_TYPES as BLOCKS_TOOLTIP_TYPES
from gui.Scaleform.genConsts.RANKEDBATTLES_ALIASES import RANKEDBATTLES_ALIASES as RANKEDBATTLES_ALIASES
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.formatters import text_styles as text_styles
from gui.shared.tooltips import TOOLTIP_TYPE as TOOLTIP_TYPE
from gui.shared.tooltips import formatters as formatters
from gui.shared.tooltips.common import BlocksTooltipData as BlocksTooltipData
from helpers import dependency as dependency
from skeletons.gui.game_control import IRankedBattlesController as IRankedBattlesController
_TOOLTIP_MIN_WIDTH = 320

class RankedStepTooltip(BlocksTooltipData):
    rankedController: Any
    def __init__(self, ctx):
        ...
    def _packBlocks(self, *args):
        ...
    def _packHeaderBlock(self):
        ...
    def _packReceivedBlock(self, winEarnedCount, loseEarnedCount):
        ...
    def _packNotReceivedBlock(self, winEarnedCount, winNotReceivedCount, loseEarnedCount, loseNotReceivedCount):
        ...
    def _packLostBlock(self, totalPlayers, winLostCount, loseLostCount):
        ...
    def _getConditionStr(self, strResID, topValue, fromPlace, tillPlace):
        ...
    def _getFromTillPlaceStr(self, formatter, fromPlace, tillPlace):
        ...
    def _getConditionBlock(self, topValue=0, fromPlaceValue=1, placesCount=0, condition=None, conditionTop=None):
        ...
    def _getConditionHeaderBlock(self, strValue):
        ...
    def _getOrBlock(self, padding=None):
        ...
