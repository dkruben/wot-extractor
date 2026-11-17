# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/tooltips/ranked/ranked_selectable_reward_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.tooltips.common import BlocksTooltipData as BlocksTooltipData
from gui.shared.formatters import text_styles as text_styles
from gui.shared.tooltips import TOOLTIP_TYPE as TOOLTIP_TYPE, formatters as formatters
from gui.Scaleform.genConsts.BLOCKS_TOOLTIP_TYPES import BLOCKS_TOOLTIP_TYPES as BLOCKS_TOOLTIP_TYPES

class RankedSelectableRewardTooltip(BlocksTooltipData):
    _items: Any
    def __init__(self, context):
        ...
    def _packBlocks(self, *args, **kwargs):
        ...
    @staticmethod
    def __packImageBlock():
        ...
    @staticmethod
    def __packRewardNamesBlock():
        ...
    @staticmethod
    def __packLimitBlock():
        ...
