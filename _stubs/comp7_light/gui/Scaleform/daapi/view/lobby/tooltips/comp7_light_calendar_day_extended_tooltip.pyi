# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_light/scripts/client/comp7_light/gui/Scaleform/daapi/view/lobby/tooltips/comp7_light_calendar_day_extended_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from datetime import datetime as datetime
from comp7_light.gui.Scaleform.daapi.view.lobby.tooltips.comp7_light_calendar_day_tooltip import Comp7LightCalendarDayTooltip as Comp7LightCalendarDayTooltip
from comp7_light.gui.comp7_light_constants import SELECTOR_BATTLE_TYPES as SELECTOR_BATTLE_TYPES
from comp7_light.gui.shared.tooltips import TOOLTIP_TYPE as TOOLTIP_TYPE
from gui.Scaleform.daapi.view.lobby.formatters.tooltips import packCalendarBlock as packCalendarBlock
from gui.impl import backport as backport
from gui.shared.formatters import text_styles as text_styles
from gui.shared.tooltips import formatters as formatters
from helpers import time_utils as time_utils
_TOOLTIP_MIN_WIDTH = 210

class Comp7LightCalendarDayExtendedTooltip(Comp7LightCalendarDayTooltip):
    _TOOLTIP_TYPE = TOOLTIP_TYPE.COMP7_LIGHT_CALENDAR_DAY_EXTENDED_INFO
    def _packBlocks(self, selectedTime):
        ...
    def __packTimeLeftBlock(self, daysLeft):
        ...
    def __isSeasonEnded(self, selectedTime):
        ...
    def __packCalendarBlock(self, selectedTime):
        ...
