# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/Scaleform/daapi/view/lobby/tooltips/comp7_calendar_day_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from comp7.gui.shared.tooltips import TOOLTIP_TYPE as TOOLTIP_TYPE
from gui.impl.gen import R as R
from gui.shared.tooltips.periodic.calendar_day import PeriodicCalendarDayTooltip as PeriodicCalendarDayTooltip
from helpers import dependency as dependency
from skeletons.gui.game_control import IComp7Controller as IComp7Controller

class Comp7CalendarDayTooltip(PeriodicCalendarDayTooltip):
    _controller: Any
    _TOOLTIP_TYPE = TOOLTIP_TYPE.COMP7_CALENDAR_DAY_INFO
    _RES_ROOT = R.strings.comp7_ext.calendarDay
    def _getController(self, *_):
        ...
