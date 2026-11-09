# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/time_tracking.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import sys as sys
from time import time as time
from functools import wraps as wraps
from constants import SERVER_TICK_LENGTH as SERVER_TICK_LENGTH, IS_BASEAPP as IS_BASEAPP, IS_CELLAPP as IS_CELLAPP
from debug_utils import LOG_WARNING as LOG_WARNING
from math_common import round_py2_style as round_py2_style
DEFAULT_TIME_LIMIT = 0.02
DEFAULT_TICK_LENGTH = SERVER_TICK_LENGTH

class TimeTracker(object):
    context: Any
    timeLimit: Any
    tickLength: Any
    startTime: Any
    checkpoints: Any
    def __init__(self, context=None, timeLimit=..., tickLength=...):
        ...
    def __enter__(self):
        ...
    def __exit__(self, exc_type, exc_val, exc_tb):
        ...
    def checkpoint(self, name):
        ...

def incrTickOverspends():
    ...
def LOG_TIME_WARNING(spentTime, context=None, tickLength=..., *args):
    ...
def timetracked(func=None, context=None, timeLimit=..., tickLength=...):
    ...
def logTimeTracker(func):
    ...
