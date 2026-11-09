# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/Scaleform/daapi/view/lobby/tooltips/comp7_selector_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from comp7.gui.shared.tooltips import TOOLTIP_TYPE as TOOLTIP_TYPE
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.formatters import text_styles as text_styles
from gui.shared.tooltips import formatters as formatters
from gui.shared.tooltips.battle_selector import SeasonalBattleSelectorTooltip as SeasonalBattleSelectorTooltip
from gui.shared.tooltips.common import BlocksTooltipData as BlocksTooltipData
from helpers import dependency as dependency, time_utils as time_utils
from skeletons.gui.game_control import IComp7Controller as IComp7Controller
_R_COMP7_SELECTOR_TOOLTIP = R.strings.comp7_ext.selectorTooltip
_TOOLTIP_MIN_WIDTH = 280

class Comp7SelectorTooltip(SeasonalBattleSelectorTooltip):
    _battleController: Any
    _TOOLTIP_TYPE = TOOLTIP_TYPE.COMP7_SELECTOR_INFO
    _TOOLTIP_WIDTH = _TOOLTIP_MIN_WIDTH
    _R_BATTLE_SELECTOR_STR = R.strings.comp7_ext.seasonalBattleSelector
    @staticmethod
    def _getTitle():
        ...
    @staticmethod
    def _getDescription():
        ...

class Comp7SelectorUnavailableTooltip(BlocksTooltipData):
    __comp7Controller: Any
    def __init__(self, context):
        ...
    def _packBlocks(self, *_, **__):
        ...
    @staticmethod
    def _packHeaderBlock():
        ...
    @classmethod
    def _packInfoBlock(cls):
        ...
