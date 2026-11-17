# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_results/components/progress.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import operator as operator
from collections import namedtuple as namedtuple
from copy import deepcopy as deepcopy
from itertools import chain as chain
import typing as typing
import personal_missions as pm
from battle_pass_common import BattlePassConsts as BattlePassConsts, isPostProgressionChapter as isPostProgressionChapter
from constants import EVENT_TYPE as EVENT_TYPE
from gui.Scaleform.daapi.view.lobby.customization.progression_helpers import getC11nProgressionLinkBtnParams as getC11nProgressionLinkBtnParams, parseEventID as parseEventID, getC11n2dProgressionLinkBtnParams as getC11n2dProgressionLinkBtnParams, getProgressiveCustomizationProgress as getProgressiveCustomizationProgress
from gui.Scaleform.daapi.view.lobby.server_events.awards_formatters import BattlePassTextBonusesPacker as BattlePassTextBonusesPacker
from gui.Scaleform.daapi.view.lobby.server_events.events_helpers import getEventPostBattleInfo as getEventPostBattleInfo, get2dProgressionStylePostBattleInfo as get2dProgressionStylePostBattleInfo
from gui.Scaleform.genConsts.MISSIONS_STATES import MISSIONS_STATES as MISSIONS_STATES
from gui.Scaleform.genConsts.PROGRESSIVEREWARD_CONSTANTS import PROGRESSIVEREWARD_CONSTANTS as prConst
from gui.Scaleform.genConsts.QUESTS_ALIASES import QUESTS_ALIASES as QUESTS_ALIASES
from gui.Scaleform.locale.BATTLE_RESULTS import BATTLE_RESULTS as BATTLE_RESULTS
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS as TOOLTIPS
from gui.battle_results.components import base as base
from gui.battle_results.progress.progress_helpers import getDogTagsProgress as getDogTagsProgress, getPrestigeProgress as getPrestigeProgress, isQuestCompleted as isQuestCompleted, packQuestProgressData as packQuestProgressData, PrestigeProgress as PrestigeProgress
from gui.battle_results.progress.research import MIN_BATTLES_TO_SHOW_PROGRESS as MIN_BATTLES_TO_SHOW_PROGRESS, VehicleProgressHelper as VehicleProgressHelper
from gui.battle_results.progress.progress_filters import battleMattersProgressFilter as battleMattersProgressFilter
from gui.battle_results.settings import PROGRESS_ACTION as PROGRESS_ACTION
from gui.dog_tag_composer import dogTagComposer as dogTagComposer
from gui.impl import backport as backport
from gui.impl.auxiliary.rewards_helper import getProgressiveRewardVO as getProgressiveRewardVO
from gui.impl.gen import R as R
from gui.server_events import formatters as formatters
from gui.server_events.awards_formatters import QuestsBonusComposer as QuestsBonusComposer
from gui.server_events.events_helpers import getDataByC11nQuest as getDataByC11nQuest, isC11nQuest as isC11nQuest
from gui.shared.formatters import getItemUnlockPricesVO as getItemUnlockPricesVO, text_styles as text_styles
from gui.shared.gui_items import Tankman as Tankman
from gui.shared.gui_items.Vehicle import getLevelIconPath as getLevelIconPath
from gui.shared.gui_items.crew_skin import localizedFullName as localizedFullName
from helpers import dependency as dependency
from helpers.i18n import makeString as _ms
from skeletons.gui.game_control import IBattlePassController as IBattlePassController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.server_events import IEventsCache as IEventsCache
from skeletons.gui.shared import IItemsCache as IItemsCache
from typing import Dict as Dict, Tuple as Tuple
from gui.battle_results.reusable import _ReusableInfo as _ReusableInfo
from gui.Scaleform.daapi.view.lobby.server_events.events_helpers import BattlePassProgress as BattlePassProgress
_POST_BATTLE_RES = R.strings.battle_pass.reward.postBattle
_logger: Any
PMComplete: Any

class VehicleProgressBlock(base.StatsBlock):
    _itemsCache: Any
    __slots__: tuple
    def getVO(self):
        ...
    def setRecord(self, result, reusable):
        ...

class BattlePassProgressBlock(base.StatsBlock):
    __battlePass: Any
    def setRecord(self, result, reusable):
        ...
    @classmethod
    def __formatBattlePassProgress(cls, progress, level, chapter):
        ...
    @classmethod
    def __formatBattlePassPoints(cls, progress):
        ...
    @staticmethod
    def __makeProgressAwards(progress, chapter, level):
        ...
    @classmethod
    def __makeProgressQuestInfo(cls, progress, chapterID, level):
        ...
    @classmethod
    def __makePointsInfo(cls, progress):
        ...
    @classmethod
    def __makeProgressList(cls, progress, chapter, level):
        ...
    @classmethod
    def __makePointsList(cls, progress):
        ...
    @staticmethod
    def __getPointsInfo(description, tooltip, points):
        ...
    @classmethod
    def __getChapterName(cls, chapterID):
        ...
    @staticmethod
    def _getDescription(progress):
        ...
    @staticmethod
    def _getProgressDiffTooltip(progress, chapterID):
        ...
    @staticmethod
    def __getMissionState(isDone):
        ...
    @staticmethod
    def __getProgressBarType(needShow):
        ...

class QuestsProgressBlock(base.StatsBlock):
    __eventsCache: Any
    __slots__: tuple
    def getVO(self):
        ...
    def setRecord(self, result, reusable):
        ...
    @staticmethod
    def __sortPersonalMissions(a, b):
        ...
    @staticmethod
    def __sortCommonQuestsFunc(aData, bData):
        ...

class DogTagsProgressBlock(base.StatsBlock):
    __slots__: tuple
    def setRecord(self, result, reusable):
        ...
    @classmethod
    def _formatDogTag(cls, dogTagProgress):
        ...
    @staticmethod
    def __getInfoTitle(dogTagProgress):
        ...
    @staticmethod
    def __getInfoDescription(dogTagProgress):
        ...

class ProgressiveRewardVO(base.StatsItem):
    eventsCache: Any
    lobbyContext: Any
    __slots__: tuple
    def _convert(self, record, reusable):
        ...

class ProgressiveCustomizationVO(base.DirectStatsItem):
    _itemsCache: Any
    __slots__: tuple
    def getVO(self):
        ...

class QuestProgressiveCustomizationVO(base.DirectStatsItem):
    _itemsCache: Any
    __slots__: tuple
    def getVO(self):
        ...

class PrestigeProgressVO(base.StatsItem):
    def _convert(self, result, reusable):
        ...
    @staticmethod
    def __createPrestigeVO(prestigeData):
        ...

def _makeTankmanDescription(roleName, fullName):
    ...
def _makeVehicleDescription(vehicle):
    ...
def _makeTankmanVO(tman, newSkillEarned, bonusSkillsAmount, avgBattles2NewSkill, skinItem):
    ...
def _makeUnlockModuleVO(item, unlockProps):
    ...
def _makeUnlockVehicleVO(item, unlockProps, avgBattlesTillUnlock):
    ...
