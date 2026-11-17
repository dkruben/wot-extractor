# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/uilogging/dog_tags/logger.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from typing import TYPE_CHECKING as TYPE_CHECKING
from advanced_achievements_client.getters import getAchievementByID as getAchievementByID
from uilogging.base.logger import MetricsLogger as MetricsLogger
from uilogging.dog_tags.logging_constants import FEATURE as FEATURE, MIN_VIEW_TIME as MIN_VIEW_TIME, DogTagActions as DogTagActions, DogTagAchievementStates as DogTagAchievementStates, DogTagsViewKeys as DogTagsViewKeys
from wotdecorators import noexcept as noexcept
from typing import Optional as Optional
from uilogging.types import ParentScreenType as ParentScreenType, ItemType as ItemType, InfoType as InfoType

class DogTagsMetricsLoger(MetricsLogger):
    __slots__: tuple
    def __init__(self):
        ...
    # decorador original: @noexcept
    def logClick(self, item, parentScreen=None, info=None):
        ...
    # decorador original: @noexcept
    def onViewOpen(self, item, parentScreen=None, info=None):
        ...

class DogTagsViewLogger(DogTagsMetricsLoger):
    __slots__: tuple
    _parentScreen: Any
    def __init__(self, parentScreen):
        ...
    def logClick(self, item, parentScreen=None, info=None):
        ...
    def onViewOpen(self, item, parentScreen=None, info=None):
        ...

class AnimatedDogTagsViewLogger(DogTagsMetricsLoger):
    __slots__: tuple
    _parentScreen: Any
    def __init__(self, parentScreen):
        ...
    def logClick(self, item, parentScreen=None, info=None):
        ...
    # decorador original: @noexcept
    def logClickAchievement(self, item, achievementId, category):
        ...
    def onViewOpen(self, item, parentScreen=None, info=None):
        ...
    def __getStateInfo(self, progress):
        ...

class DogTagsTooltipLogger(DogTagsMetricsLoger):
    __slots__: tuple
    _currentViewKey: Any
    _parentViewKey: Any
    def __init__(self, currentViewKey, parentScreen):
        ...
    def viewOpened(self):
        ...
    def viewClosed(self, info=None):
        ...
    def reset(self):
        ...
