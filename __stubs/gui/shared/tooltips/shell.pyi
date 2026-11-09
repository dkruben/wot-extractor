# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/tooltips/shell.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from constants import DAMAGE_INTERPOLATION_DIST_LAST as DAMAGE_INTERPOLATION_DIST_LAST, DAMAGE_INTERPOLATION_DIST_FIRST as DAMAGE_INTERPOLATION_DIST_FIRST, SHELL_MECHANICS_TYPE as SHELL_MECHANICS_TYPE
from gui.Scaleform.genConsts.BLOCKS_TOOLTIP_TYPES import BLOCKS_TOOLTIP_TYPES as BLOCKS_TOOLTIP_TYPES
from gui.impl import backport as backport
from gui.impl.backport import image as image
from gui.impl.gen import R as R
from gui.shared.formatters import text_styles as text_styles
from gui.shared.gui_items.gui_item_economics import isItemBuyPriceAvailable as isItemBuyPriceAvailable
from gui.shared.items_parameters.functions import getShellParamsSwitcherModifiedShells as getShellParamsSwitcherModifiedShells
from gui.shared.items_parameters.shell_params import SHELL_MECHANIC_ADDITIONAL_PARAMETERS as SHELL_MECHANIC_ADDITIONAL_PARAMETERS
from gui.shared.items_parameters import params_helper as params_helper, formatters as params_formatters
from gui.shared.tooltips import formatters as formatters, TOOLTIP_TYPE as TOOLTIP_TYPE
from gui.shared.tooltips.common import makePriceBlock as makePriceBlock, CURRENCY_SETTINGS as CURRENCY_SETTINGS, BlocksTooltipData as BlocksTooltipData
from gui.shared.tooltips.module import ModuleTooltipBlockConstructor as ModuleTooltipBlockConstructor
from gui.shared.utils import NORMALIZATION_ANGLE as NORMALIZATION_ANGLE, RICOCHET_ANGLE as RICOCHET_ANGLE, PENETRATION_LOSS as PENETRATION_LOSS
from helpers import dependency as dependency
from helpers.i18n import makeString as _ms
from items.utils import getVehicleDescriptorWithoutMechanic as getVehicleDescriptorWithoutMechanic
from items.vehicle_mechanics_types import VehicleMechanicKeys as VehicleMechanicKeys
from skeletons.gui.shared import IItemsCache as IItemsCache
from vehicles.mechanics.mechanic_helpers import hasVehicleDescrMechanic as hasVehicleDescrMechanic
from gui.impl.gen.view_models.common.vehicle_mechanic_model import MechanicsRank as MechanicsRank
_logger: Any
_DASH: Any
_SHELL_TOOLTIP_FORMAT_SETTINGS: Any
_ASTERISK = '*'
_TOOLTIP_MIN_WIDTH = 380
_TOOLTIP_NORMAL_WIDTH = 420
_TWO_COLUMNS_TOOLTIP_WIDTH = 500
_MECHANICS_TEXT_ROOT = R.strings.tooltips.shell.mechanics
_MECHANICS_IMAGE_ROOT = R.images.gui.maps.icons.tooltip.mechanics
_SUPPORTED_MECHANICS: tuple
_MECHANIC_PARAMS_WIDTH: dict
_PARAM_VISIBILITY: dict
_MECHANIC_ONLY_PARAMS: Any
_MECHANIC_PARAMS_CONSTRUCTOR: dict

class ShellBlockToolTipData(BlocksTooltipData):
    item: Any
    def __init__(self, context):
        ...
    def _invalidateWidth(self, width):
        ...
    def _packBlocks(self, *args, **kwargs):
        ...
    def __getStatsBlockConstructor(self, shellMechanic):
        ...
    def __getActiveShellMechanic(self):
        ...
    def __getExtraStatusBlock(self, mechanicItem):
        ...
    def __getBasicIsUsedInCalculationsInfoBlock(self):
        ...

class ShellTooltipBlockConstructor(object):
    itemsCache: Any
    shell: Any
    configuration: Any
    leftPadding: Any
    rightPadding: Any
    _params: Any
    def __init__(self, shell, configuration, leftPadding=20, rightPadding=20, params=None):
        ...
    def construct(self):
        ...

class HeaderBlockConstructor(ShellTooltipBlockConstructor):
    def construct(self):
        ...

class PriceBlockConstructor(ShellTooltipBlockConstructor):
    _valueWidth: Any
    def __init__(self, shell, configuration, valueWidth):
        ...
    def construct(self):
        ...

class CommonStatsBlockConstructor(ShellTooltipBlockConstructor):
    _valueWidth: Any
    def __init__(self, shell, configuration, valueWidth, mechanic, params):
        ...
    def construct(self):
        ...
    def _getHeaderBlock(self, bottomPadding):
        ...
    def _isSkippedParam(self, paramName, shell):
        ...
    def _packParamBlock(self, name, value, units):
        ...
    def _getValueBlock(self, paramName, comparator, piercingPowerTable, colorScheme):
        ...
    def _applyParamMeta(self, paramName, tableData, footNotes):
        ...
    @staticmethod
    def _addFootNote(container, note):
        ...
    @staticmethod
    def _packFootNotes(footNotes):
        ...
    @staticmethod
    def _iteratePiercingPowerTable(table, comparator, colorScheme):
        ...
    def _getValueComparator(self, vDescr):
        ...

class ICompareStrategy(object):
    @staticmethod
    def resolveDescriptors(vDescr):
        ...
    @staticmethod
    def buildComparators(shell, vDescr):
        ...

class _LowChargeShotCompareStrategy(ICompareStrategy):
    @staticmethod
    def resolveDescriptors(vDescr):
        ...
    @staticmethod
    def buildComparators(shell, vDescr):
        ...

class _ShellParamsSwitcherCompareStrategy(ICompareStrategy):
    @staticmethod
    def resolveDescriptors(vDescr):
        ...
    @staticmethod
    def buildComparators(shell, vDescr):
        ...

class _ShellCalibrationCompareStrategy(ICompareStrategy):
    @staticmethod
    def resolveDescriptors(vDescr):
        ...
    @staticmethod
    def buildComparators(shell, vDescr):
        ...

class _ShellParamsBustleFeedCompareStrategy(ICompareStrategy):
    @staticmethod
    def resolveDescriptors(vDescr):
        ...
    @staticmethod
    def buildComparators(shell, vDescr):
        ...

class TwoColumnsStatsBlockConstructor(CommonStatsBlockConstructor):
    _MECHANIC_DESCRIPTOR_RESOLVERS: dict
    _mechanic: Any
    _leftComparator: Any
    _rightComparator: Any
    _mechanicParameters: Any
    def __init__(self, shell, configuration, valueWidth, mechanic, params=None):
        ...
    def _isSkippedParam(self, paramName, shell):
        ...
    def _getValueComparator(self, vDescr, dropMechanic=True):
        ...
    def _getValueBlock(self, paramName, comparator, piercingPowerTable, colorScheme):
        ...
    def _getHeaderBlock(self, bottomPadding):
        ...
    def _packParamBlock(self, name, value, units):
        ...

class ShellCalibrationStatsBlockConstructor(TwoColumnsStatsBlockConstructor):
    def _getHeaderBlock(self, bottomPadding):
        ...
    def _packParamBlock(self, name, value, units):
        ...

def _isEmptyNormalizationAngleValid(cfg, shell):
    ...
