# wot-extractor: STUB (.pyi) gerado a partir de sources/res/advent_calendar/scripts/client/advent_calendar/gui/impl/lobby/feature/bonus_grouper.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import Enum as Enum
from advent_calendar.gui.impl.lobby.feature.advent_helper import getFlattenedBonuses as getFlattenedBonuses
from gui.goodies.goodie_items import Booster as Booster, DemountKit as DemountKit, RecertificationForm as RecertificationForm, MentoringLicense as MentoringLicense
from gui.server_events.bonuses import C11nProgressTokenBonus as C11nProgressTokenBonus, splitBonuses as splitBonuses
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from helpers import dependency as dependency
from skeletons.gui.goodies import IGoodiesCache as IGoodiesCache

class QuestRewardsGroups(Enum):
    CURRENCIES_AND_PREMIUM = 'currenciesAndPremium'
    BOOSTERS = 'boosters'
    CUSTOMIZATIONS = 'customizations'
    CREW_BONUSES_OR_X5 = 'crewBonusesOrX5'
    PROGRESSION_REWARDS = 'progressionRewards'
    EXPERIMENTAL_EQUIPMENT_AND_COMPONENTS = 'experimentalEquipmentAndComponents'

class AdventCalendarQuestsBonusGrouper(object):
    __goodiesCache: Any
    _groupAndValueExtractors: Any
    def __init__(self, groupAndValueExtractorMapping=None):
        ...
    @staticmethod
    def _extractCurrency(bonus):
        ...
    @staticmethod
    def _extractTokens(bonus):
        ...
    @staticmethod
    def _extractCrewBook(_):
        ...
    @staticmethod
    def _extractCustomizations(bonus):
        ...
    @staticmethod
    def _extractCrewSkins(_):
        ...
    @staticmethod
    def _emptyExtractor(_):
        ...
    @staticmethod
    def _extractGoodies(bonus):
        ...
    @staticmethod
    def _extractItems(bonus):
        ...
    def group(self, quests):
        ...

class RewardsBonusGroups(Enum):
    CREW_MEMBER = 'crewMember'
    LOOTBOX = 'lootbox'
    PREMIUM = 'premium_plus'
    STYLE_2D = 'style'
    DECAL = 'projection_decal'
    RESERVE_CREDITS = 'booster_credits'
    RESERVE_EXP = 'booster_xp'
    RESERVE_COMBINED_EXP = 'booster_free_xp_and_crew_xp'
    CREW_BONUSES = 'booklet'
    RECERTIFICATION_FORM = 'recertificationForm'
    MENTORING_LICENSE = 'mentoringLicense'
    BATTLE_BONUS_5X = 'battleBonus5X'
    EXPERIMENTAL_EQUIPMENT = 'experimental_equipment'
    CREDITS = 'credits'
    COMPONENTS = 'equipCoin'
    FREEXP = 'freeXP'
    NONE = 'none'

class RewardBonusGrouper(object):
    _goodiesCache: Any
    _rewardsBonuses: Any
    _groupAndValueExtractors: Any
    def __init__(self, rewardsBonusGroup, groupAndValueExtractorMapping=None):
        ...
    def _extractCurrency(self, bonus):
        ...
    def _extractLootBoxes(self, _):
        ...
    def _extractCurrencies(self, bonus):
        ...
    def _extractTokens(self, bonus):
        ...
    def _extractCrewBook(self, _):
        ...
    def _extractCustomizations(self, bonus):
        ...
    def _extractProgressionCustomizations(self, _):
        ...
    def _extractTman(self, _):
        ...
    @staticmethod
    def _emptyExtractor(_):
        ...
    def _extractGoodies(self, bonus):
        ...
    def _extractItems(self, bonus):
        ...
    def group(self, bonuses):
        ...
