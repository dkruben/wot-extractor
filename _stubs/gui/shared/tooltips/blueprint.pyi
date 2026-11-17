# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/tooltips/blueprint.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import iteritems as iteritems
import nations as nations
from blueprints.BlueprintTypes import BlueprintTypes as BlueprintTypes
from gui.Scaleform.genConsts.BLOCKS_TOOLTIP_TYPES import BLOCKS_TOOLTIP_TYPES as BLOCKS_TOOLTIP_TYPES
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.Scaleform.locale.NATIONS import NATIONS as NATIONS
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS as TOOLTIPS
from gui.impl import backport as backport
from gui.impl.gen.resources import R as R
from gui.shared.formatters import text_styles as text_styles, icons as icons
from gui.shared.tooltips import TOOLTIP_TYPE as TOOLTIP_TYPE
from gui.shared.tooltips import formatters as formatters
from gui.shared.tooltips.common import BlocksTooltipData as BlocksTooltipData, DynamicBlocksTooltipData as DynamicBlocksTooltipData
from gui.shared.utils.requesters.blueprints_requester import SPECIAL_BLUEPRINT_LEVEL as SPECIAL_BLUEPRINT_LEVEL
from helpers import int2roman as int2roman, i18n as i18n
from helpers.blueprint_generator import g_blueprintGenerator as g_blueprintGenerator

class BlueprintTooltipData(BlocksTooltipData):
    _fragmentCD: Any
    _items: Any
    def __init__(self, context):
        ...
    def _packBlocks(self, fragmentCD):
        ...
    @staticmethod
    def _getVehicleDescrStr(vehicle):
        ...
    @staticmethod
    def _getUnlockDiscountBlock(percentValue, xpValue, title, showPlus=False):
        ...
    @staticmethod
    def _getImageWithBottomTitleBlock(imagePath, imageTitle, blockPadding=None):
        ...
    @staticmethod
    def _getAllianceTextWithIcon(alliance):
        ...
    def _setNationFlagCornerBg(self, nationName):
        ...
    def _packConversionFormulaBlock(self, intelRequired, nationRequired, vehicle):
        ...

class ConvertInfoBlueprintTooltipData(BlueprintTooltipData):
    __vehicle: Any
    __blueprintData: Any
    __convertibleCount: Any
    def __init__(self, context):
        ...
    def _packBlocks(self, vehicleCD):
        ...

class VehicleBlueprintTooltipData(BlueprintTooltipData, DynamicBlocksTooltipData):
    __vehicle: Any
    __blueprintData: Any
    __texture: Any
    __allianceName: Any
    _items: Any
    def __init__(self, context):
        ...
    def isDynamic(self):
        ...
    def stopUpdates(self):
        ...
    def changeVisibility(self, isVisible):
        ...
    def _packBlocks(self, vehicleCD, isShortForm=False):
        ...
    def __packTitleBlock(self, isShortForm):
        ...
    def __packBlueprintBlock(self):
        ...
    def __packFragmentsInfoBlock(self):
        ...
    def __packDiscountBlock(self):
        ...
    def __packGatherDescrBlock(self):
        ...
    def __packStatusBlock(self):
        ...
    @staticmethod
    def __packBlueprintDescrBlock():
        ...
    @staticmethod
    def __packFreeUnlockBlock():
        ...

class BlueprintFragmentRandomTooltipData(BlueprintTooltipData):
    def __init__(self, context):
        ...
    def _packBlocks(self, fragmentCD):
        ...
    @staticmethod
    def __packDiscountBlock():
        ...
    def __packRandomFragmentBlocks(self):
        ...
    def _getHeader(self):
        ...
    def _getDescr(self):
        ...

class BlueprintFragmentRandomNationalTooltipData(BlueprintTooltipData):
    def __init__(self, context):
        ...
    def _packBlocks(self, fragmentCD):
        ...
    def __packAdditionalInfoBlock(self):
        ...
    def __packRandomFragmentBlocks(self):
        ...

class BlueprintFragmentTooltipData(BlueprintTooltipData):
    __nationName: Any
    __allianceName: Any
    _items: Any
    def __init__(self, context):
        ...
    def _packBlocks(self, fragmentCD):
        ...
    @staticmethod
    def __packInStorageBlock(count=0):
        ...
    def __packAdditionalInfoBlock(self):
        ...
    def __packIntelFragmentBlocks(self):
        ...
    def __packNationalFragmentBlocks(self):
        ...
    def __packVehicleFragmentBlocks(self):
        ...

class BlueprintEmptySlotTooltipData(BlueprintTooltipData):
    __vehicle: Any
    __blueprintData: Any
    __allianceName: Any
    def __init__(self, context):
        ...
    def _packBlocks(self, vehicleCD):
        ...
    @staticmethod
    def __packTitleBlock():
        ...
    def __packDiscountBlock(self):
        ...
    def __packDescriptionBlock(self):
        ...
