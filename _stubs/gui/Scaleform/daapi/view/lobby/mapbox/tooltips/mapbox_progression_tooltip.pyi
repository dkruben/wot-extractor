# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/mapbox/tooltips/mapbox_progression_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from gui.impl.gen import R as R
from gui.impl import backport as backport
from gui.mapbox.mapbox_helpers import getTillTimeString as getTillTimeString, prepareProgressionData as prepareProgressionData
from gui.Scaleform.genConsts.PROGRESSCOLOR_CONSTANTS import PROGRESSCOLOR_CONSTANTS as PROGRESSCOLOR_CONSTANTS
from gui.Scaleform.genConsts.BLOCKS_TOOLTIP_TYPES import BLOCKS_TOOLTIP_TYPES as BLOCKS_TOOLTIP_TYPES
from gui.shared.formatters import text_styles as text_styles
from gui.shared.tooltips import formatters as formatters, TOOLTIP_TYPE as TOOLTIP_TYPE
from gui.shared.tooltips.common import BlocksTooltipData as BlocksTooltipData
from gui.shared.tooltips.formatters import RENDERERS_ALIGN_CENTER as RENDERERS_ALIGN_CENTER
from helpers import dependency as dependency
from skeletons.gui.game_control import IMapboxController as IMapboxController
_logger: Any
_IMG_PATH = R.images.gui.maps.icons.mapbox
_STR_PATH = R.strings.mapbox.questFlag
_MAPS_IN_ROW = 3
_MAX_MAPS_IN_ROW = 4
_MAP_ICON_SIZE: tuple

class MapboxProgressionTooltip(BlocksTooltipData):
    __mapboxCtrl: Any
    def __init__(self, context):
        ...
    def _packBlocks(self, *args):
        ...
    def __packHeaderBlock(self):
        ...
    def __packMapsProgressionBlock(self, progressionData):
        ...
    @staticmethod
    def __packTotalProgressionBlock(progressionData):
        ...
    @staticmethod
    def __packFrozenBlock():
        ...
    @staticmethod
    def __getMapsSublists(mapsVOs):
        ...
