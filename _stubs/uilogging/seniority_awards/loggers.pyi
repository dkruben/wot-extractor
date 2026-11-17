# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/uilogging/seniority_awards/loggers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from typing import TYPE_CHECKING as TYPE_CHECKING
from uilogging.base.logger import MetricsLogger as MetricsLogger
from uilogging.constants import LogLevels as LogLevels
from uilogging.seniority_awards.constants import SeniorityAwardsLogActions as SeniorityAwardsLogActions, SeniorityAwardsLogKeys as SeniorityAwardsLogKeys, SeniorityAwardsLogButtons as SeniorityAwardsLogButtons, SeniorityAwardsLogSpaces as SeniorityAwardsLogSpaces, SeniorityAwardsFeatures as SeniorityAwardsFeatures
from wotdecorators import noexcept as noexcept
from uilogging.types import ParentScreenType as ParentScreenType
_logger: Any

class SeniorityAwardsMetricsLogger(MetricsLogger):
    __slots__: tuple
    def __init__(self):
        ...

class VehicleSelectionErrorNotificationsLogger(MetricsLogger):
    __slots__: tuple
    def __init__(self):
        ...
    # decorador original: @noexcept
    def handleTimeoutError(self):
        ...
    # decorador original: @noexcept
    def handleMultipleTokensError(self):
        ...

class VehicleSelectionNotificationLogger(SeniorityAwardsMetricsLogger):
    __slots__: tuple
    # decorador original: @noexcept
    def handleClickAction(self):
        ...
    # decorador original: @noexcept
    def handleDisplayedAction(self):
        ...

class RewardNotificationLogger(SeniorityAwardsMetricsLogger):
    __slots__: tuple
    # decorador original: @noexcept
    def handleClickAction(self, displaySpace):
        ...
    # decorador original: @noexcept
    def handleDisplayedAction(self, parentScreen, limitedUICompleted, isNeedBullet):
        ...

class CoinsNotificationLogger(SeniorityAwardsMetricsLogger):
    __slots__: tuple
    # decorador original: @noexcept
    def handleClickAction(self, displaySpace):
        ...
    # decorador original: @noexcept
    def handleDisplayedAction(self, parentScreen):
        ...
