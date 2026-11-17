# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/impl/lobby/common/fun_view_helpers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
from account_helpers.AccountSettings import AccountSettings as AccountSettings, FUN_RANDOM_PROGRESSION as FUN_RANDOM_PROGRESSION, FUN_RANDOM_PROGR_PREV_COUNTER as FUN_RANDOM_PROGR_PREV_COUNTER, FUN_RANDOM_INF_PROGR_PREV_COUNTER as FUN_RANDOM_INF_PROGR_PREV_COUNTER, FUN_RANDOM_INF_PROGR_PREV_COMPLETE_COUNT as FUN_RANDOM_INF_PROGR_PREV_COMPLETE_COUNT
from typing import Any as Any, Dict as Dict, List as List, Optional as Optional, Tuple as Tuple, Union as Union, TYPE_CHECKING as TYPE_CHECKING
import math_utils as math_utils
from fun_random.gui.impl.gen.view_models.views.lobby.common.fun_random_progression_stage import FunRandomProgressionStage as FunRandomProgressionStage, Rarity as Rarity
from fun_random.gui.impl.gen.view_models.views.lobby.common.fun_random_progression_state import FunRandomProgressionStatus as FunRandomProgressionStatus
from fun_random.gui.impl.gen.view_models.views.lobby.common.fun_random_quest_card_model import FunRandomQuestCardModel as FunRandomQuestCardModel, CardState as CardState
from fun_random.gui.impl.lobby.common.lootboxes import FunRandomLootBoxTokenBonusPacker as FunRandomLootBoxTokenBonusPacker, FunRandomRewardLootBoxTokenBonusPacker as FunRandomRewardLootBoxTokenBonusPacker, FunRandomLootBoxVehiclesBonusUIPacker as FunRandomLootBoxVehiclesBonusUIPacker, FEP_CATEGORY as FEP_CATEGORY
from fun_random.gui.feature.fun_constants import FunSubModesState as FunSubModesState
from fun_random.gui.fun_account_settings import FunAccountSettings as FunAccountSettings
from fun_random.gui.feature.sub_systems.fun_performance_analyzers import PerformanceGroup as PerformanceGroup
from gui.impl import backport as backport
from gui.impl.auxiliary.collections_helper import TmanTemplateBonusPacker as TmanTemplateBonusPacker
from gui.impl.auxiliary.rewards_helper import BlueprintBonusTypes as BlueprintBonusTypes
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.common.mode_performance_model import PerformanceRiskEnum as PerformanceRiskEnum
from gui.impl.gen.view_models.views.lobby.user_missions.constants.event_banner_state import EventBannerState as EventBannerState
from gui.impl.lobby.common.view_helpers import packBonusModelAndTooltipData as packBonusModelAndTooltipData
from gui.server_events.bonuses import LootBoxTokensBonus as LootBoxTokensBonus, mergeBonuses as mergeBonuses
from gui.shared.formatters import time_formatters as time_formatters
from gui.shared.formatters.ranges import toRomanRangeString as toRomanRangeString
from gui.shared.missions.packers.bonus import BonusUIPacker as BonusUIPacker, ExtendedBlueprintBonusUIPacker as ExtendedBlueprintBonusUIPacker, getDefaultBonusPackersMap as getDefaultBonusPackersMap, Customization3Dand2DbonusUIPacker as Customization3Dand2DbonusUIPacker, VehiclesBonusUIPacker as VehiclesBonusUIPacker
from helpers import dependency as dependency
from shared_utils import first as first, findFirst as findFirst
from skeletons.gui.shared import IItemsCache as IItemsCache
from frameworks.wulf import Array as Array
from fun_random.gui.feature.models.common import FunSubModesStatus as FunSubModesStatus
from fun_random.gui.feature.models.progressions import FunProgression as FunProgression
from fun_random.gui.impl.gen.view_models.views.lobby.common.fun_random_progression_state import FunRandomProgressionState as FunRandomProgressionState
from gui.server_events.bonuses import SimpleBonus as SimpleBonus
from gui.impl.gen.view_models.common.missions.bonuses.bonus_model import BonusModel as BonusModel
from gui.impl.gen.view_models.common.missions.bonuses.item_bonus_model import ItemBonusModel as ItemBonusModel
from gui.impl.gen.view_models.views.lobby.common.mode_performance_model import ModePerformanceModel as ModePerformanceModel
from fun_random.gui.impl.gen.view_models.views.lobby.common.fun_random_progression_condition import FunRandomProgressionCondition as FunRandomProgressionCondition
from fun_random.gui.impl.gen.view_models.views.lobby.common.fun_random_infinite_progression_condition import FunRandomInfiniteProgressionCondition as FunRandomInfiniteProgressionCondition
from fun_random.gui.impl.gen.view_models.views.lobby.tooltips.fun_random_base_quest_tooltip_view_model import FunRandomBaseQuestTooltipViewModel as FunRandomBaseQuestTooltipViewModel
from fun_random.gui.server_events.event_items import FunProgressionTriggerQuest as FunProgressionTriggerQuest
_PROGRESSION_STATUS_MAP: dict
_EVENT_STATE_MAP: dict
_PERFORMANCE_GROUP_TO_RISK_ENUM: dict
FUN_RANDOM_MAPPING: dict
RARITY_ORDER: tuple
LOOTBOX_TYPE = 'fep_{0}'
RARITY_VALUES: _Any

def getFormattedTimeLeft(seconds):
    ...
def getConditionText(rootStrPath, levels):
    ...
def getFunRandomEventState(status):
    ...
def getFunRandomBonusPacker():
    ...
def getCompensatedFunRandomBonusPacker():
    ...
def getFunRandomSpecialBonusPacker():
    ...
def defineProgressionStatus(progression):
    ...
def packAdditionalRewards(progression, stageIndex, showCount, isSpecial=False):
    ...
def packBonuses(bonuses, showCount, isSpecial):
    ...
def packProgressionActiveStage(progression, stageModel, isSpecial=False, tooltips=None):
    ...
def packInfiniteProgressionStage(progression, stageModel, isSpecial=False, tooltips=None):
    ...
def packFullProgressionConditions(modeUserName, progression, conditionModel):
    ...
def packProgressionConditions(progression, conditionModel):
    ...
def packFullInfiniteProgressionConditions(modeUserName, progression, conditionModel):
    ...
def packInfiniteProgressionConditions(progression, conditionModel):
    ...
def packProgressionStages(progression, stagesModel, tooltips=None):
    ...
def packProgressionState(progression, stateModel):
    ...
def packInfiniteProgressionState(progression, stateModel):
    ...
def packStageRewards(bonuses, rewardsModel, isSpecial=False, tooltips=None):
    ...
def packPerformanceAlertInfo(performanceModel, performanceGroup, default=...):
    ...
def sortFunProgressionBonuses(bonuses):
    ...
def _packConditions(conditionModel, statusTimer, text, triggers):
    ...
def _packTriggers(triggers, cardsModel):
    ...
def packQuestTooltip(tooltipModel, progression, assetsPointer):
    ...
def packTrigger(cardModel, trigger):
    ...
def _packStage(bonuses, currentPoints, requiredPoints, maximumPoints, isCompleted, stageModel, isSpecial=False, tooltips=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def _getStageRarity(bonuses, itemsCache=None):
    ...
