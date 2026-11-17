# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/dict2model/extensions/color.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from Math import Vector4 as Vector4
from dict2model import models as models, validate as validate
from dict2model.fields import Float as Float, HexColorCode as HexColorCode
from dict2model.schemas import Schema as Schema
colorSchema: Any

class ColorModel(models.Model):
    __slots__: tuple
    code: Any
    alpha: Any
    __red: Any
    __green: Any
    __blue: Any
    def __init__(self, code, alpha):
        ...
    @property
    def red(self):
        ...
    @property
    def green(self):
        ...
    @property
    def blue(self):
        ...
    def toFloats(self):
        ...
    def _reprArgs(self):
        ...
