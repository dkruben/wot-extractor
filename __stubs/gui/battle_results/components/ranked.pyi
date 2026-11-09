# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_results/components/ranked.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from collections import namedtuple as namedtuple
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import ENABLE_RANKED_ANIMATIONS as ENABLE_RANKED_ANIMATIONS
from gui.Scaleform.genConsts.RANKEDBATTLES_ALIASES import RANKEDBATTLES_ALIASES as RANKEDBATTLES_ALIASES
from gui.battle_results.components import base as base
from gui.battle_results.reusable import sort_keys as sort_keys
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.ranked_battles.ranked_models import RankChangeStates as _RCS
from gui.ranked_battles.ranked_helpers import getBonusBattlesIncome as getBonusBattlesIncome
from gui.shared.formatters import text_styles as text_styles
from helpers import dependency as dependency
from skeletons.gui.game_control import IRankedBattlesController as IRankedBattlesController
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from shared_utils import CONST_CONTAINER as CONST_CONTAINER
TitleAndDescription: Any
Shield: Any
IconsAndShield: Any

class MiniSteps(CONST_CONTAINER):
    STEPS_EARNED_BONUS = 4
    STEP_EARNED_BONUS = 3
    STEPS_EARNED = 2
    STEP_EARNED = 1
    STEP_NOT_CHANGED = 0
    STEP_LOST = -1

class RankedInfoHelper(object):
    rankedController: Any
    __slots__: tuple
    _RESOURCE_MAP: dict
    _reusable: Any
    def __init__(self, reusable):
        ...
    def getRankChangeStatus(self):
        ...

class RankedResultsInfoHelper(RankedInfoHelper):
    __slots__: tuple
    _CHANGE_TO_ALIAS_STATE: dict
    _STATUS_LABEL_MAP: dict
    def makeState(self):
        ...
    def makeStatusLabel(self):
        ...
    def getListsData(self, isLoser):
        ...
    def getPlayersNumber(self):
        ...
    def getPlayerStandoff(self, team, position, stepChanges, updatedStepChanges):
        ...
    def getStandoff(self, xp, xpToCompare, position, isLoser, isTop, lastStandoffInfo=None):
        ...
    @classmethod
    def __getStepTypeByDiff(cls, stepDiff):
        ...
    @classmethod
    def __getStepInfo(cls, stepElement, rankChanges):
        ...
    @classmethod
    def __getNextStandoff(cls, standoff, diff):
        ...

class RankedChangesInfoHelper(RankedInfoHelper):
    settingsCore: Any
    __slots__: tuple
    _STEPS_ICONS: dict
    _MINI_STEPS_ICONS: dict
    _STATE_TO_SUBTASK: dict
    _TITLE_LABEL_MAP: dict
    def makeTitleAndDescription(self, allyVehicles):
        ...
    def makeIcons(self):
        ...
    def makeSubTaskState(self):
        ...
    def _getDescriptionIcon(self, state, stepChanges, updatedStepChanges):
        ...
    def _getLoserBounds(self, position):
        ...
    def _getPlayerPosition(self, allyVehicles):
        ...
    def _getWinnerBounds(self, position):
        ...
    def __getRankIcon(self, rankID):
        ...

class RankedResultsShowWidgetAnimation(base.StatsItem):
    rankedController: Any
    def _convert(self, value, reusable):
        ...

class RankedResultsStatusBlock(base.StatsItem):
    def _convert(self, value, reusable):
        ...

class RankedResultsStateBlock(base.StatsItem):
    def _convert(self, value, reusable):
        ...

class RankedResultsEnableAnimation(base.StatsItem):
    def _convert(self, value, reusable):
        ...

class RankChangesBlock(base.StatsBlock):
    __slots__: tuple
    state: Any
    linkage: Any
    title: Any
    description: Any
    descriptionIcon: Any
    icon: Any
    shieldCount: Any
    shieldIcon: Any
    plateIcon: Any
    def __init__(self, meta=None, field='', *path):
        ...
    def setRecord(self, result, reusable):
        ...

def _getTopsLoseIcon(topNumber):
    ...
def _getTopsTopIcon(topNumber):
    ...
def _getTopsNotEffectiveIcon(topNumber):
    ...
