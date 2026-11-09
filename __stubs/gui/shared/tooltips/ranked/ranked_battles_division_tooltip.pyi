# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/tooltips/ranked/ranked_battles_division_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.formatters import text_styles as text_styles
from gui.shared.tooltips import TOOLTIP_TYPE as TOOLTIP_TYPE
from gui.shared.tooltips import formatters as formatters
from gui.shared.tooltips.common import BlocksTooltipData as BlocksTooltipData
from helpers import dependency as dependency
from shared_utils import findFirst as findFirst
from skeletons.gui.game_control import IRankedBattlesController as IRankedBattlesController
_TOOLTIP_MIN_WIDTH = 364
_TOOLTIP_ICON_SIZE = 56

class RankedDivisionTooltip(BlocksTooltipData):
    rankedController: Any
    def __init__(self, ctx):
        ...
    def _packBlocks(self, divisionId, isCurrent, isLocked, isCompleted):
        ...
    def _getDescriptionBlock(self, division, isLocked, isCompleted):
        ...
    @staticmethod
    def _getStatusBlock(division, isLocked, isCompleted):
        ...
    def _getTitleBlock(self, division):
        ...
