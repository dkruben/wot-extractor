# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/tooltips/ranked/ranked_calendar_day_extended_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from datetime import datetime as datetime
from past.utils import old_div as old_div
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.formatters import text_styles as text_styles
from gui.shared.tooltips import formatters as formatters
from gui.shared.tooltips.ranked.ranked_calendar_day_tooltip import RankedCalendarDayTooltip as RankedCalendarDayTooltip
from gui.Scaleform.daapi.view.lobby.formatters.tooltips import packCalendarBlock as packCalendarBlock
from helpers import dependency as dependency, time_utils as time_utils
from skeletons.gui.game_control import IRankedBattlesController as IRankedBattlesController
from gui.prb_control.settings import SELECTOR_BATTLE_TYPES as SELECTOR_BATTLE_TYPES
_TOOLTIP_MIN_WIDTH = 200

class RankedCalendarDayExtendedTooltip(RankedCalendarDayTooltip):
    __rankedController: Any
    def _getController(self, *_):
        ...
    def _packBlocks(self, selectedTime):
        ...
    def __packTimeLeftBlock(self, name, daysLeft):
        ...
    def __isSeasonEnded(self, selectedTime):
        ...
    def __packCalendarBlock(self, selectedTime):
        ...
