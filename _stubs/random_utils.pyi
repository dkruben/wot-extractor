# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/random_utils.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import itertools as itertools
import random as random
from bisect import bisect as bisect
from copy import deepcopy as deepcopy
from past.builtins import xrange as xrange
import typing as typing

class wchoices(object):
    welist: Any
    def __init__(self, elist, wlist=None):
        ...
    def nseq(self, count=1):
        ...
    def ncounts(self, count):
        ...
    def __iter__(self):
        ...

def getValueWithDeviationInPercent(value, deviation):
    ...
def weighted_choice(seq, weights, customRandomModule=None):
    ...
