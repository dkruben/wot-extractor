# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/tooltips/ranked/rank_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.genConsts.BLOCKS_TOOLTIP_TYPES import BLOCKS_TOOLTIP_TYPES as BLOCKS_TOOLTIP_TYPES
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.ranked_battles.constants import ZERO_RANK_ID as ZERO_RANK_ID
from gui.ranked_battles.ranked_formatters import getRankedAwardsFormatter as getRankedAwardsFormatter
from gui.shared.formatters import text_styles as text_styles
from gui.shared.tooltips import TOOLTIP_TYPE as TOOLTIP_TYPE, formatters as formatters
from gui.shared.tooltips.common import BlocksTooltipData as BlocksTooltipData
from helpers import dependency as dependency
from skeletons.gui.game_control import IRankedBattlesController as IRankedBattlesController
from gui.Scaleform.genConsts.RANKEDBATTLES_ALIASES import RANKEDBATTLES_ALIASES as RANKEDBATTLES_ALIASES
_TOOLTIP_MIN_WIDTH = 364
_AWARD_STEP = 63
_AWARDS_RIGHT_PADDING = 25

class RankedTooltipData(BlocksTooltipData):
    rankedController: Any
    __shieldStatus: Any
    item: Any
    def __init__(self, context):
        ...
    def _packBlocks(self, *args, **kwargs):
        ...
    def __getQualificationQuest(self):
        ...
    def __packTitle(self):
        ...
    def __packComment(self):
        ...
    def __getDivisionComment(self):
        ...
    def __getShieldComment(self):
        ...
    def __getUnburnableComment(self):
        ...
    def __packStepsBlock(self):
        ...
    def __packStatusBlock(self):
        ...
    def __packAwardsBlock(self, quest):
        ...
