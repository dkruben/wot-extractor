# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/tooltips/vehicle_collector.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from itertools import chain as chain
from constants import MIN_VEHICLE_LEVEL as MIN_VEHICLE_LEVEL
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.shared.formatters import text_styles as text_styles
from gui.shared.tooltips.common import BLOCKS_TOOLTIP_TYPES as BLOCKS_TOOLTIP_TYPES, BlocksTooltipData as BlocksTooltipData
from gui.shared.tooltips import formatters as formatters, TOOLTIP_TYPE as TOOLTIP_TYPE
from gui.shared.utils import vehicle_collector_helper as helper
from dossiers2.custom.cache import getCache as getCache
from helpers import dependency as dependency
import nations as nations
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache
from soft_exception import SoftException as SoftException
_logger: Any

class VehicleCollectorTooltipData(BlocksTooltipData):
    __itemsCache: Any
    __nationName: Any
    def __init__(self, context):
        ...
    def _packBlocks(self, nationName):
        ...
    def __getHeader(self):
        ...
    def __getDisabledStatusBlock(self):
        ...
    @staticmethod
    def __getDescription():
        ...

class VehicleCollectorDisabledTooltipData(BlocksTooltipData):
    __lobbyContext: Any
    def __init__(self, context):
        ...
    def getDisplayableData(self, *args, **kwargs):
        ...
