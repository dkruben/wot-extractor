# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/helpers/PixieBG.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import weakref as weakref
import functools as functools
from past.builtins import xrange as xrange
import Pixie as Pixie
from debug_utils import LOG_ERROR as LOG_ERROR, LOG_CURRENT_EXCEPTION as LOG_CURRENT_EXCEPTION

class PixieBG(object):
    __slots__: tuple
    name: Any
    pixie: Any
    __data: Any
    __loader: Any
    __callback: Any
    @staticmethod
    def enablePixie(pixie, turnOn):
        ...
    @staticmethod
    def onLoad(pixieBGRef, newPixie):
        ...
    def __init__(self, name, onLoadCallback, pixie=None, data=None, modifiers=None):
        ...
    def __del__(self):
        ...
    def destroy(self, forceKill=False):
        ...
    def onPixieLoaded(self, newPixie):
        ...
    def stopLoading(self):
        ...
    def stopEmission(self):
        ...
    def clear(self):
        ...
    def scale(self, scale):
        ...
    def force(self, force):
        ...
