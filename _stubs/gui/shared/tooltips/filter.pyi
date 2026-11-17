# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/tooltips/filter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import constants as constants
from frameworks.wulf import WindowLayer as WindowLayer
from helpers import dependency as dependency
from helpers import int2roman as int2roman
from helpers.i18n import makeString as _ms
from gui import GUI_NATIONS as GUI_NATIONS
from gui.prb_control.settings import VEHICLE_LEVELS as VEHICLE_LEVELS
from gui.Scaleform import getNationsFilterAssetPath as getNationsFilterAssetPath, getVehicleTypeAssetPath as getVehicleTypeAssetPath
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.genConsts.HANGAR_ALIASES import HANGAR_ALIASES as HANGAR_ALIASES
from gui.Scaleform.genConsts.QUESTS_ALIASES import QUESTS_ALIASES as QUESTS_ALIASES
from gui.Scaleform.genConsts.BLOCKS_TOOLTIP_TYPES import BLOCKS_TOOLTIP_TYPES as BLOCKS_TOOLTIP_TYPES
from gui.Scaleform.genConsts.ICON_TEXT_FRAMES import ICON_TEXT_FRAMES as ICON_TEXT_FRAMES
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.Scaleform.locale.TANK_CAROUSEL_FILTER import TANK_CAROUSEL_FILTER as TANK_CAROUSEL_FILTER
from gui.shared.gui_items.Vehicle import VEHICLE_TYPES_ORDER as VEHICLE_TYPES_ORDER
from gui.shared.formatters import text_styles as text_styles, icons as icons
from gui.shared.tooltips import TOOLTIP_TYPE as TOOLTIP_TYPE, formatters as formatters
from gui.shared.tooltips.common import BlocksTooltipData as BlocksTooltipData
from skeletons.gui.shared import IItemsCache as IItemsCache

class VehicleFilterTooltip(BlocksTooltipData):
    itemsCache: Any
    _currentVehiclesCount: Any
    _totalVehiclesCount: Any
    _nations: Any
    _vehicleTypes: Any
    _levels: Any
    _rented: Any
    _event: Any
    _specials: Any
    _searchNameVehicle: Any
    def __init__(self, ctx):
        ...
    def _packBlocks(self, *args):
        ...
    def _packSearchNameVehicle(self):
        ...
    def _packHeaderBlock(self):
        ...
    def _packHiddenBlock(self):
        ...
    def _packCounterBlock(self):
        ...
    def _packBodyBlock(self):
        ...
    def __getParagraphNameBlock(self, name):
        ...
    def __packNationsListBlock(self):
        ...
    def __packTypesListBlock(self):
        ...
    def __packLevelBlock(self):
        ...
    def __packSpecialTypeBlock(self):
        ...
    def __packSearchNameVehicle(self, text):
        ...
    def __gatherData(self, tankCarousel):
        ...
    def __hasBody(self):
        ...
