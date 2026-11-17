# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/Scaleform/daapi/view/lobby/feature/tooltips/calendar_day_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from future.utils import viewvalues as viewvalues
from fun_random.gui.feature.util.fun_mixins import FunSubModesWatcher as FunSubModesWatcher
from fun_random.gui.shared.tooltips import TOOLTIP_TYPE as TOOLTIP_TYPE
from gui.impl.gen import R as R
from gui.shared.tooltips.periodic.calendar_day import PeriodicCalendarDayTooltip as PeriodicCalendarDayTooltip
from helpers.time_utils import ONE_DAY as ONE_DAY

class FunRandomCalendarDayTooltip(PeriodicCalendarDayTooltip, FunSubModesWatcher):
    _TOOLTIP_TYPE = TOOLTIP_TYPE.FUN_RANDOM
    _RES_ROOT = R.strings.fun_random.calendarDay
    def _getController(self, *_):
        ...

class FunRandomModeSelectorCalendarTooltip(FunRandomCalendarDayTooltip):
    def _getController(self, subModeID=None, *_):
        ...
    def _isValidPrimeTimes(self, serversPeriodsMapping):
        ...
