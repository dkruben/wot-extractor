# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/periodic_battles/models.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from functools import partial as partial
import typing as typing
from enum import Enum as Enum
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.Scaleform.genConsts.ALERTMESSAGE_CONSTANTS import ALERTMESSAGE_CONSTANTS as ALERTMESSAGE_CONSTANTS
from gui.shared.formatters import text_styles as text_styles
from gui.shared.utils.decorators import ReprInjector as ReprInjector
from gui.shared.utils.functions import makeTooltip as makeTooltip
from helpers import time_utils as time_utils
from shared_utils import collapseIntervals as collapseIntervals, findFirst as findFirst, first as first, CONST_CONTAINER as CONST_CONTAINER
from frameworks.wulf import PyResAccessor as PyResAccessor
from season_common import GameSeason as GameSeason, GameSeasonCycle as GameSeasonCycle
_logger: Any
PERIOD_TO_STANDALONE: dict

class PrimeTimeStatus(CONST_CONTAINER):
    NOT_SET = 1
    FROZEN = 2
    NOT_AVAILABLE = 3
    AVAILABLE = 4

class PeriodType(Enum):
    UNDEFINED = 'undefined'
    BEFORE_SEASON = 'beforeSeason'
    BETWEEN_SEASONS = 'betweenSeasons'
    AFTER_SEASON = 'afterSeason'
    BEFORE_CYCLE = 'beforeCycle'
    BETWEEN_CYCLES = 'betweenCycles'
    AFTER_CYCLE = 'afterCycle'
    AVAILABLE = 'available'
    FROZEN = 'frozen'
    NOT_AVAILABLE = 'notAvailable'
    ALL_NOT_AVAILABLE = 'allNotAvailable'
    STANDALONE_NOT_AVAILABLE = 'standaloneNotAvailable'
    NOT_AVAILABLE_END = 'notAvailableEnd'
    ALL_NOT_AVAILABLE_END = 'allNotAvailableEnd'
    STANDALONE_NOT_AVAILABLE_END = 'standaloneNotAvailableEnd'
    NOT_SET = 'notSet'
    ALL_NOT_SET = 'allNotSet'
    STANDALONE_NOT_SET = 'standaloneNotSet'

# decorador original: @ReprInjector.simple(...)
class PeriodBorder(object):
    __slots__: tuple
    _TECH_FIELD_FMT = '{techName}{fieldName}'
    userName: Any
    timestamp: Any
    techData: Any
    def __init__(self, userName, timestamp):
        ...
    def delta(self, now):
        ...
    def setTechName(self, techName):
        ...

# decorador original: @ReprInjector.simple(...)
class PeriodInfo(object):
    __slots__: tuple
    now: Any
    periodType: Any
    seasonBorderLeft: Any
    seasonBorderRight: Any
    cycleBorderLeft: Any
    cycleBorderRight: Any
    primeDelta: Any
    borders: Any
    def __init__(self, now, pType, seasonLeft=None, seasonRight=None, cycleLeft=None, cycleRight=None, primeDelta=0):
        ...
    @staticmethod
    def defaultDeltaFormatter(resRoot):
        ...
    @staticmethod
    def leftSeasonBorder(season):
        ...
    @staticmethod
    def rightSeasonBorder(season):
        ...
    @staticmethod
    def leftCycleBorder(cycle):
        ...
    @staticmethod
    def rightCycleBorder(cycle):
        ...
    def getVO(self, withBNames=False, withBDeltas=False, deltaFmt=None, timeFmt=None, dateFmt=None):
        ...
    def __addBorderTechName(self, border, techName):
        ...
    def __buildDeltas(self, result, deltaFormatter, bordersDeltas):
        ...
    def __buildDates(self, result, timeFormatter, dateFormatter):
        ...
    def __buildNames(self):
        ...

class PrimeTime(object):
    __peripheryID: Any
    __periods: Any
    def __init__(self, peripheryID, periods=None):
        ...
    def hasAnyPeriods(self):
        ...
    def getAvailability(self, forTime, cycleEnd):
        ...
    def getNextPeriodStart(self, fromTime, tillTime, includeBeginning=False):
        ...
    def getPeriodsActiveForTime(self, periodTime, preferPeriodBounds=False):
        ...
    def getPeriodsBetween(self, startTime, endTime, includeBeginning=True, includeEnd=True, preferPeriodBounds=False):
        ...

class AlertData(object):
    _RES_ROOT = None
    _PERIOD_TYPES_WITH_BUTTON: tuple
    _PERIOD_TYPES_PRIME_ALERT: tuple
    _RES_REASON_ROOT = None
    __slots__: tuple
    state: Any
    alertIcon: Any
    buttonIcon: Any
    buttonLabel: Any
    buttonVisible: Any
    buttonTooltip: Any
    statusText: Any
    additionalText: Any
    popoverAlias: Any
    bgVisible: Any
    shadowFilterVisible: Any
    tooltip: Any
    isSimpleTooltip: Any
    def __init__(self, state=..., alertIcon=None, buttonIcon='', buttonLabel='', buttonVisible=False, buttonTooltip=None, statusText='', additionalText='', popoverAlias=None, bgVisible=True, shadowFilterVisible=False, tooltip=None, isSimpleTooltip=False):
        ...
    @classmethod
    def construct(cls, periodInfo, serverShortName):
        ...
    @classmethod
    def constructForVehicle(cls, levelsStr, vehicleIsAvailableForBuy, vehicleIsAvailableForRestore, tooltip=None):
        ...
    @classmethod
    def packCallbacks(cls, onBtnClickCallback=None, onBlockClickCallback=None):
        ...
    def asDict(self):
        ...
    @classmethod
    def _getAlertLabel(cls, periodInfo, serverShortName):
        ...
    @classmethod
    def _getAlertLabelParams(cls, periodInfo):
        ...
    @classmethod
    def _getTooltip(cls, periodInfo):
        ...
