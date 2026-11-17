# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/helpers/func_utils.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from functools import partial as partial, wraps as wraps
from past.builtins import intern as intern
from time import sleep as sleep, time as time
import BigWorld as BigWorld
from constants import IS_DEVELOPMENT as IS_DEVELOPMENT
from debug_utils import LOG_DEBUG as LOG_DEBUG
FLASH_IMG_PREFIX = 'img://'

def callback(delay, obj, methodName, *args):
    ...
def callMethod(obj, methodName, *args):
    ...
def debugDelay(timeLag):
    ...
def logFunc(func):
    ...
def freeze(seconds, nextFrame=True):
    ...
def oncePerPeriod(period):
    ...
def replaceImgPrefix(path):
    ...
def isDeveloperFunc(func):
    ...
