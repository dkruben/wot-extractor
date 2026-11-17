# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/tooltips/battle_selector.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from gui.Scaleform.genConsts.BLOCKS_TOOLTIP_TYPES import BLOCKS_TOOLTIP_TYPES as BLOCKS_TOOLTIP_TYPES
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.formatters import text_styles as text_styles
from gui.shared.formatters.time_formatters import formatDate as formatDate
from gui.shared.tooltips import formatters as formatters
from gui.shared.tooltips.common import BlocksTooltipData as BlocksTooltipData
from gui.shared.tooltips.periodic.prime_helpers import getPrimeTableBlocks as getPrimeTableBlocks
from helpers import dependency as dependency, time_utils as time_utils
from skeletons.connection_mgr import IConnectionManager as IConnectionManager
from skeletons.gui.game_control import ISeasonProvider as ISeasonProvider

class SeasonalBattleSelectorTooltip(BlocksTooltipData):
    __connectionMgr: Any
    _battleController = None
    _TOOLTIP_TYPE = None
    _TOOLTIP_WIDTH = None
    _R_BATTLE_SELECTOR_STR = R.strings.tooltips.seasonalBattleSelector
    def __init__(self, ctx):
        ...
    def _packBlocks(self, *_, **__):
        ...
    @classmethod
    def _packHeaderBlock(cls):
        ...
    @classmethod
    def _packTimeTableBlock(cls, leftPadding=0, bottomPadding=0):
        ...
    @classmethod
    def _packTillEndBlock(cls):
        ...
    @classmethod
    def _packTimeTableHeaderBlock(cls):
        ...
    @staticmethod
    def _packTimeBlock(message, timeStr):
        ...
    @classmethod
    def _packPeriods(cls, periods):
        ...
    @staticmethod
    def _getTitle():
        ...
    @staticmethod
    def _getDescription():
        ...
