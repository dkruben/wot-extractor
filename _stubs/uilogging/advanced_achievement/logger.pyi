# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/uilogging/advanced_achievement/logger.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from typing import TYPE_CHECKING as TYPE_CHECKING
from advanced_achievements_client.getters import getAchievementByID as getAchievementByID
from helpers import dependency as dependency
from skeletons.gui.game_control import IAchievementsController as IAchievementsController
from uilogging.base.logger import MetricsLogger as MetricsLogger
from uilogging.advanced_achievement.logging_constants import FEATURE as FEATURE, AdvancedAchievementActions as AdvancedAchievementActions, AdvancedAchievementInfoKeys as AdvancedAchievementInfoKeys, AdvancedAchievementViewKey as AdvancedAchievementViewKey, AdvancedAchievementKeys as AdvancedAchievementKeys, AdvancedAchievementSubcategory as AdvancedAchievementSubcategory, AdvancedAchievementStates as AdvancedAchievementStates
from wotdecorators import noexcept as noexcept
from typing import Optional as Optional
from uilogging.types import ParentScreenType as ParentScreenType, ItemType as ItemType, InfoType as InfoType

class AdvancedAchievementMetricsLoger(MetricsLogger):
    __slots__: tuple
    def __init__(self):
        ...
    def logClick(self, item, parentScreen=None, info=None):
        ...
    def onViewOpen(self, item, parentScreen=None, info=None):
        ...

class AdvancedAchievementLogger(AdvancedAchievementMetricsLoger):
    __slots__: tuple
    __achievementsController: Any
    __SUBCATEGORY: dict
    _parentViewKey: Any
    def __init__(self, parentViewKey):
        ...
    def logClick(self, item, parentScreen=None, info=None):
        ...
    # decorador original: @noexcept
    def logCategoryClick(self, achievementID, category=None):
        ...
    # decorador original: @noexcept
    def logCardClick(self, achievementID, category):
        ...
    # decorador original: @noexcept
    def onViewOpen(self, item, parentScreen=None, info=None, isOtherPlayer=None):
        ...
    def __getStateInfo(self, progress):
        ...

class AdvancedAchievementEarningLogger(AdvancedAchievementMetricsLoger):
    # decorador original: @noexcept
    def logNotificationClick(self, item, isMultiple):
        ...
    def onViewOpen(self, item, parentScreen=None, info=None):
        ...

class AdvancedAchievementRewardLogger(AdvancedAchievementMetricsLoger):
    __slots__: tuple
    _parentViewKey: Any
    def __init__(self, parentViewKey):
        ...
    # decorador original: @noexcept
    def logRewardClick(self, item, count):
        ...
