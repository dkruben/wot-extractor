# wot-extractor: STUB (.pyi) gerado a partir de sources/res/advent_calendar/scripts/client/advent_calendar/gui/Scaleform/daapi/view/tooltips/common_blocks.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from advent_calendar.gui.feature.constants import ADVENT_CALENDAR_TOKEN as ADVENT_CALENDAR_TOKEN
from advent_calendar.gui.impl.lobby.feature.advent_helper import getAccountTokensAmount as getAccountTokensAmount, getQuestNeededTokensCount as getQuestNeededTokensCount
from advent_calendar.skeletons import IAdventCalendarController as IAdventCalendarController
from gui.Scaleform.genConsts.BLOCKS_TOOLTIP_TYPES import BLOCKS_TOOLTIP_TYPES as BLOCKS_TOOLTIP_TYPES
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.formatters import text_styles as text_styles, icons as icons
from gui.shared.tooltips import formatters as formatters
from helpers import dependency as dependency

class AdventCalendarProgressionRewardTooltipData(object):
    __adventController: Any
    @classmethod
    def packProgressionBlock(cls, questID):
        ...
