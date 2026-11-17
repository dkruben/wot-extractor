# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline/gui/Scaleform/daapi/view/lobby/tooltips/frontline.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui import makeHtmlString as makeHtmlString
from gui.Scaleform.genConsts.BLOCKS_TOOLTIP_TYPES import BLOCKS_TOOLTIP_TYPES as BLOCKS_TOOLTIP_TYPES
from gui.Scaleform.locale.EPIC_BATTLE import EPIC_BATTLE as EPIC_BATTLE
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS as TOOLTIPS
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.formatters import text_styles as text_styles, icons as icons
from gui.shared.money import Currency as Currency
from gui.shared.tooltips import TOOLTIP_TYPE as TOOLTIP_TYPE, formatters as formatters
from gui.shared.tooltips.common import BlocksTooltipData as BlocksTooltipData
from helpers import dependency as dependency
from helpers.i18n import makeString as _ms
from skeletons.gui.game_control import ITradeInController as ITradeInController, IEpicBattleMetaGameController as IEpicBattleMetaGameController
_R_EPIC_BATTLE = R.strings.epic_battle.questsTooltip.epicBattle
_PREVIEW_TOOLTIP_WIDTH = 350
_GIFTS_WIDTH = 265
_RANK_TOOLTIP_WIDTH = 330
_RANK_ICONS: list

class FrontlinePackPreviewTooltipData(BlocksTooltipData):
    __tradeIn: Any
    def __init__(self, context):
        ...
    def _packBlocks(self, discount, bonuses):
        ...
    def _getHeader(self):
        ...
    def _getGiftBlock(self):
        ...
    def _getDiscountSection(self, discount, bonuses):
        ...
    def _getBonusSection(self, bonuses):
        ...

class FrontlineRankTooltipData(BlocksTooltipData):
    __frontLine: Any
    __rank = 0
    def __init__(self, context):
        ...
    def _packBlocks(self, rank):
        ...
    def _getIcon(self):
        ...
    def _getHeader(self):
        ...
    def _getBottom(self):
        ...
