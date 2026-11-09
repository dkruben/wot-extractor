# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/tooltips/marathon.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from gui import makeHtmlString as makeHtmlString
from gui.impl import backport as backport
from gui.marathon.marathon_constants import MarathonState as MarathonState, MarathonWarning as MarathonWarning
from gui.shared.formatters import text_styles as text_styles, icons as icons
from gui.shared.tooltips import TOOLTIP_TYPE as TOOLTIP_TYPE, formatters as formatters
from gui.shared.tooltips.common import BlocksTooltipData as BlocksTooltipData
from helpers import dependency as dependency
from skeletons.gui.game_control import IMarathonEventsController as IMarathonEventsController

class MarathonEventTooltipData(BlocksTooltipData):
    _marathonsCtrl: Any
    _marathonEvent: Any
    __tooltipData: Any
    __iconsData: Any
    def __init__(self, context):
        ...
    def _packBlocks(self, questType, prefix, *args, **kwargs):
        ...
    def _getHeader(self, _):
        ...
    def _getBody(self, state):
        ...
    def _getBottom(self, state):
        ...
    def _getAttentionNotice(self):
        ...
