# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/dog_tags_common/number_formatter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import re as re
from collections import defaultdict as defaultdict
from math import floor as floor
import typing as typing
from dog_tags_common.config.common import ComponentNumberType as ComponentNumberType
_TRAILING_ZEROES_RE: Any
_millionDivider: Any
_replacements: dict

def formatComponentValue(locale, value, numberType, specialReplacements=True):
    ...
def formatPercentage(value):
    ...
def formatNumber(locale, value, regionalPrefix=True):
    ...
def customRound(value, ndecimals=0):
    ...
def _formatThousands(value, roundStrategy=...):
    ...
def _formatMillions(locale, value):
    ...
