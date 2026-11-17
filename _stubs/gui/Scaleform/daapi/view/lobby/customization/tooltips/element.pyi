# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/customization/tooltips/element.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from future.utils import viewitems as viewitems
from CurrentVehicle import g_currentVehicle as g_currentVehicle, g_currentPreviewVehicle as g_currentPreviewVehicle
from gui.Scaleform.daapi.view.lobby.customization.shared import getItemInventoryCount as getItemInventoryCount, makeVehiclesShortNamesString as makeVehiclesShortNamesString, getSuitableText as getSuitableText, ITEM_TYPE_TO_TAB as ITEM_TYPE_TO_TAB, CustomizationTabs as CustomizationTabs
from gui.Scaleform.daapi.view.lobby.customization.shared import getProgressionItemStatusText as getProgressionItemStatusText
from gui.Scaleform.genConsts.BLOCKS_TOOLTIP_TYPES import BLOCKS_TOOLTIP_TYPES as BLOCKS_TOOLTIP_TYPES
from gui.Scaleform.genConsts.SEASONS_CONSTANTS import SEASONS_CONSTANTS as SEASONS_CONSTANTS
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.Scaleform.locale.MENU import MENU as MENU
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS as TOOLTIPS
from gui.Scaleform.locale.VEHICLE_CUSTOMIZATION import VEHICLE_CUSTOMIZATION as VEHICLE_CUSTOMIZATION
from gui.customization.constants import CustomizationModes as CustomizationModes
from gui.customization.shared import PROJECTION_DECAL_TEXT_FORM_TAG as PROJECTION_DECAL_TEXT_FORM_TAG, SEASON_TYPE_TO_NAME as SEASON_TYPE_TO_NAME, PROJECTION_DECAL_FORM_TO_UI_ID as PROJECTION_DECAL_FORM_TO_UI_ID, getBaseStyleItems as getBaseStyleItems, getAncestors as getAncestors, getInheritors as getInheritors
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.Scaleform.daapi.view.lobby.missions.cards_formatters import CARD_FIELDS_FORMATTERS as CARD_FIELDS_FORMATTERS
from gui.server_events.cond_formatters.bonus import BattlesCountFormatter as BattlesCountFormatter
from gui.server_events.events_helpers import getC11nQuestsConfig as getC11nQuestsConfig
from gui.shared.formatters import text_styles as text_styles, icons as icons
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE, GUI_ITEM_TYPE_NAMES as GUI_ITEM_TYPE_NAMES
from gui.shared.gui_items.customization import CustomizationTooltipContext as CustomizationTooltipContext
from gui.shared.items_parameters import formatters as params_formatters
from gui.shared.items_parameters.params_helper import SimplifiedBarVO as SimplifiedBarVO
from gui.shared.missions.packers.conditions import getDefaultMissionsBonusConditionsFormatter as getDefaultMissionsBonusConditionsFormatter, getDefaultPostBattleCondFormatter as getDefaultPostBattleCondFormatter, getDefaultVehicleCondFormatter as getDefaultVehicleCondFormatter
from gui.shared.tooltips import formatters as formatters, TOOLTIP_TYPE as TOOLTIP_TYPE
from gui.shared.tooltips.common import BlocksTooltipData as BlocksTooltipData, makePriceBlock as makePriceBlock, CURRENCY_SETTINGS as CURRENCY_SETTINGS
from gui.shared.utils.graphics import isRendererPipelineDeferred as isRendererPipelineDeferred
from shared_utils import first as first
from helpers import dependency as dependency, int2roman as int2roman, time_utils as time_utils
from helpers.i18n import makeString as _ms
from items.components.c11n_constants import ProjectionDecalFormTags as ProjectionDecalFormTags, SeasonType as SeasonType, ItemTags as ItemTags, CustomizationDisplayType as CustomizationDisplayType, Rarity as Rarity
from items.vehicles import g_cache as g_cache
from math_common import round_py2_style_int as round_py2_style_int
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.customization import ICustomizationService as ICustomizationService
from skeletons.gui.server_events import IEventsCache as IEventsCache
from skeletons.gui.shared import IItemsCache as IItemsCache
_logger: Any

class SimplifiedStatsBlockConstructor(object):
    __stockParams: Any
    __comparator: Any
    __padding: Any
    def __init__(self, stockParams, comparator, padding=None):
        ...
    def construct(self):
        ...

class SimpleCustomizationTooltip(BlocksTooltipData):
    def __init__(self, context):
        ...
    def _packBlocks(self, *args, **kwargs):
        ...
    def _packItemBlocks(self, *args, **kwargs):
        ...
    @staticmethod
    def _packNonHistoricBlock(topPadding):
        ...

class NonHistoricTooltip(SimpleCustomizationTooltip):
    def _packItemBlocks(self):
        ...

class FantasticalTooltip(SimpleCustomizationTooltip):
    def _packItemBlocks(self):
        ...

class ChainedTooltip(SimpleCustomizationTooltip):
    def _packItemBlocks(self):
        ...
    @staticmethod
    def _packChainedBlock():
        ...

class PopoverTooltip(SimpleCustomizationTooltip):
    __service: Any
    def _packItemBlocks(self, isNonHistoric):
        ...
    @classmethod
    def __packPopoverBlock(cls):
        ...

class ElementTooltip(BlocksTooltipData):
    _itemsCache: Any
    __settingsCore: Any
    __service: Any
    __eventsCache: Any
    CUSTOMIZATION_TOOLTIP_WIDTH = 446
    CUSTOMIZATION_TOOLTIP_ICON_WIDTH = 104
    CUSTOMIZATION_TOOLTIP_ICON_HEIGHT = 102
    CUSTOMIZATION_TOOLTIP_ICON_WIDTH_WIDE = 204
    CUSTOMIZATION_TOOLTIP_ICON_WIDTH_OTHER_BIG = 226
    CUSTOMIZATION_TOOLTIP_ICON_WIDTH_INSCRIPTION = 278
    CUSTOMIZATION_TOOLTIP_ICON_WIDTH_PERSONAL_NUMBER = 390
    CUSTOMIZATION_TOOLTIP_ICON_WIDTHS: dict
    CUSTOMIZATION_TOOLTIP_ICON_HEIGHTS: dict
    ALL_SEASON_MAP_ICON = 'all_season'
    HISTORICAL_ICON = 'historical'
    NON_HISTORICAL_ICON = 'non_historical'
    FANTASTICAL_ICON = 'fantastical'
    RENTABLE_ICON = 'rentable'
    EDITABLE_DISABLE_ICON = 'editable_disable'
    EDITED_ICON = 'edited'
    EDITABLE_ICON = 'editable'
    NON_EDITABLE_ICON = 'non_editable'
    PROGRESSION_REWIND_ICON = 'progression_rewind'
    SERIAL_NUMBER_ICON = 'serial_number'
    QUEST_PROGRESSION_ICON = 'questProgression'
    OPENED_ICON = 'opened'
    SPECIAL_EFFECT_ICON = 'special_effect'
    _item: Any
    _appliedCount: Any
    _progressionLevel: Any
    _showOnlyProgressBlock: Any
    __skipQuestValidation: Any
    __ctx: Any
    __vehicle: Any
    bonusDescription: Any
    boundVehs: Any
    installedVehs: Any
    installedCount: Any
    def __init__(self, context, tooltipType=...):
        ...
    def _packBlocks(self, *args):
        ...
    def _packItemBlocks(self, statsConfig):
        ...
    def _packStatusBlock(self):
        ...
    def _packQuestsBlock(self):
        ...
    def _packCharacteristicsBlock(self):
        ...
    @staticmethod
    def _getCustomizationTypes():
        ...
    def _packSuitableBlock(self):
        ...
    def _getSuitableBlocks(self):
        ...
    def _packAppliedBlock(self):
        ...
    def _packSpecialBlock(self):
        ...
    def _packRarityHeaderBlock(self):
        ...
    def _packTitleBlock(self):
        ...
    def _packInventoryBlock(self, showBuyPrice, showSellPrice, showInventoryCount):
        ...
    def _countImageWidth(self):
        ...
    def _countImageHeight(self):
        ...
    def _packIconBlock(self, isDim=False):
        ...
    def _packBonusBlock(self, bonus, camo, isApplied):
        ...
    def _packLockedBlock(self):
        ...
    def _packDescriptionBlock(self):
        ...
    def _packUnsupportedBlock(self):
        ...
    def _packProgressBlock(self):
        ...
    def __packProgressDescriptionText(self, condition, showCurrentProgress=False):
        ...
    def _packProgressStateBlock(self):
        ...
    def _packStatTrackerStatBlock(self):
        ...
    def __packInheritorBlock(self, ancestors):
        ...
    def __packAncestorBlock(self, dependentItems):
        ...
    @staticmethod
    def __packChainedBlockTitle(title):
        ...
    @staticmethod
    def __packDependentContentFormat(text, icon):
        ...

class ElementIconTooltip(ElementTooltip):
    def __init__(self, context):
        ...
    @staticmethod
    def _getCustomizationTypes():
        ...
    def _packBonusBlock(self, bonus, camo, isApplied):
        ...

class ElementAwardTooltip(ElementTooltip):
    def __init__(self, context):
        ...
    def _packBonusBlock(self, bonus, camo, isApplied):
        ...

class ElementPurchaseTooltip(ElementTooltip):
    def __init__(self, context):
        ...
    @staticmethod
    def _getCustomizationTypes():
        ...
    def _packBonusBlock(self, bonus, camo, isApplied):
        ...
