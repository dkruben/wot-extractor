# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/utils/decorators.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import time as time
import adisp as adisp
import BigWorld as BigWorld
from debug_utils import LOG_DEBUG as LOG_DEBUG
from gui.Scaleform.Waiting import Waiting as Waiting
IS_DEVELOPMENT = True
trackFrame = _TrackFrameDisabled

class adisp_process(object):
    __currentMessage: Any
    __messages: Any
    __messages2Show: Any
    def __init__(self, *kargs):
        ...
    def __hideWaiting(self):
        ...
    def __nextWaiting(self):
        ...
    def __stepCallback(self, isStop):
        ...
    def __call__(self, func):
        ...

class _TrackFrameEnabled(object):
    __logID: Any
    def __init__(self, logID):
        ...
    def __call__(self, func):
        ...

class _TrackFrameDisabled(object):
    def __init__(self, logID):
        ...
    def __call__(self, func):
        ...

class ReprInjector(object):
    @classmethod
    def withParent(cls, *argNames):
        ...
    @classmethod
    def simple(cls, *argNames):
        ...

class InternalRepresenter(object):
    argNames: Any
    reprParentFlag: Any
    def __init__(self, reprParentFlag, argNames):
        ...
    def __call__(self, clazz):
        ...

def adisp_async(func, cbname='callback', cbwrapper=...):
    ...
def debugTime(func):
    ...
def makeArr(obj):
    ...
