# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/formatters/date_time.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import time as time
import re as re
from gui.impl.gen import R as R
from gui.impl import backport as backport
from constants import CURRENT_REALM as CURRENT_REALM
from soft_exception import SoftException as SoftException
from gui.impl.gen.view_models.constants.date_time_formats import DateTimeFormatsEnum as DateTimeFormatsEnum
_R_MONTHS = R.strings.menu.dateTime.months
_R_WEEKDAYS = R.strings.menu.dateTime.weekDays
_R_REG_DATE = R.strings.datetime_formats.regionalDate
_FORMAT_REXP: Any
_FORMAT_ARGS_DICT: dict
_DATE_TIME_FMT_MAP: dict

class _MonthFormatKeys(object):
    FULL = '%B'
    FULL_D = '%Bd'
    FULL_S = '%Bs'
    ABBR = '%b'
    ABBR_D = '%bd'
    ABBR_S = '%bs'

class _WeekdayFormatKeys(object):
    FULL = '%A'
    ABBR = '%a'

class _TimeFormatKeys(object):
    SHORT = '%TIME'
    FULL = '%FULL_TIME'
    ALL: tuple

def __getRealmLocale(path):
    ...
def _getRegionalTime(ts, isShort):
    ...
def _fallbackArgHandler(specifier, ts):
    ...
def _expandTimeFmtArguments(rePattern, fmtStr, customArgsDict, ts):
    ...
def formatTimeString(fmtStr, ts):
    ...
def getFormattedDateTime(timestamp, formatString, isConvertedToLocal=True):
    ...
def getRegionalDateTime(timestamp, dateTimeFormat, isConvertedToLocal=True):
    ...
