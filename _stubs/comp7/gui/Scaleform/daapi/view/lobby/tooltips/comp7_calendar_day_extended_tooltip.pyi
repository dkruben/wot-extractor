# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/Scaleform/daapi/view/lobby/tooltips/comp7_calendar_day_extended_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from datetime import datetime as datetime
from comp7.gui.Scaleform.daapi.view.lobby.tooltips.comp7_calendar_day_tooltip import Comp7CalendarDayTooltip as Comp7CalendarDayTooltip
from comp7.gui.comp7_constants import SELECTOR_BATTLE_TYPES as SELECTOR_BATTLE_TYPES
from comp7.gui.impl.gen.view_models.views.lobby.enums import SeasonName as SeasonName
from comp7.gui.shared.tooltips import TOOLTIP_TYPE as TOOLTIP_TYPE
from comp7_core.gui.impl.lobby.comp7_core_helpers import comp7_core_model_helpers as comp7_core_model_helpers
from gui.Scaleform.daapi.view.lobby.formatters.tooltips import packCalendarBlock as packCalendarBlock
from gui.impl import backport as backport
from gui.shared.formatters import text_styles as text_styles
from gui.shared.tooltips import formatters as formatters
from helpers import dependency as dependency
from helpers import time_utils as time_utils
from skeletons.gui.game_control import IComp7Controller as IComp7Controller
_TOOLTIP_MIN_WIDTH = 210

class Comp7CalendarDayExtendedTooltip(Comp7CalendarDayTooltip):
    _TOOLTIP_TYPE = TOOLTIP_TYPE.COMP7_CALENDAR_DAY_EXTENDED_INFO
    __comp7Controller: Any
    def _packBlocks(self, selectedTime):
        ...
    def __packTimeLeftBlock(self, daysLeft):
        ...
    def __isSeasonEnded(self, selectedTime):
        ...
    def __packCalendarBlock(self, selectedTime):
        ...
