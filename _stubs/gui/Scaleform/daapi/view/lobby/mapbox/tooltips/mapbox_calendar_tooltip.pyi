# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/mapbox/tooltips/mapbox_calendar_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.impl.gen import R as R
from gui.impl import backport as backport
from gui.Scaleform.daapi.view.lobby.formatters.tooltips import packCalendarBlock as packCalendarBlock
from gui.shared.tooltips import formatters as formatters, TOOLTIP_TYPE as TOOLTIP_TYPE
from gui.shared.tooltips.common import BlocksTooltipData as BlocksTooltipData
from helpers import dependency as dependency, time_utils as time_utils
from skeletons.gui.game_control import IMapboxController as IMapboxController
from gui.shared.formatters import text_styles as text_styles
from gui.prb_control.settings import SELECTOR_BATTLE_TYPES as SELECTOR_BATTLE_TYPES

class MapboxCalendarTooltip(BlocksTooltipData):
    __mapboxCtrl: Any
    def __init__(self, context):
        ...
    def _packBlocks(self, *args, **kwargs):
        ...
    def __packHeader(self):
        ...
    def __getCurrentSeasonDate(self):
        ...
    def __getDate(self, date):
        ...
    def __packTimeTableHeaderBlock(self):
        ...
