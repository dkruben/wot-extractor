# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/mapbox/tooltips/mapbox_calendar_day_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.impl.gen import R as R
from gui.shared.tooltips import TOOLTIP_TYPE as TOOLTIP_TYPE
from gui.shared.tooltips.periodic.calendar_day import PeriodicCalendarDayTooltip as PeriodicCalendarDayTooltip
from helpers import dependency as dependency
from skeletons.gui.game_control import IMapboxController as IMapboxController

class MapboxCalendarDayTooltip(PeriodicCalendarDayTooltip):
    _controller: Any
    _TOOLTIP_TYPE = TOOLTIP_TYPE.MAPBOX_CALENDAR_DAY
    _RES_ROOT = R.strings.mapbox.calendarDay
    def _getController(self, *_):
        ...
    def _isValidPrimeTimes(self, serversPeriodsMapping):
        ...
