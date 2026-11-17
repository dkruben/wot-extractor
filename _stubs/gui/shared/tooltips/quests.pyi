# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/tooltips/quests.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import constants as constants
from battle_pass_common import BATTLE_PASS_RANDOM_QUEST_ID_PREFIX as BATTLE_PASS_RANDOM_QUEST_ID_PREFIX
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from gui import makeHtmlString as makeHtmlString
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.ranked_battles.ranked_helpers import isRankedQuestID as isRankedQuestID
from gui.Scaleform.daapi.view.lobby.missions import missions_helper as missions_helper
from gui.Scaleform.genConsts.BLOCKS_TOOLTIP_TYPES import BLOCKS_TOOLTIP_TYPES as BLOCKS_TOOLTIP_TYPES
from gui.Scaleform.genConsts.ICON_TEXT_FRAMES import ICON_TEXT_FRAMES as ICON_TEXT_FRAMES
from gui.Scaleform.locale.ITEM_TYPES import ITEM_TYPES as ITEM_TYPES
from gui.Scaleform.locale.MENU import MENU as MENU
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS as TOOLTIPS
from gui.server_events import events_helpers as events_helpers
from gui.server_events.awards_formatters import TokenBonusFormatter as TokenBonusFormatter, PreformattedBonus as PreformattedBonus, LABEL_ALIGN as LABEL_ALIGN
from gui.server_events.bonuses import CustomizationsBonus as CustomizationsBonus
from gui.server_events.cond_formatters.tooltips import MissionsAccountRequirementsFormatter as MissionsAccountRequirementsFormatter
from gui.shared.formatters import text_styles as text_styles, icons as icons
from gui.shared.gui_items import GUI_ITEM_TYPE_NAMES as GUI_ITEM_TYPE_NAMES, GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.gui_items.Vehicle import getTypeSmallIconPath as getTypeSmallIconPath
from gui.shared.tooltips import TOOLTIP_TYPE as TOOLTIP_TYPE, formatters as formatters
from gui.shared.tooltips.common import BlocksTooltipData as BlocksTooltipData
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from gui.shared.utils import flashObject2Dict as flashObject2Dict
from gui.shared.utils.functions import makeTooltip as makeTooltip
from helpers import dependency as dependency, time_utils as time_utils
from helpers.i18n import makeString as _ms
from shared_utils import findFirst as findFirst
from skeletons.gui.server_events import IEventsCache as IEventsCache
from skeletons.gui.shared import IItemsCache as IItemsCache
from skeletons.gui.game_control import IQuestsController as IQuestsController, IRankedBattlesController as IRankedBattlesController, IBattleRoyaleController as IBattleRoyaleController, IComp7Controller as IComp7Controller
_MAX_AWARDS_PER_TOOLTIP = 5
_MAX_QUESTS_PER_TOOLTIP = 4
_MAX_BONUSES_PER_QUEST = 2
_RENT_TYPES: tuple

class _StringTokenBonusFormatter(TokenBonusFormatter):
    def format(self, bonus):
        ...
    def _formatComplexToken(self, complexToken, token, bonus):
        ...

class QuestsPreviewTooltipData(BlocksTooltipData):
    _questController: Any
    _eventsCache: Any
    __battleRoyaleController: Any
    __itemsCache: Any
    __comp7Controller: Any
    def __init__(self, context):
        ...
    def _getQuests(self, vehicle):
        ...
    def _packBlocks(self, *args, **kwargs):
        ...
    def __hasAnyUncompletedQuests(self):
        ...
    def __getQuestItem(self, quest):
        ...
    def _getHeader(self, count, vehicleName, description):
        ...
    def _getBottom(self, value):
        ...
    def _packBattlePassRandomQuest(self, questName, isAvailable):
        ...
    def _packQuest(self, questName, bonuses, isAvailable):
        ...
    def _getBody(self, text):
        ...
    def _isShowBottom(self, vehicle=None):
        ...

class ScheduleQuestTooltipData(BlocksTooltipData):
    _questController: Any
    def __init__(self, context):
        ...
    def _packBlocks(self, *args, **kwargs):
        ...
    def _getBody(self, eventID):
        ...
    def _getSubBlock(self, header, items, padding=None):
        ...

class UnavailableQuestTooltipData(BlocksTooltipData):
    _eventsCache: Any
    __rankedController: Any
    def __init__(self, context):
        ...
    def _packBlocks(self, *args, **kwargs):
        ...
    def __getBootom(self, text):
        ...
    def __getList(self, items):
        ...
    def __getListBlock(self, header, items, padding=None):
        ...
    def __getNotVehicle(self):
        ...
    def __getRankedOverrides(self, quest):
        ...

class AdditionalAwardTooltipData(BlocksTooltipData):
    def __init__(self, context):
        ...
    def _packBlocks(self, *args, **kwargs):
        ...
    def _packTitle(self):
        ...

class RentVehicleAwardTooltipData(BlocksTooltipData):
    def __init__(self, context):
        ...
    def _packBlocks(self, *args, **kwargs):
        ...

class MissionVehiclesConditionTooltipData(BlocksTooltipData):
    def __init__(self, context):
        ...
    def _packBlocks(self, *args, **kwargs):
        ...

class MissionVehiclesTypeTooltipData(BlocksTooltipData):
    def __init__(self, context):
        ...
    def _packBlocks(self, *args, **kwargs):
        ...
