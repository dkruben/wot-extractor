# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/battle_results/packers/fun_packers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from fun_random_common.fun_constants import FunEfficiencyParameterCount as FunEfficiencyParameterCount
from fun_random.gui.battle_results.pbs_helpers import getTotalTMenXPToShow as getTotalTMenXPToShow, getTotalGoldToShow as getTotalGoldToShow, getEventID as getEventID, isCreditsShown as isCreditsShown, isGoldShown as isGoldShown, isXpShown as isXpShown, isFreeXpShown as isFreeXpShown, isTmenXpShown as isTmenXpShown, isCrystalShown as isCrystalShown, isFunAddXpBonusStatusAcceptable as isFunAddXpBonusStatusAcceptable
from fun_random.gui.feature.util.fun_mixins import FunAssetPacksMixin as FunAssetPacksMixin, FunSubModesWatcher as FunSubModesWatcher
from fun_random.gui.impl.gen.view_models.views.lobby.feature.battle_results.fun_battle_type import FunBattleType as FunBattleType
from fun_random.gui.impl.gen.view_models.views.lobby.feature.battle_results.fun_player_model import FunPlayerModel as FunPlayerModel
from fun_random.gui.impl.gen.view_models.views.lobby.feature.battle_results.fun_stats_efficiency_model import FunStatsEfficiencyModel as FunStatsEfficiencyModel
from fun_random.gui.impl.gen.view_models.views.lobby.feature.battle_results.fun_stats_efficiency_param_model import FunStatsEfficiencyParamModel as FunStatsEfficiencyParamModel, StatsValueType as StatsValueType
from fun_random.gui.impl.gen.view_models.views.lobby.feature.battle_results.fun_random_reward_item_model import FunRandomRewardItemModel as FunRandomRewardItemModel, FunRewardTypes as FunRewardTypes
from gui.battle_results.pbs_helpers.additional_bonuses import isAdditionalXpBonusAvailable as isAdditionalXpBonusAvailable, getLeftAdditionalBonus as getLeftAdditionalBonus
from gui.battle_results.pbs_helpers.economics import getTotalCreditsToShow as getTotalCreditsToShow, getTotalCrystalsToShow as getTotalCrystalsToShow, getTotalXPToShow as getTotalXPToShow, getTotalFreeXPToShow as getTotalFreeXPToShow
from gui.battle_results.presenters.packers.battle_info import BattleInfo as BattleInfo
from gui.battle_results.presenters.packers.personal_efficiency import PersonalEfficiency as PersonalEfficiency
from gui.battle_results.presenters.packers.personal_rewards import PersonalRewards as PersonalRewards
from gui.battle_results.presenters.packers.manageable_xp_multiplier import ManageableXpMultiplier as ManageableXpMultiplier
from gui.battle_results.presenters.packers.team.team_stats_packer import TeamStats as TeamStats
from gui.impl.gen.view_models.views.lobby.battle_results.efficiency_param_constants import EfficiencyParamConstants as EfficiencyParamConstants
from gui.impl.gen.view_models.views.lobby.battle_results.team_stats_model import SortingOrder as SortingOrder
from gui.impl.gen.view_models.views.lobby.battle_results.team_stats_column_types import TeamStatsColumnTypes as TeamStatsColumnTypes
from gui.shared.gui_items.Vehicle import VEHICLE_CLASS_NAME as VEHICLE_CLASS_NAME
from helpers import time_utils as time_utils
from gui.battle_results.reusable.shared import VehicleSummarizeInfo as VehicleSummarizeInfo

class FunRandomBattleInfo(BattleInfo, FunAssetPacksMixin, FunSubModesWatcher):
    _BATTLE_TYPE = FunBattleType.STANDARD
    @classmethod
    def packModel(cls, model, battleResults):
        ...

class FunRandomPersonalEfficiency(PersonalEfficiency, FunSubModesWatcher):
    _PARAMETERS: dict
    _DEFAULT_PARAMS: tuple
    @classmethod
    def _getParameterList(cls, vehicle, battleResults):
        ...

class FunRandomTeamStats(TeamStats):
    _PLAYER_MODEL_CLS = FunPlayerModel
    _SORTING_PRIORITIES: tuple
    _STATS_EFFICIENCY: tuple
    @classmethod
    def _packEfficiency(cls, efficiencyModel, summarizeInfo):
        ...

class FunRandomPersonalRewards(PersonalRewards):
    _AVAILABLE_REWARDS: list
    _ITEM_MODEL_CLS = FunRandomRewardItemModel
    _REWARD_GETTERS: dict
    _REWARDS_TO_CONDITION_MAP: dict

class FunRandomPremiumPlus(ManageableXpMultiplier):
    @classmethod
    def _updateLeftCount(cls, model, wasPremiumPlusInBattle, hasPremiumPlus, hasWotPlus):
        ...
    @classmethod
    def _getXpAdditionalBonusStatus(cls, arenaUniqueID, reusable, hasPremiumPlus):
        ...
