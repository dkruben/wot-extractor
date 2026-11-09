# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline/gui/Scaleform/daapi/view/lobby/tooltips/epic_battle_calendar_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.formatters import text_styles as text_styles
from gui.shared.formatters.time_formatters import formatDate as formatDate
from gui.shared.tooltips import formatters as formatters
from gui.shared.tooltips.common import BlocksTooltipData as BlocksTooltipData
from helpers import dependency as dependency, time_utils as time_utils
from .common_blocks import packEpicBattleSeasonBlock as packEpicBattleSeasonBlock
from skeletons.connection_mgr import IConnectionManager as IConnectionManager
from skeletons.gui.game_control import IEpicBattleMetaGameController as IEpicBattleMetaGameController
_R_TIMETABLE = R.strings.epic_battle.selectorTooltip.epicBattle.timeTable

class EpicBattleCalendarTooltip(BlocksTooltipData):
    __connectionMgr: Any
    __epicController: Any
    __slots__: tuple
    def __init__(self, context):
        ...
    def _packBlocks(self, *args, **kwargs):
        ...
    def __getPackersInProgress(self):
        ...
    def __packScheduleBlock(self):
        ...
    def __packTimeTableHeaderBlock(self):
        ...
    def __packPeriods(self, periods):
        ...
    def __packTimeBlock(self, message, timeStr):
        ...
