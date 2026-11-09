# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/tooltips/advanced.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from constants import SHELL_TYPES as SHELL_TYPES
from gui.Scaleform.genConsts.BLOCKS_TOOLTIP_TYPES import BLOCKS_TOOLTIP_TYPES as BLOCKS_TOOLTIP_TYPES
from gui.Scaleform.genConsts.FITTING_TYPES import FITTING_TYPES as FITTING_TYPES
from gui.Scaleform.genConsts.STORE_CONSTANTS import STORE_CONSTANTS as STORE_CONSTANTS
from gui.Scaleform.locale.ITEM_TYPES import ITEM_TYPES as ITEM_TYPES
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS as TOOLTIPS
from gui.goodies.goodie_items import DemountKit as DemountKit
from gui.impl import backport as backport
from gui.impl.backport.backport_tooltip import DecoratedTooltipWindow as DecoratedTooltipWindow
from gui.impl.gen import R as R
from gui.prb_control.settings import PREBATTLE_ACTION_NAME as PREBATTLE_ACTION_NAME
from gui.shared.formatters import text_styles as text_styles
from gui.shared.gui_items.artefacts import OptionalDevice as OptionalDevice
from gui.shared.tooltips import formatters as formatters, ToolTipBaseData as ToolTipBaseData
from gui.shared.tooltips.common import BlocksTooltipData as BlocksTooltipData
from helpers import dependency as dependency
from helpers import i18n as i18n
from items.vehicle_mechanics_types import VehicleMechanicKeys as VehicleMechanicKeys
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
DISABLED_ITEMS_ID = 12793
CHASSIS_TRACK_WITHIN_TRACK = 'vehicleTrackWithinTrackChassis'
_FOOTER_FOR_VEHICLE_MECHANICS: dict
SKILL_MOVIES: dict
MODULE_MOVIES: dict
TANKMAN_MOVIES: dict
SHELL_MOVIES: dict

class ComplexTooltip(BlocksTooltipData):
    __settingsCore: Any
    _disableAnim: Any
    def __init__(self, context, disableAnim):
        ...
    def _packBlocks(self, *args, **kwargs):
        ...

class BaseAdvancedTooltip(BlocksTooltipData):
    _item: Any
    def __init__(self, context):
        ...
    @staticmethod
    def getMovieAnimationPath(moviename):
        ...
    def _packBlocks(self, *args, **kwargs):
        ...
    def _getBlocksList(self, *args, **kwargs):
        ...
    def _getDescrText(self, description, descReady=False):
        ...
    def _packAdvancedBlocks(self, movie, header, description, descReady=False):
        ...

class AdvancedTooltipWithMechanics(BaseAdvancedTooltip):
    def _getMechanics(self, vehicle):
        ...
    def _getDescrText(self, description, descReady=False):
        ...

class FakeAdvancedTooltip(BaseAdvancedTooltip):
    def _getBlocksList(self, *args, **kwargs):
        ...

class ComplexAdvanced(BaseAdvancedTooltip):
    def _getBlocksList(self, item, *args, **kwargs):
        ...

class HangarShellAdvanced(AdvancedTooltipWithMechanics):
    _MODERN_SUFFIX = '_MODERN'
    _NOT_PIERCING_DAMAGE = '_NOT_PIERCING_DAMAGE'
    _TRAY = '_TRAY'
    def _getBlocksList(self, *args, **kwargs):
        ...
    def _getDescriptionSuffix(self):
        ...

class HangarBoosterAdvanced(BaseAdvancedTooltip):
    def _getBlocksList(self, *args, **kwargs):
        ...

class HangarModuleAdvanced(AdvancedTooltipWithMechanics):
    def _getMechanics(self, vehicle):
        ...
    def _getBlocksList(self, *args, **kwargs):
        ...

class TankmanPreviewTooltipAdvanced(BaseAdvancedTooltip):
    def _packBlocks(self, role, *args, **kwargs):
        ...

class VehicleParametersAdvanced(ToolTipBaseData):
    _movies: dict
    def __init__(self, context):
        ...
    def getDisplayableData(self, paramName, *args, **kwargs):
        ...

class MoneyAndXpAdvanced(BaseAdvancedTooltip):
    _moviesOrDescriptions: dict
    def _getBlocksList(self, *args, **kwargs):
        ...

class RankedAdvanced(BaseAdvancedTooltip):
    def _getBlocksList(self, *args, **kwargs):
        ...

class DemountKitTooltipAdvanced(BaseAdvancedTooltip):
    def _packBlocks(self, *args, **kwargs):
        ...

def _getLowChargeShotFooter(text):
    ...
