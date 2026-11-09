# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/tooltips/ranked/ranked_year_reward_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.genConsts.BLOCKS_TOOLTIP_TYPES import BLOCKS_TOOLTIP_TYPES as BLOCKS_TOOLTIP_TYPES
from gui.Scaleform.genConsts.ICON_TEXT_FRAMES import ICON_TEXT_FRAMES as ICON_TEXT_FRAMES
from gui.Scaleform.genConsts.RANKEDBATTLES_CONSTS import RANKEDBATTLES_CONSTS as _RBC
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.ranked_battles.ranked_formatters import getRankedAwardsFormatter as getRankedAwardsFormatter, rankedYearAwardsSortFunction as rankedYearAwardsSortFunction
from gui.selectable_reward.constants import SELECTABLE_BONUS_NAME as SELECTABLE_BONUS_NAME
from gui.shared.formatters import text_styles as text_styles
from gui.shared.tooltips import TOOLTIP_TYPE as TOOLTIP_TYPE, formatters as formatters
from gui.shared.tooltips.common import BlocksTooltipData as BlocksTooltipData
from helpers import dependency as dependency
from shared_utils import findFirst as findFirst, first as first
from skeletons.gui.game_control import IRankedBattlesController as IRankedBattlesController
from gui.server_events.awards_formatters import AWARDS_SIZES as AWARDS_SIZES
_TOOLTIP_MIN_WIDTH = 442
_AWARD_STEP = 63
_AWARDS_RIGHT_PADDING = 25

class RankedYearReward(BlocksTooltipData):
    __rankedController: Any
    __points: Any
    def __init__(self, context):
        ...
    def _packBlocks(self, boxType, status, *args, **kwargs):
        ...
    def __packAwardBlock(self, formattedBonuses):
        ...
    def __packTitleBlock(self, boxType):
        ...
    def __packPointsBlock(self):
        ...
    def __packEquipmentChoiceBlock(self, equipmentCount):
        ...
    def __packStatusBlock(self, status):
        ...
