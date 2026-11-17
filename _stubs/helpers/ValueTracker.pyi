# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/helpers/ValueTracker.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import math as math
import functools as functools
from future.utils import viewitems as viewitems
import GUI as GUI
import constants as constants
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer

class ValueTracker(CallbackDelayer):
    _ENABLED: Any
    __instance = None
    textGui: Any
    __items: Any
    __avgInfo: Any
    __textGui: Any
    __tickNames: Any
    @staticmethod
    def enable(isEnable):
        ...
    @staticmethod
    def instance():
        ...
    def __init__(self):
        ...
    def destroy(self):
        ...
    def clear(self):
        ...
    def addValue(self, name, value):
        ...
    def addValue2(self, name, value):
        ...
    def addValueAverage(self, name, value, maxAmount=100):
        ...
    def addValueTick(self, name, callback, period):
        ...
    def removeValueTick(self, name):
        ...
    def __tickFunc(self, name, callback, period):
        ...
    def __updateText(self):
        ...
