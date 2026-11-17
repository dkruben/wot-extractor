# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/battle_results/components.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from collections import defaultdict as defaultdict
from future.utils import lfilter as lfilter, viewitems as viewitems
from past.builtins import long as long
from constants import ARENA_BONUS_TYPE as ARENA_BONUS_TYPE, DEATH_REASON_ALIVE as DEATH_REASON_ALIVE
from gui.battle_control.battle_constants import WinStatus as WinStatus
from gui.battle_results.components import base as base
from gui.battle_results.components.personal import PersonalVehiclesBlock as PersonalVehiclesBlock
from gui.battle_results.progress.progress_helpers import isQuestCompleted as isQuestCompleted
from gui.battle_results.reusable import sort_keys as sort_keys
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.server_events import IEventsCache as IEventsCache
from gui.server_events.battle_royale_formatters import SOLO_ITEMS_ORDER as SOLO_ITEMS_ORDER, SQUAD_ITEMS_ORDER as SQUAD_ITEMS_ORDER, StatsItemType as StatsItemType
from gui.server_events.events_helpers import isBattleRoyale as isBattleRoyale
from gui.shared.utils.functions import replaceHyphenToUnderscore as replaceHyphenToUnderscore
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from skeletons.gui.game_control import IBattleRoyaleController as IBattleRoyaleController
from ValueReplay import ValueReplay as ValueReplay, ValueReplayConnector as ValueReplayConnector
from battle_results import g_config as battleResultsConfig
from gui.battle_results.reusable import records as records
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui.shared.money import Currency as Currency
_logger: Any
_THE_BEST_RANK = 1

class BattleRoyaleArenaNameBlock(base.StatsItem):
    __slots__: tuple
    def _convert(self, value, reusable):
        ...

class ArenaBonusTypeNameBlock(base.StatsItem):
    __slots__: tuple
    def _convert(self, value, reusable):
        ...

class PersonalPlayerNameBlock(base.StatsBlock):
    __slots__: tuple
    userName: Any
    clanAbbrev: Any
    def __init__(self, meta=None, field='', *path):
        ...
    def setRecord(self, result, reusable):
        ...

class BattleRoyalePlayerPlaceBlock(base.StatsItem):
    __slots__: tuple
    __sessionProvider: Any
    def _convert(self, value, reusable):
        ...

class BattleRoyaleIsSquadModeBlock(base.StatsItem):
    __slots__: tuple
    def _convert(self, value, reusable):
        ...

class BattleRoyalePersonalVehicleBlock(base.StatsBlock):
    __slots__: tuple
    vehicleName: Any
    vehicleType: Any
    isObserver: Any
    def __init__(self, meta=None, field='', *path):
        ...
    def setVehicle(self, item):
        ...
    def setRecord(self, result, reusable):
        ...

class BattleRoyaleVehiclesBlock(PersonalVehiclesBlock):
    __slots__: tuple
    def _createComponent(self):
        ...

class BattleRoyaleIsPremiumBlock(base.StatsItem):
    __slots__: tuple
    def _convert(self, value, reusable):
        ...

class BattleRoyaleDailyBonusFactorBlock(base.StatsBlock):
    __slots__: tuple
    dailyBonusFactor: Any
    def __init__(self, meta=None, field='', *path):
        ...
    def setRecord(self, result, reusable):
        ...

class BattleRoyaleVehicleStatusBlock(base.StatsBlock):
    __itemsCache: Any
    __slots__: tuple
    killer: Any
    vehicleState: Any
    isSelfDestroyer: Any
    def __init__(self, meta=None, field='', *path):
        ...
    def setRecord(self, result, reusable):
        ...

class _BRCoinReplayRecords(records.ReplayRecords):
    __slots__: tuple
    def __init__(self, replay, results):
        ...

class _STPCoinReplayRecords(records.ReplayRecords):
    __slots__: tuple
    def __init__(self, replay, results):
        ...

class BattleRoyaleFinancialBlock(base.StatsBlock):
    __slots__: tuple
    __eventsCache: Any
    credits: Any
    xp: Any
    crystal: Any
    brcoin: Any
    stpcoin: Any
    def __init__(self, meta=None, field='', *path):
        ...
    def setRecord(self, result, reusable):
        ...
    def _getBrCoins(self, result, reusable, isPremium):
        ...
    def _getStpCoins(self, result, reusable):
        ...
    def __getCoinsQuestBonus(self, questProgress, currencyCode):
        ...

class BattleRoyaleFinancialPremBlock(BattleRoyaleFinancialBlock):
    brcoin: Any
    stpcoin: Any
    credits: Any
    crystal: Any
    xp: Any
    def setRecord(self, result, reusable):
        ...

class BattleRoyaleStatsItemBlock(base.StatsBlock):
    __slots__: tuple
    _ICON_PATH = R.images.battle_royale.gui.maps.icons.battleResults.stat_list
    _DEFAULT_ICON = _ICON_PATH.wreath_transparent
    type: Any
    value: Any
    maxValue: Any
    wreathImage: Any
    def __init__(self, itemType, meta=None, field='', *path):
        ...
    def setRecord(self, result, reusable):
        ...
    def _getValue(self, result, reusable):
        ...
    def _getMaxValue(self, result, reusable):
        ...
    def _getWreathImage(self, result, reusable):
        ...
    def _isTop(self, result, reusable):
        ...

class SimpleEfficiencyParameter(BattleRoyaleStatsItemBlock):
    __slots__: tuple
    def _getValue(self, result, reusable):
        ...
    def _isTop(self, result, reusable):
        ...

class PlaceParameter(BattleRoyaleStatsItemBlock):
    __slots__: tuple
    def _getValue(self, result, reusable):
        ...
    def _getMaxValue(self, result, reusable):
        ...
    def _getWreathImage(self, result, reusable):
        ...

class KilledBySquadParameter(BattleRoyaleStatsItemBlock):
    __slots__: tuple
    def _getValue(self, result, reusable):
        ...
    def _isTop(self, result, reusable):
        ...

class BattleRoyaleStatsBlock(base.StatsBlock):
    __slots__: tuple
    _itemsFactory: dict
    def setRecord(self, result, reusable):
        ...

class BattleRoyaleRewardsBlock(base.StatsBlock):
    __slots__: tuple
    __eventsCache: Any
    __battleRoyaleController: Any
    __QUESTS_WITH_MEDALS: Any
    achievements: Any
    bonuses: Any
    completedQuestsCount: Any
    completedQuests: Any
    brAwardTokens: Any
    def __init__(self, meta=None, field='', *path):
        ...
    def setRecord(self, result, reusable):
        ...
    def __getAchievements(self, questProgress, allQuests):
        ...
    def __getAchievementQuestsCondition(self, qID, _):
        ...
    def __getDailyQuestsCondition(self, qID, allQuests):
        ...
    @staticmethod
    def __getCompletedQuests(questProgress, condition, allQuests):
        ...
    @staticmethod
    def __getBonuses(allQuests, completedQuests):
        ...
    @staticmethod
    def __getBrAwardTokens(result):
        ...

class BattlePassBlock(base.StatsBlock):
    __slots__: tuple
    bpTopPoints: Any
    def __init__(self, meta=None, field='', *path):
        ...
    def setRecord(self, result, reusable):
        ...

class BattleRoyalePlayerBlock(base.StatsBlock):
    __slots__: tuple
    isPersonal: Any
    userName: Any
    hiddenName: Any
    clanAbbrev: Any
    place: Any
    squadIdx: Any
    isPersonalSquad: Any
    achievedLevel: Any
    kills: Any
    damage: Any
    vehicleName: Any
    vehicleType: Any
    databaseID: Any
    prebattleID: Any
    def __init__(self, meta=None, field='', *path):
        ...
    def setRecord(self, result, reusable):
        ...

class BattleRoyaleTeamStatsBlock(base.StatsBlock):
    __slots__: tuple
    def setRecord(self, result, reusable):
        ...

def _isSquadMode(reusable):
    ...
