# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/uilogging/base/logger.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import uuid as uuid
import typing as typing
import logging as logging
from functools import wraps as wraps
import BigWorld as BigWorld
from helpers import dependency as dependency
from skeletons.ui_logging import IUILoggingCore as IUILoggingCore
from uilogging.constants import LogLevels as LogLevels, DEFAULT_LOGGER_NAME as DEFAULT_LOGGER_NAME
from wotdecorators import noexcept as noexcept
from uilogging.types import FeatureType as FeatureType, GroupType as GroupType, ActionType as ActionType, LogLevelType as LogLevelType, PartnerIdType as PartnerIdType, TimeLimitType as TimeLimitType, ItemType as ItemType, ItemStateType as ItemStateType, ParentScreenType as ParentScreenType, InfoType as InfoType, SourceItemType as SourceItemType, DestinationItemType as DestinationItemType, TransitionMethodType as TransitionMethodType
_logger: Any
LOGGERS_TYPING: Any

class _BaseLogger(object):
    __slots__: tuple
    _core: Any
    _feature: Any
    _group: Any
    _logOnceSet: Any
    _timedActions: Any
    _suspendedActions: Any
    def __init__(self, feature, group):
        ...
    def __str__(self):
        ...
    # decorador original: @noexcept
    def ensureSession(self):
        ...
    # decorador original: @noexcept
    def reset(self):
        ...
    @property
    def disabled(self):
        ...
    # decorador original: @noexcept
    def suspendAction(self, action):
        ...
    # decorador original: @noexcept
    def resumeAction(self, action):
        ...
    # decorador original: @noexcept
    # decorador original: @ifUILoggingEnabled(...)
    def startAction(self, action):
        ...
    # decorador original: @noexcept
    # decorador original: @ifUILoggingEnabled(...)
    def _log(self, action, loglevel=..., **params):
        ...
    # decorador original: @noexcept
    # decorador original: @ifUILoggingEnabled(...)
    def _logImmediately(self, action, loglevel=..., **params):
        ...
    # decorador original: @noexcept
    # decorador original: @ifUILoggingEnabled(...)
    def _logOnce(self, action, loglevel=..., **params):
        ...
    # decorador original: @noexcept
    def _stopAction(self, action, loglevel=..., timeLimit=0.0, **params):
        ...

class MetricsLogger(_BaseLogger):
    __slots__: tuple
    def __init__(self, feature):
        ...
    def log(self, action, item, parentScreen=None, itemState=None, info=None, partnerID=None, loglevel=...):
        ...
    def logOnce(self, action, item, parentScreen=None, itemState=None, info=None, partnerID=None, loglevel=...):
        ...
    def stopAction(self, action, item, parentScreen=None, itemState=None, info=None, partnerID=None, loglevel=..., timeLimit=0.0):
        ...

class FlowLogger(_BaseLogger):
    __slots__: tuple
    def __init__(self, feature):
        ...
    def log(self, action, sourceItem, destinationItem, transitionMethod, partnerID=None, loglevel=...):
        ...
    def logOnce(self, action, sourceItem, destinationItem, transitionMethod, partnerID=None, loglevel=...):
        ...
    def stopAction(self, action, sourceItem, destinationItem, transitionMethod, partnerID=None, loglevel=..., timeLimit=0.0):
        ...

def createPartnerID():
    ...
def ifUILoggingEnabled(result=None):
    ...
