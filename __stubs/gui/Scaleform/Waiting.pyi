# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/Waiting.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from gui.impl.gen import R as R
from helpers import dependency as dependency
from skeletons.gui.app_loader import IAppLoader as IAppLoader, IWaitingWidget as IWaitingWidget
_logger: Any

class Waiting(object):
    __appLoader: Any
    @classmethod
    def getWaitingView(cls, overlapsUI):
        ...
    @classmethod
    def isVisible(cls):
        ...
    @classmethod
    def isOpened(cls, msg):
        ...
    @classmethod
    def getWaiting(cls, msg):
        ...
    @classmethod
    def getSuspendedWaiting(cls, msg):
        ...
    @classmethod
    def show(cls, message, isSingle=False, interruptCallback=None, overlapsUI=True, isAlwaysOnTop=False, backgroundImage=None, softStart=False, showBg=True):
        ...
    @classmethod
    def hide(cls, message):
        ...
    @classmethod
    def suspend(cls, lockerID=None):
        ...
    @classmethod
    def isResumeLocked(cls):
        ...
    @classmethod
    def resume(cls, lockerID=None, hard=False):
        ...
    @classmethod
    def isSuspended(cls):
        ...
    @classmethod
    def close(cls):
        ...
    @classmethod
    def rollback(cls):
        ...
    @classmethod
    def cancelCallback(cls):
        ...
    @classmethod
    def snapshort(cls):
        ...
    @classmethod
    def __getWaiting(cls):
        ...

def convertToResource(message):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def worker(appLoader=None):
    ...
