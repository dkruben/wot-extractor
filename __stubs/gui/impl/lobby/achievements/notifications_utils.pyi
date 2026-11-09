# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/achievements/notifications_utils.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import weakref as weakref
from abc import ABCMeta as ABCMeta, abstractmethod as abstractmethod
from constants import AchievementsLayoutStates as AchievementsLayoutStates
from achievements20.WTRStageChecker import WTRStageChecker as WTRStageChecker
from gui.impl.lobby.achievements.profile_utils import isSummaryEnabled as isSummaryEnabled, isWTREnabled as isWTREnabled, getStagesOfWTR as getStagesOfWTR, getNormalizedValue as getNormalizedValue, isEditingEnabled as isEditingEnabled, isLayoutEnabled as isLayoutEnabled
from helpers import dependency as dependency
from skeletons.gui.game_control import IAchievements20Controller as IAchievements20Controller
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache
_logger: Any

class FLAG_STATUS(object):
    UNSET = 0
    SET = 1
    VISITED = 2

class NotificationsRuleProcessor(object):
    __slot__: tuple
    __rules: Any
    __ctrl: Any
    def __init__(self, ctrl):
        ...
    def fini(self):
        ...
    def start(self):
        ...
    def stop(self):
        ...
    def process(self):
        ...

class _NotificationRule(object, metaclass=ABCMeta):
    _lobbyContext: Any
    _itemsCache: Any
    _achievementsCtrl: Any
    def __init__(self, achievementsCtrl):
        ...
    @abstractmethod
    def prereq(self):
        ...
    @abstractmethod
    def req(self):
        ...
    @abstractmethod
    def do(self):
        ...

class _NotificationNewSummaryPage(_NotificationRule):
    def prereq(self):
        ...
    def req(self):
        ...
    def do(self):
        ...

class _NotificationRatingEnabled(_NotificationRule):
    def prereq(self):
        ...
    def req(self):
        ...
    def do(self):
        ...

class _NotificationAchievementEditingEnabled(_NotificationRule):
    def prereq(self):
        ...
    def req(self):
        ...
    def do(self):
        ...

class _NotificationNewMedal(_NotificationRule):
    def prereq(self):
        ...
    def req(self):
        ...
    def do(self):
        ...

class _NotificationChangeRank(_NotificationRule):
    def prereq(self):
        ...
    def req(self):
        ...
    def do(self):
        ...

def buildRules(ctrl):
    ...
