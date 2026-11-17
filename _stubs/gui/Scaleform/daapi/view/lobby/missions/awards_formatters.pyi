# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/missions/awards_formatters.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from future.utils import viewvalues as viewvalues, viewitems as viewitems
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.Scaleform.locale.QUESTS import QUESTS as QUESTS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.impl.lobby.missions.missions_helpers import formatCompleteCount as formatCompleteCount
from gui.server_events import finders as finders
from gui.server_events.awards_formatters import AWARDS_SIZES as AWARDS_SIZES, LABEL_ALIGN as LABEL_ALIGN, PACK_RENT_VEHICLES_BONUS as PACK_RENT_VEHICLES_BONUS, PostProcessTags as PostProcessTags, PreformattedBonus as PreformattedBonus, QuestsBonusComposer as QuestsBonusComposer, formatCountLabel as formatCountLabel, getBattlePassAwardsPacker as getBattlePassAwardsPacker, getOperationPacker as getOperationPacker, getPersonalMissionAwardPacker as getPersonalMissionAwardPacker
from gui.server_events.bonuses import FreeTokensBonus as FreeTokensBonus
from gui.shared.formatters import text_styles as text_styles
from helpers import dependency as dependency, i18n as i18n
from skeletons.gui.server_events import IEventsCache as IEventsCache
from skeletons.gui.shared import IItemsCache as IItemsCache
_OPERATION_AWARDS_COUNT = 3
DISPLAY_ALL_AWARDS = -1

class CurtailingAwardsComposer(QuestsBonusComposer):
    _displayedRewardsCount: Any
    def __init__(self, displayedAwardsCount, awardsFormatter=None):
        ...
    def getShortBonusesData(self, bonuses):
        ...
    def _isMergeAllow(self):
        ...
    def _packBonuses(self, preformattedBonuses, size):
        ...
    def _packBonus(self, bonus, size=...):
        ...
    def _packMergedBonuses(self, mergedBonuses, size=...):
        ...
    @classmethod
    def _getShortBonusesData(cls, preformattedBonuses, size=...):
        ...

class TwitchAwardsComposer(CurtailingAwardsComposer):
    def _packBonus(self, bonus, size=...):
        ...
    def _packMergedBonuses(self, mergedBonuses, size=...):
        ...

class BattlePassAwardsComposer(CurtailingAwardsComposer):
    _displayedRewardsCount: Any
    def __init__(self, displayedAwardsCount=1, awardsFormatter=None):
        ...
    def setDisplayedCount(self, count):
        ...
    def _packMergedBonuses(self, mergedBonuses, size=...):
        ...

class RawLabelBonusComposer(QuestsBonusComposer):
    __slots__: tuple
    def _packBonus(self, bonus, size=...):
        ...

class AwardsWindowComposer(CurtailingAwardsComposer):
    @classmethod
    def _getShortBonusesData(cls, preformattedBonuses, size=...):
        ...

class DetailedCardAwardComposer(CurtailingAwardsComposer):
    def getFormattedBonuses(self, bonuses, bigAwardsCount=6):
        ...

class PackRentVehiclesAwardComposer(CurtailingAwardsComposer):
    def _packBonuses(self, preformattedBonuses, size):
        ...

class BonusNameQuestsBonusComposer(PackRentVehiclesAwardComposer):
    def _packBonus(self, bonus, size=...):
        ...

class LootBoxBonusComposer(BonusNameQuestsBonusComposer):
    def getVisibleFormattedBonuses(self, bonuses, alwaysVisibleBonuses, size=..., sortKey=None):
        ...

class NewStyleBonusComposer(LootBoxBonusComposer):
    ...

class PersonalMissionsAwardComposer(CurtailingAwardsComposer):
    _displayedAwardsCount: Any
    def __init__(self, displayedAwardsCount, packer=None):
        ...
    def getFormattedBonuses(self, bonuses, size=..., gap=0, isObtained=False, obtainedImage='', obtainedImageOffset=0):
        ...
    def getPawnedQuestBonuses(self, bonuses, size=..., gap=0, isObtained=False, pawnedTokensCount=0, obtainedImage='', obtainedImageOffset=0, freeTokenName=''):
        ...
    def getReturnTokensQuestBonuses(self, bonuses, size=..., gap=0, isObtained=False, returnedTokensCount=0, obtainedImage='', obtainedImageOffset=0, freeTokenName=''):
        ...
    def _packBonuses(self, preformattedBonuses, size, gap=0, isObtained=False, obtainedImage='', obtainedImageOffset=0):
        ...
    def _packBonus(self, bonus, size=..., gap=0, isObtained=False, obtainedImage='', obtainedImageOffset=0):
        ...

class MainOperationAwardComposer(PersonalMissionsAwardComposer):
    _eventsCache: Any
    _TANKWOMAN_BONUS = 'tankwoman'
    def __init__(self, packer=None):
        ...
    def getFormattedBonuses(self, operation, size=..., gap=0):
        ...
    def _getBonuses(self, operation):
        ...
    def _getPreformattedTankwomanBonus(self, operation):
        ...

class AddOperationAwardComposer(PersonalMissionsAwardComposer):
    _eventsCache: Any
    def __init__(self):
        ...
    def getFormattedBonuses(self, operation, size=..., gap=0):
        ...
    def _getBonuses(self, operation):
        ...

class TooltipOperationAwardComposer(MainOperationAwardComposer):
    _BONUSES_ORDER: tuple
    def __init__(self, packer=None):
        ...
    def _bonusSortKey(self, bonus):
        ...
    def _packBonuses(self, preformattedBonuses, size, gap=0, isObtained=False, obtainedImage='', obtainedImageOffset=0):
        ...
    def _getBonuses(self, operation):
        ...
    def _getPreformattedTankwomanBonus(self, operation):
        ...

class TooltipPostponedOperationAwardComposer(TooltipOperationAwardComposer):
    POSTPONE_PERSONAL_MISSION_TOKEN = 'pm2_t%s_early_access'
    def _getBonuses(self, operation):
        ...
    def _getPreformattedTankwomanBonus(self, operation):
        ...

class MarathonAwardComposer(CurtailingAwardsComposer):
    AWARDS_PER_LINE_COUNT = 3
    def _packBonuses(self, preformattedBonuses, size):
        ...

class AnniversaryAwardComposer(CurtailingAwardsComposer):
    def getFormattedBonuses(self, bonuses, size=...):
        ...
    def _doCustomSort(self, bonuses):
        ...

class EpicCurtailingAwardsComposer(CurtailingAwardsComposer):
    @classmethod
    def _getShortBonusesData(cls, preformattedBonuses, size=...):
        ...

class RoyaleCurtailingAwardsComposer(CurtailingAwardsComposer):
    itemsCache: Any
    @classmethod
    def _getShortBonusesData(cls, preformattedBonuses, size=...):
        ...

def formatShortData(bonus, size):
    ...
def getBonusesWithModifyTokens(bonuses, freeTokenName, addTokensCount, hasPawned, additionalCtx=None):
    ...
def _getTankwomansCountInOperation(operation):
    ...
