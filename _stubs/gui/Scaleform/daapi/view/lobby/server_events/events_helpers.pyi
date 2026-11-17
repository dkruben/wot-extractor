# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/server_events/events_helpers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import operator as operator
from collections import defaultdict as defaultdict, namedtuple as namedtuple
from typing import TYPE_CHECKING as TYPE_CHECKING
from future.utils import viewitems as viewitems, viewvalues as viewvalues
from gui.Scaleform.daapi.view.lobby.customization.progression_helpers import getC11n2dProgressionLinkBtnParams as getC11n2dProgressionLinkBtnParams
from gui.Scaleform.daapi.view.lobby.server_events.token_converter_helper import getBonusDataFromOneOfBonuses as getBonusDataFromOneOfBonuses, convertTokensInBonusData as convertTokensInBonusData
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
import constants as constants
from battle_pass_common import BattlePassConsts as BattlePassConsts, BATTLE_PASS_RANDOM_QUEST_ID_PREFIX as BATTLE_PASS_RANDOM_QUEST_ID_PREFIX, NON_CHAPTER_ID as NON_CHAPTER_ID, isPostProgressionChapter as isPostProgressionChapter, getPostProgressionLevel as getPostProgressionLevel
from constants import EVENT_TYPE as EVENT_TYPE
from gui.server_events.bonuses import BattleTokensBonus as BattleTokensBonus
from gui.server_events.events_constants import BATTLE_MATTERS_QUEST_ID as BATTLE_MATTERS_QUEST_ID
from gui import GUI_NATIONS as GUI_NATIONS, makeHtmlString as makeHtmlString
from gui.Scaleform import getNationsFilterAssetPath as getNationsFilterAssetPath
from gui.Scaleform.daapi.view.lobby.event_boards.formaters import getNationText as getNationText
from gui.Scaleform.daapi.view.lobby.server_events.awards_formatters import OldStyleBonusesFormatter as OldStyleBonusesFormatter
from gui.Scaleform.genConsts.PERSONAL_MISSIONS_ALIASES import PERSONAL_MISSIONS_ALIASES as PERSONAL_MISSIONS_ALIASES
from gui.Scaleform.genConsts.QUESTS_ALIASES import QUESTS_ALIASES as QUESTS_ALIASES
from gui.Scaleform.locale.PERSONAL_MISSIONS import PERSONAL_MISSIONS as PERSONAL_MISSIONS
from gui.Scaleform.locale.QUESTS import QUESTS as QUESTS
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS as TOOLTIPS
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.server_events import conditions as conditions, formatters as formatters, settings as quest_settings
from gui.server_events.events_helpers import EventInfoModel as EventInfoModel, MISSIONS_STATES as MISSIONS_STATES, QuestInfoModel as QuestInfoModel, isDailyQuest as isDailyQuest, getDataByC11nQuest as getDataByC11nQuest
from gui.server_events.personal_progress.formatters import PostBattleConditionsFormatter as PostBattleConditionsFormatter
from gui.shared.formatters import icons as icons, text_styles as text_styles
from helpers import dependency as dependency, i18n as i18n, int2roman as int2roman, time_utils as time_utils
from helpers.i18n import makeString as _ms
from math_common import round_py2_style_int as round_py2_style_int
from nations import ALLIANCE_TO_NATIONS as ALLIANCE_TO_NATIONS
from personal_missions import PM_BRANCH as PM_BRANCH
from quest_xml_source import MAX_BONUS_LIMIT as MAX_BONUS_LIMIT
from shared_utils import first as first
from skeletons.gui.customization import ICustomizationService as ICustomizationService
from skeletons.gui.game_control import IBattlePassController as IBattlePassController
from skeletons.gui.server_events import IEventsCache as IEventsCache
from skeletons.gui.shared import IItemsCache as IItemsCache
from typing import Dict as Dict, Iterable as Iterable, Union as Union
from gui.server_events.bonuses import BattlePassStyleProgressTokenBonus as BattlePassStyleProgressTokenBonus, TokensBonus as TokensBonus
from gui.server_events.event_items import Quest as Quest
FINISH_TIME_LEFT_TO_SHOW = time_utils.ONE_DAY
START_TIME_LIMIT: Any
_AWARDS_PER_PAGE = 3
_ChapterProgress: Any
_questBranchToTabMap: dict

class BattlePassProgress(object):
    __battlePassController: Any
    __eventsCache: Any
    __BATTLE_PASS_POINTS = 'battlePassPoints'
    __arenaBonusType: Any
    __topPoints: Any
    __topExternalPoints: Any
    __pointsAux: Any
    __hasBattlePass: Any
    __questsProgress: Any
    __battlePassComplete: Any
    __availablePoints: Any
    __questPoints: Any
    __bonusCapPoints: Any
    __chaptersInfo: Any
    __previousChapterID: Any
    __currentChapterID: Any
    __chaptersProgress: Any
    def __init__(self, arenaBonusType, *args, **kwargs):
        ...
    @property
    def previousChapterID(self):
        ...
    @property
    def currentChapterID(self):
        ...
    @property
    def isApplied(self):
        ...
    @property
    def hasBattlePass(self):
        ...
    @property
    def battlePassComplete(self):
        ...
    @property
    def availablePoints(self):
        ...
    @property
    def bpTopPoints(self):
        ...
    @property
    def bpTopExternalPoints(self):
        ...
    @property
    def bpTopExternalPointsTotalAmount(self):
        ...
    @property
    def pointsAux(self):
        ...
    @property
    def questPoints(self):
        ...
    @property
    def bonusCapPoints(self):
        ...
    def getCurrentLevelPoints(self, chapterID):
        ...
    def getMaxLevelPoints(self, chapterID):
        ...
    def getCurrentLevel(self, chapterID):
        ...
    def getPreviousLevel(self, chapterID):
        ...
    def getPointsDiff(self, chapterID):
        ...
    def getLevelAwards(self, chapterID, level):
        ...
    def getLevelAwardsByType(self, chapterID, level, rewardType):
        ...
    def hasProgress(self, chapterID):
        ...
    def isLevelReached(self, chapterID):
        ...
    def isLevelMax(self, chapterID):
        ...
    def isDone(self, chapterID):
        ...
    def __initExtendedData(self):
        ...
    def __getRewardType(self, chapterID):
        ...
    @staticmethod
    def __isQuestCompleted(_, previousProgress, currentProgress):
        ...

class EventPostBattleInfo(EventInfoModel):
    def getInfo(self, svrEvents, pCur=None, pPrev=None, noProgressInfo=False):
        ...
    def getPostBattleInfo(self, svrEvents, pCur, pPrev, isProgressReset, isCompleted, **kwargs):
        ...
    @classmethod
    def _getEventsByIDs(cls, ids, svrEvents):
        ...
    def _getBonusCount(self, pCur=None):
        ...
    def _getProgressValues(self, svrEvents=None, pCur=None, pPrev=None):
        ...
    def _getBonuses(self, svrEvents, pCur=None, bonuses=None, **kwargs):
        ...
    def _filterBonuses(self, bonuses):
        ...
    def _getProgresses(self, pCur, pPrev):
        ...

class QuestPostBattleInfo(EventPostBattleInfo, QuestInfoModel):
    PROGRESS_TOOLTIP_MAX_ITEMS = 4
    itemsCache: Any
    def _getStatus(self, pCur=None):
        ...
    def _getBonuses(self, svrEvents, pCur=None, bonuses=None, **kwargs):
        ...
    def _getBonusCount(self, pCur=None):
        ...
    def _getProgressValues(self, svrEvents=None, pCur=None, pPrev=None):
        ...

class PersonalMissionPostBattleInfo(EventPostBattleInfo):
    def getPostBattleInfo(self, svrEvents, pCur, pPrev, isProgressReset, isCompleted, **kwargs):
        ...
    def _getStatus(self, pCur=None, pmComplete=None, failed=None):
        ...

class _BattlePassRandomQuestPostBattleInfo(QuestPostBattleInfo):
    def _filterBonuses(self, bonuses):
        ...

class MotiveQuestPostBattleInfo(QuestPostBattleInfo):
    def getPostBattleInfo(self, svrEvents, pCur, pPrev, isProgressReset, isCompleted, **kwargs):
        ...

class _BattleMattersQuestInfo(QuestPostBattleInfo):
    def getInfo(self, svrEvents, pCur=None, pPrev=None, noProgressInfo=False):
        ...
    def _getProgresses(self, pCur, pPrev):
        ...

class Progression2dStyleFormater(object):
    c11nService: Any
    @classmethod
    def getProgress(cls, event, pCur, pPrev, isCompleted):
        ...
    @classmethod
    def getProgressRate(cls, event, pCur, pPrev, isCompleted):
        ...
    @classmethod
    def getTitle(cls, style):
        ...
    @classmethod
    def getStatus(cls, isComplete=None):
        ...

def _getEventInfoData(event):
    ...
def getEventPostBattleInfo(event, svrEvents=None, pCur=None, pPrev=None, isProgressReset=False, isCompleted=False, **kwargs):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def get2dProgressionStylePostBattleInfo(styleID, quests, c11nService=None):
    ...
def getNationsForChain(operation, chainID):
    ...
def getChainVehRequirements(operation, chainID, useIcons=False):
    ...
def getChainVehTypeAndLevelRestrictions(operation, chainID):
    ...
