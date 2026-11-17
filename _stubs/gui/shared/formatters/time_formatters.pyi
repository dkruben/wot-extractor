# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/formatters/time_formatters.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import math as math
import time as time
from gui.Scaleform.locale.MENU import MENU as MENU
from gui.impl import backport as backport
from helpers import i18n as i18n, time_utils as time_utils
from rent_common import SeasonRentDuration as SeasonRentDuration
from constants import GameSeasonType as GameSeasonType
from season_common import getDateFromSeasonID as getDateFromSeasonID
_SEASON_TYPE_KEY: dict

class RentDurationKeys(object):
    SEASON = 'season'
    CYCLE = 'cycle'
    CYCLES = 'cycles'
    TIME = 'time'
    DAYS = 'days'
    HOURS = 'hours'
    MINUTES = 'minutes'
    BATTLES = 'battles'
    WINS = 'wins'

class RentLeftFormatter(object):
    __rentInfo: Any
    __isIGR: Any
    __localizationRootKey: Any
    def __init__(self, rentInfo, isIGR=False):
        ...
    def getRentLeftStr(self, localization=None, timeStyle=None, ctx=None, formatter=None, strForSpecialTimeFormat=''):
        ...
    def getRentTimeLeftStr(self, localization=None, timeStyle=None, ctx=None, formatter=None):
        ...
    def getUntilTimeLeftStr(self, finishTime, localization=''):
        ...
    def getRentBattlesLeftStr(self, localization=None, formatter=None):
        ...
    def getRentWinsLeftStr(self, localization=None, formatter=None):
        ...
    def getRentSeasonLeftStr(self, rentData, localization=None, formatter=None, timeStyle=None, ctx=None):
        ...
    def getRentRankedSeasonLeftStr(self, rentData, timeStyle):
        ...

def defaultFormatter(key, countType, count, ctx=None):
    ...
def formatDate(dateFormat, timestamp):
    ...
def formatTime(timeLeft, divisor, timeStyle=None):
    ...
def getTimeLeftInfo(timeLeft, timeStyle=None):
    ...
def getTimeLeftStr(localization, timeLeft, timeStyle=None, ctx=None, formatter=None):
    ...
def getDueDateOrTimeStr(finishTime, localization='', isShortDateFormat=False):
    ...
def getTimeDurationStr(seconds, useRoundUp=False):
    ...
def getTillTimeByResource(seconds, resource, useMinutesRoundUp=False, removeLeadingZeros=False, useHoursRoundUp=False):
    ...
