# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/tooltips/personal_missions.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from future.utils import iteritems as iteritems, itervalues as itervalues
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from gui import GUI_NATIONS as GUI_NATIONS
from gui.Scaleform import getNationsFilterAssetPath as getNationsFilterAssetPath
from gui.Scaleform.daapi.view.lobby.hangar.header_helpers.personal_mission_flags import HANGAR_HEADER_QUESTS_TO_PM_BRANCH as HANGAR_HEADER_QUESTS_TO_PM_BRANCH
from gui.Scaleform.daapi.view.lobby.missions import missions_helper as missions_helper
from gui.Scaleform.daapi.view.lobby.missions.awards_formatters import TooltipOperationAwardComposer as TooltipOperationAwardComposer, TooltipPostponedOperationAwardComposer as TooltipPostponedOperationAwardComposer
from gui.Scaleform.daapi.view.lobby.server_events.events_helpers import getNationsForChain as getNationsForChain
from gui.Scaleform.genConsts.BLOCKS_TOOLTIP_TYPES import BLOCKS_TOOLTIP_TYPES as BLOCKS_TOOLTIP_TYPES
from gui.Scaleform.genConsts.HANGAR_HEADER_QUESTS import HANGAR_HEADER_QUESTS as HANGAR_HEADER_QUESTS
from gui.Scaleform.genConsts.ICON_TEXT_FRAMES import ICON_TEXT_FRAMES as ICON_TEXT_FRAMES
from gui.Scaleform.genConsts.PERSONAL_MISSIONS_ALIASES import PERSONAL_MISSIONS_ALIASES as PERSONAL_MISSIONS_ALIASES
from gui.Scaleform.locale.NATIONS import NATIONS as NATIONS
from gui.Scaleform.locale.PERSONAL_MISSIONS import PERSONAL_MISSIONS as PERSONAL_MISSIONS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS as TOOLTIPS
from gui.Scaleform.settings import BADGES_ICONS as BADGES_ICONS, BADGES_STRIPS_ICONS as BADGES_STRIPS_ICONS
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.personal_missions_30.common.enums import OperationState as OperationState
from gui.impl.lobby.missions.missions_helpers import formatCompleteCount as formatCompleteCount
from gui.impl.lobby.personal_missions_30.views_helpers import getOperationStatus as getOperationStatus, isOperationAvailableByVehicles as isOperationAvailableByVehicles, wasOperationActivatedBefore as wasOperationActivatedBefore, getPMInstalledVehDetails as getPMInstalledVehDetails
from gui.server_events.awards_formatters import AWARDS_SIZES as AWARDS_SIZES, CompletionTokensBonusFormatter as CompletionTokensBonusFormatter, getPersonalMissionsOperationTooltipsPacker as getPersonalMissionsOperationTooltipsPacker
from gui.server_events.events_helpers import AwardSheetPresenter as AwardSheetPresenter
from gui.server_events.personal_progress.formatters import PMTooltipConditionsFormatters as PMTooltipConditionsFormatters
from gui.shared.formatters import text_styles as text_styles, icons as icons
from gui.shared.tooltips import TOOLTIP_TYPE as TOOLTIP_TYPE, formatters as formatters
from gui.shared.tooltips.common import BlocksTooltipData as BlocksTooltipData
from gui.shared.utils import getPlayerName as getPlayerName
from helpers import dependency as dependency
from helpers.i18n import makeString as _ms
from helpers.i18n import doesTextExist as doesTextExist
from nations import ALLIANCES_TAGS_ORDER as ALLIANCES_TAGS_ORDER, ALLIANCE_IDS as ALLIANCE_IDS
from personal_missions import PM_BRANCH as PM_BRANCH
from potapov_quests import PM_BRANCH_TO_FREE_TOKEN_NAME as PM_BRANCH_TO_FREE_TOKEN_NAME
from shared_utils import first as first, findFirst as findFirst
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.server_events import IEventsCache as IEventsCache
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui.server_events.event_items import PMOperation as PMOperation
from gui.shared.tooltips.contexts import PersonalMissionOperationContext as PersonalMissionOperationContext
from typing import Dict as Dict, List as List, Tuple as Tuple

class UniqueCamouflageTooltip(BlocksTooltipData):
    def __init__(self, context):
        ...
    def _packBlocks(self, *args, **kwargs):
        ...

class BasicFreeSheetTooltip(BlocksTooltipData):
    def __init__(self, context):
        ...
    def _packBlocks(self, *args, **kwargs):
        ...
    def _getInfoBlock(self):
        ...
    def _getDescriptionBlock(self):
        ...

class FreeSheetTooltip(BasicFreeSheetTooltip):
    def _getDescriptionBlock(self):
        ...
    def _getMainBlock(self):
        ...
    def _getFooterBlock(self):
        ...

class FreeSheetReturnTooltip(FreeSheetTooltip):
    def _getInfoBlock(self):
        ...

class FreeSheetNotEnoughTooltip(FreeSheetTooltip):
    def _getInfoBlock(self):
        ...
    def _getFooterBlock(self):
        ...

class FreeSheetUsedTooltip(BasicFreeSheetTooltip):
    def _getDescriptionBlock(self):
        ...

class BadgeTooltipData(BlocksTooltipData):
    __itemsCache: Any
    def __init__(self, context):
        ...
    def _packBlocks(self, badgeID, isSuffixLayout=False):
        ...
    @staticmethod
    def __getImageBlock(badge):
        ...

class LoyalServiceTooltipData(BadgeTooltipData):
    def _getDescription(self):
        ...

class OperationsChainDetailsTooltipData(BlocksTooltipData):
    def __init__(self, context):
        ...
    def _packBlocks(self, chainID):
        ...

class OperationTooltipData(BlocksTooltipData):
    PROGRESS_COUNT_TEMPLATE = '/ %s'
    __eventsCache: Any
    __settingsCore: Any
    def __init__(self, context):
        ...
    def _packBlocks(self, *args, **kwargs):
        ...
    @classmethod
    def _getTitleBlock(cls, operation):
        ...
    @classmethod
    def _getMissionsBlock(cls, operation):
        ...
    @classmethod
    def _getAwardsBlock(cls, bonuses, operation):
        ...
    @classmethod
    def _getStatusBlock(cls, operation):
        ...
    @classmethod
    def _getOperationCompletionTokensCount(cls, operation):
        ...
    @staticmethod
    def _getOperationCompletionTokensDescription(operation):
        ...
    @staticmethod
    def _getTooltipFormatter():
        ...
    @staticmethod
    def _getOperationOperationStateIcon(state):
        ...
    @classmethod
    def _isOperationUnavailable(cls, operation):
        ...
    @classmethod
    def _isOperationPaused(cls, operation):
        ...
    @classmethod
    def _isOperationInProgress(cls, operation):
        ...

class OperationPostponedTooltipData(OperationTooltipData):
    _lobbyCtx: Any
    @classmethod
    def _getMissionsBlock(cls, _):
        ...
    @classmethod
    def _getAwardsBlock(cls, bonuses, _):
        ...
    @classmethod
    def _getStatusBlock(cls, operation):
        ...
    @staticmethod
    def _getTooltipFormatter():
        ...

class PersonalMissionInfoTooltipData(BlocksTooltipData):
    _eventsCache: Any
    def __init__(self, context):
        ...
    def _getTitleBlock(self, quest):
        ...
    def _getDescriptionBlock(self, localizationKey):
        ...
    def _getLimiterBlock(self, localizationKey):
        ...
    def _getWarningBlock(self, localizationKey):
        ...
    def _packBlocks(self, *args, **kwargs):
        ...

class PersonalMissionsMapRegionTooltipData(BlocksTooltipData):
    _hasOrCondition: Any
    _quest: Any
    def __init__(self, context):
        ...
    def _getPersonalMission(self, *args, **kwargs):
        ...
    def _packBlocks(self, *args, **kwargs):
        ...
    def _getTitleBlock(self):
        ...
    def _getConditionsTitleBlock(self):
        ...
    @classmethod
    def _getAndConditionsBlock(cls, conditions, padding):
        ...
    @classmethod
    def _getOrConditionBlock(cls, conditions):
        ...
    @classmethod
    def _getAwardsBlock(cls, quest):
        ...
    @classmethod
    def _getStatusBlock(cls, quest):
        ...
    @staticmethod
    def __getOperationOperationStateIcon(state):
        ...

class PersonalMissionPreviewTooltipData(PersonalMissionsMapRegionTooltipData):
    def _getPersonalMission(self, questType=..., *args, **kwargs):
        ...

class TankwomanTooltipData(BlocksTooltipData):
    def __init__(self, context):
        ...
    def _packBlocks(self, *args, **kwargs):
        ...
    def __makeImageBlock(self, icon, text, imgPaddingLeft=15, imgPaddingRight=30, imgPaddingTop=0):
        ...

class TankModuleTooltipData(BlocksTooltipData):
    def __init__(self, context):
        ...
    def _packBlocks(self, operationID, classifier):
        ...
    def __getObtainedStatus(self, isAlliance):
        ...
    def __getNotObtainedStatus(self, isAlliance):
        ...
    def __getAvailableStatus(self, pawnsCount):
        ...
