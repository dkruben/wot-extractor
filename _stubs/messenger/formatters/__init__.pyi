# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/formatters/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import re as re
from collections import namedtuple as namedtuple
from past.builtins import unicode as unicode
from time import gmtime as gmtime, time as getTime
from constants import NC_CONTEXT_ITEM_TYPE as NC_CONTEXT_ITEM_TYPE
from gui.impl import backport as backport
from helpers import time_utils as time_utils
from messenger import g_settings as g_settings
_logger: Any
SysMsgExtraData: Any
_SMILEY_TRIGGERS_RE: Any
_SMILEY_BREAK = "\\1<font size='1'>&nbsp;</font>"

class TimeFormatter(object):
    _messageDateTimeFormat: dict
    @classmethod
    def getMessageTimeFormat(cls, time):
        ...
    @classmethod
    def getShortDateFormat(cls, time):
        ...
    @classmethod
    def getLongTimeFormat(cls, time):
        ...
    @classmethod
    def getShortTimeFormat(cls, time):
        ...
    @classmethod
    def getLongDatetimeFormat(cls, time):
        ...
    @classmethod
    def getShortTimeDateFormat(cls, time):
        ...
    @classmethod
    def getShortDatetimeFormat(cls, time):
        ...
    @classmethod
    def getActualMsgTimeStr(cls, timestamp):
        ...
    @classmethod
    def getMessageEmptyFormatU(cls, _):
        ...
    @classmethod
    def getMessageShortDateFormat(cls, time):
        ...
    @classmethod
    def getMessageLongTimeFormat(cls, time):
        ...
    @classmethod
    def getMessageLongDatetimeFormat(cls, time):
        ...

class NCContextItemFormatter(object):
    _formats: dict
    @classmethod
    def getItemFormat(cls, itemType, itemValue):
        ...
    @classmethod
    def getGoldFormat(cls, value):
        ...
    @classmethod
    def getIntegralFormat(cls, value):
        ...
    @classmethod
    def getFractionalFormat(cls, value):
        ...
    @classmethod
    def getNiceNumberFormat(cls, value):
        ...
    @classmethod
    def getShortTimeFormat(cls, value):
        ...
    @classmethod
    def getLongTimeFormat(cls, value):
        ...
    @classmethod
    def getShortDateFormat(cls, value):
        ...
    @classmethod
    def getLongDateFormat(cls, value):
        ...
    @classmethod
    def getDateTimeFormat(cls, value):
        ...
    @classmethod
    def getStringFormat(cls, value):
        ...
    @classmethod
    def _makeLocalTimeString(cls, value, formatter):
        ...

def escapeSmileys(text):
    ...
