# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/mapbox/tooltips/mapbox_selector_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui import makeHtmlString as makeHtmlString
from gui.impl.gen import R as R
from gui.impl import backport as backport
from gui.mapbox.mapbox_helpers import getTillTimeString as getTillTimeString
from gui.prb_control.settings import SELECTOR_BATTLE_TYPES as SELECTOR_BATTLE_TYPES
from gui.Scaleform.daapi.view.lobby.formatters import tooltips as tooltips
from gui.shared.formatters import text_styles as text_styles
from gui.shared.formatters.ranges import toRomanRangeString as toRomanRangeString
from gui.shared.tooltips import formatters as formatters, TOOLTIP_TYPE as TOOLTIP_TYPE
from gui.shared.tooltips.common import BlocksTooltipData as BlocksTooltipData
from helpers import dependency as dependency
from skeletons.gui.game_control import IMapboxController as IMapboxController

class MapboxSelectorTooltip(BlocksTooltipData):
    __mapboxCtrl: Any
    __BODY_TEMPLATE_PATH = 'html_templates:lobby/tooltips/battle_type_selector'
    __BODY_TEMPLATE_KEY = SELECTOR_BATTLE_TYPES.MAPBOX
    def __init__(self, context):
        ...
    def _packBlocks(self, *args):
        ...
    def __packMainBlock(self):
        ...
    def __packFrozenBlock(self):
        ...
