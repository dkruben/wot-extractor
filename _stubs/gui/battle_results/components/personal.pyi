# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_results/components/personal.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import random as random
from math import ceil as ceil
import BigWorld as BigWorld
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS as ARENA_BONUS_TYPE_CAPS
from constants import DEATH_REASON_ALIVE as DEATH_REASON_ALIVE, PREMIUM_TYPE as PREMIUM_TYPE, ARENA_GUI_TYPE as ARENA_GUI_TYPE, ATTACK_REASON_INDICES as ATTACK_REASON_INDICES, ATTACK_REASON as ATTACK_REASON
from debug_utils import LOG_ERROR as LOG_ERROR
from gui.battle_results.components import base as base
from gui.battle_results.components import shared as shared
from gui.battle_results.components import style as style
from gui.battle_results.pbs_helpers.additional_bonuses import isWotPlusBonusEnabledInConfig as isWotPlusBonusEnabledInConfig, getAccountStatusToBRPS as getAccountStatusToBRPS
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.lobby.premacc import premacc_helpers as premacc_helpers
from gui.Scaleform.genConsts.STORE_CONSTANTS import STORE_CONSTANTS as STORE_CONSTANTS
from gui.Scaleform.locale.BATTLE_RESULTS import BATTLE_RESULTS as BATTLE_RESULTS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS as TOOLTIPS
from gui.shared.crits_mask_parser import CRIT_MASK_SUB_TYPES as CRIT_MASK_SUB_TYPES
from gui.shared.formatters import numbers as numbers, icons as icons
from gui.shared.formatters import text_styles as text_styles
from gui.shared.gui_items.Vehicle import getSmallIconPath as getSmallIconPath, getTypeBigIconPath as getTypeBigIconPath, getNationLessName as getNationLessName, getIconShopPath as getIconShopPath
from gui.shared.utils.functions import makeTooltip as makeTooltip
from helpers import i18n as i18n, dependency as dependency, time_utils as time_utils
from skeletons.gui.battle_results import IBattleResultsService as IBattleResultsService
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache
_UNDEFINED_EFFICIENCY_VALUE = '-'
_logger: Any
NO_OWNER_DEATH_REASON_IDS: tuple

class PremiumAccountFlag(base.StatsItem):
    __slots__: tuple
    def _convert(self, value, reusable):
        ...

class PremiumPlusFlag(base.StatsItem):
    __slots__: tuple
    def _convert(self, value, reusable):
        ...

class DynamicPremiumState(base.StatsItem):
    __slots__: tuple
    __battleResults: Any
    __arenaUniqueID: Any
    __postBattlePremiumPlus: Any
    __xpDiff: Any
    __creditsDiff: Any
    __hasXpInBonusCaps: Any
    __hasXpBonusInBonusCaps: Any
    _value: Any
    def __init__(self, field, *path):
        ...
    def setRecord(self, record, reusable):
        ...
    def getVO(self):
        ...
    def __getIsApplied(self):
        ...

class PremiumInfoBlock(base.StatsBlock):
    __slots__: tuple
    __lobbyContext: Any
    __itemsCache: Any
    __allPremiumPlusCases: tuple
    __epicPremiumPlusCases: tuple
    availableEpicCases: list
    availableCases: list
    creditsPremiumBonusStr: Any
    xpPremiumBonusStr: Any
    premiumBonusStr: Any
    backgroundIcon: Any
    isGetPremium: Any
    isUpgradeToPremiumPlus: Any
    inBattleQueue: Any
    visibleDetailsBtn: Any
    __xpDiff: Any
    __creditsDiff: Any
    __canUpgradeToBasic: Any
    __canUpgradeToPlus: Any
    __adsCase: Any
    def __init__(self, meta=None, field='', *path):
        ...
    def setRecord(self, result, reusable):
        ...
    def getVO(self):
        ...
    def __setPremiumBonusData(self):
        ...

class IsTeamKillerFlag(base.StatsItem):
    __slots__: tuple
    def _convert(self, value, reusable):
        ...

class StunDataFlag(base.StatsItem):
    __slots__: tuple
    def _convert(self, value, reusable):
        ...

class PlayerNoClanFlag(base.StatsItem):
    __slots__: tuple
    def _convert(self, value, reusable):
        ...

class PlayerRank(base.StatsItem):
    __slots__: tuple
    def _convert(self, value, reusable):
        ...

class PersonalPlayerNameBlock(shared.PlayerNameBlock):
    __slots__: tuple
    def setRecord(self, result, reusable):
        ...

class KillerPlayerNameBlock(shared.PlayerNameBlock):
    __slots__: tuple
    killerID: Any
    fakeNameLabel: Any
    def __init__(self, killerID, meta=None, field='', *path):
        ...
    def setRecord(self, result, reusable):
        ...
    def __setKillerInfo(self, killerInfo, reusable):
        ...
    def __getFakeNameLabel(self, killerInfo, reusable):
        ...

class DetailsPlayerNameBlock(shared.PlayerNameBlock):
    __slots__: tuple

class PersonalVehicleNamesBlock(base.StatsBlock):
    __slots__: tuple
    def setRecord(self, result, reusable):
        ...

class PersonalVehicleTypeIconsBlock(base.StatsBlock):
    __slots__: tuple
    def setRecord(self, result, reusable):
        ...

class EpicVehicleNamesBlock(PersonalVehicleNamesBlock):
    __slots__: tuple
    def setRecord(self, result, reusable):
        ...

class PersonalVehicleBlock(base.StatsBlock):
    __slots__: tuple
    killerID: Any
    deathReason: Any
    isVehicleStatusDefined: Any
    vehicleIcon: Any
    vehicleLevel: Any
    nationName: Any
    isPrematureLeave: Any
    vehicleState: Any
    def setVehicle(self, item):
        ...
    def setRecord(self, result, reusable):
        ...
    def _getVehicleIcon(self, item):
        ...

class EpicVehicleBlock(PersonalVehicleBlock):
    def _getVehicleIcon(self, item):
        ...

class PersonalVehiclesBlock(base.StatsBlock):
    __slots__: tuple
    def setRecord(self, result, reusable):
        ...
    def _createComponent(self):
        ...

class EpicVehiclesBlock(PersonalVehiclesBlock):
    __slots__: tuple
    def setRecord(self, result, reusable):
        ...
    def _createComponent(self):
        ...

class _DetailsBlock(base.StatsBlock):
    __slots__: tuple
    _isEmpty: Any
    def __init__(self, meta=None, field='', *path):
        ...
    def isEmpty(self):
        ...

class DamageDetailsBlock(_DetailsBlock):
    __slots__: tuple
    piercings: Any
    damageDealtValues: Any
    damageDealtNames: Any
    _isEmpty: Any
    def __init__(self, meta=None, field='', *path):
        ...
    def setRecord(self, result, reusable):
        ...

class ArmorUsingDetailsBlock(_DetailsBlock):
    __slots__: tuple
    usedArmorCount: Any
    armorValues: Any
    armorNames: Any
    _isEmpty: Any
    def __init__(self, meta=None, field='', *path):
        ...
    def setRecord(self, result, _):
        ...

class AssistDetailsBlock(_DetailsBlock):
    __slots__: tuple
    damageAssisted: Any
    damageAssistedValues: Any
    damageAssistedNames: Any
    _isEmpty: Any
    def __init__(self, meta=None, field='', *path):
        ...
    def setRecord(self, result, reusable):
        ...

class StunDetailsBlock(_DetailsBlock):
    __slots__: tuple
    stunNum: Any
    stunValues: Any
    stunNames: Any
    stunDuration: Any
    _isEmpty: Any
    def __init__(self, meta=None, field='', *path):
        ...
    def setRecord(self, result, _):
        ...

class CritsDetailsBlock(_DetailsBlock):
    __slots__: tuple
    critsCount: Any
    criticalDevices: Any
    destroyedDevices: Any
    destroyedTankmen: Any
    _isEmpty: Any
    def __init__(self, meta=None, field='', *path):
        ...
    def setRecord(self, result, reusable):
        ...

class TeamBaseDetailsBlock(base.StatsBlock):
    __slots__: tuple
    _showCapturePoints: Any
    _showDefencePoints: Any
    label: Any
    captureTotalItems: Any
    defenceTotalItems: Any
    captureValues: Any
    captureNames: Any
    defenceValues: Any
    defenceNames: Any
    isEnemyBase: Any
    def __init__(self, meta=None, field='', *path):
        ...
    def setRecord(self, result, _):
        ...

class EnemyTeamBaseDetailBlock(TeamBaseDetailsBlock):
    __slots__: tuple
    _showCapturePoints: Any
    label: Any
    isEnemyBase: Any
    def __init__(self, meta=None, field='', *path):
        ...

class AllyTeamBaseDetailBlock(TeamBaseDetailsBlock):
    __slots__: tuple
    _showDefencePoints: Any
    label: Any
    isEnemyBase: Any
    def __init__(self, meta=None, field='', *path):
        ...

class EnemyDetailsBlock(_DetailsBlock):
    __slots__: tuple
    deathReason: Any
    spotted: Any
    piercings: Any
    damageDealt: Any
    killCount: Any
    _isEmpty: Any
    vehicleIcon: Any
    vehicleName: Any
    def setRecord(self, result, reusable):
        ...
    def _setVehicle(self, vehicle):
        ...
    def _setPlayerInfo(self, info):
        ...
    def setDeathReason(self, reason):
        ...

class TotalEfficiencyDetailsHeader(base.StatsBlock):
    __slots__: tuple
    kills: Any
    damageDealt: Any
    criticalDamages: Any
    damageBlockedByArmor: Any
    damageAssisted: Any
    damageAssistedStun: Any
    spotted: Any
    killsTooltip: Any
    damageDealtTooltip: Any
    criticalDamagesTooltip: Any
    damageBlockedTooltip: Any
    damageAssistedTooltip: Any
    damageAssistedStunTooltip: Any
    spottedTooltip: Any
    hasEfficencyStats: Any
    def __init__(self, meta=None, field='', *path):
        ...
    def setRecord(self, result, reusable):
        ...
    @classmethod
    def __makeEfficiencyHeaderTooltip(cls, key, value):
        ...
    @classmethod
    def __formatter(cls, value):
        ...

class TotalEfficiencyDetailsBlock(base.StatsBlock):
    __slots__: tuple
    def setRecord(self, result, reusable):
        ...

class TotalPersonalAchievementsBlock(shared.BiDiStatsBlock):
    __slots__: tuple
    def addComponent(self, index, component):
        ...
    def setRecord(self, result, reusable):
        ...

class PersonalAccountDBID(base.StatsItem):
    def _convert(self, value, reusable):
        ...

class CommendationsReceived(base.StatsItem):
    __slots__: tuple
    def _convert(self, record, reusable):
        ...

def fillKillerInfoBlock(vehicleStateBlock, deathReason, killerID, reusable, result):
    ...
