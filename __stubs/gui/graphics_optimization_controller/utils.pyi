# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/graphics_optimization_controller/utils.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import Math as Math
import typing as typing
PERMANENT_SETTING_ID = ''

class OptimizationSetting(object):
    __slots__: tuple
    __id: Any
    __isInvert: Any
    def __init__(self, settingID=..., isInvert=False):
        ...
    @property
    def id(self):
        ...
    @property
    def isInvert(self):
        ...

def getRectBounds(x, y, width, height):
    ...
def rescaleRectBounds(scale, x, y, width, height):
    ...
def getSettingsNames(config):
    ...
