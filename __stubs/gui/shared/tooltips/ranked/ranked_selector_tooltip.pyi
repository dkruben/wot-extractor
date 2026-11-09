# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/tooltips/ranked/ranked_selector_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.formatters import text_styles as text_styles
from gui.shared.tooltips import formatters as formatters, TOOLTIP_TYPE as TOOLTIP_TYPE
from gui.shared.tooltips.battle_selector import SeasonalBattleSelectorTooltip as SeasonalBattleSelectorTooltip
from gui.shared.tooltips.common import BlocksTooltipData as BlocksTooltipData
from helpers import dependency as dependency, time_utils as time_utils
from skeletons.gui.game_control import IRankedBattlesController as IRankedBattlesController
_TOOLTIP_MIN_WIDTH = 280

class RankedSelectorTooltip(SeasonalBattleSelectorTooltip):
    _battleController: Any
    _TOOLTIP_TYPE = TOOLTIP_TYPE.RANKED_SELECTOR_INFO
    _TOOLTIP_WIDTH = _TOOLTIP_MIN_WIDTH
    @staticmethod
    def _getTitle():
        ...
    @staticmethod
    def _getDescription():
        ...

class RankedUnavailableTooltip(BlocksTooltipData):
    rankedController: Any
    def __init__(self, context):
        ...
    def _packBlocks(self, *args, **kwargs):
        ...
