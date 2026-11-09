# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/dict2model/utils.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import re as re
import typing as typing
import copy as copy
import datetime as datetime
import functools as functools
from future.utils import string_types as string_types, binary_type as binary_type
from soft_exception import SoftException as SoftException
binaryType = binary_type
baseStringTypes: Any
_ISO8601_RE: Any
ZERO: Any
HOUR: Any
utc: Any

class UTC(datetime.tzinfo):
    zone = 'UTC'
    _utcoffset = ZERO
    _dst = ZERO
    _tzname = zone
    def fromutc(self, dt):
        ...
    def utcoffset(self, dt):
        ...
    def tzname(self, dt):
        ...
    def dst(self, dt):
        ...
    def localize(self, dt, is_dst=False):
        ...
    def normalize(self, dt, is_dst=False):
        ...
    def __repr__(self):
        ...
    def __str__(self):
        ...

def isoFormat(dt, localtime=False):
    ...
def fromIso(dateString):
    ...
def castToNumber(numType, value, exceptionClass=...):
    ...
def _mergeDicts(destination, source, deep=True):
    ...
def mergeDicts(destination, first, second=None, deep=True):
    ...
