# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/Scaleform/daapi/view/lobby/tooltips/battle_royale_calendar_extended_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.formatters import text_styles as text_styles
from gui.shared.tooltips import formatters as formatters
from helpers import dependency as dependency, time_utils as time_utils
from skeletons.connection_mgr import IConnectionManager as IConnectionManager
from gui.shared.tooltips.common import BlocksTooltipData as BlocksTooltipData
from gui.shared.tooltips.periodic.prime_helpers import getPrimeTableBlocks as getPrimeTableBlocks
from skeletons.gui.game_control import IBattleRoyaleController as IBattleRoyaleController
from gui.shared.tooltips import TOOLTIP_TYPE as TOOLTIP_TYPE

class BattleRoyaleCalendarExtendedTooltip(BlocksTooltipData):
    __TOOLTIP_MIN_WIDTH = 180
    __connectionMgr: Any
    _battleController: Any
    def __init__(self, context):
        ...
    def _packBlocks(self, *args):
        ...
    def __packTimeLeftBlock(self):
        ...
    def __packTimeTableBlock(self):
        ...
    def __getTillEndBlock(self, timeLeft):
        ...
