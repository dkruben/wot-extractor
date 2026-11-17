# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/dict2model/exceptions.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import pprint as pprint
from soft_exception import SoftException as SoftException
from dict2model import utils as utils

class ValidationErrorMessage(object):
    _indicator = '>>>'
    __slots__: tuple
    _str: Any
    _data: Any
    def __init__(self, data, title=None):
        ...
    def __str__(self):
        ...
    def __repr__(self):
        ...
    def __add__(self, other):
        ...
    @property
    def data(self):
        ...

class ValidationError(SoftException):
    error: Any
    def __init__(self, error):
        ...

class CumulativeIterableValidationError(ValidationError):
    ...

class AccessToFieldDeniedError(SoftException):
    def __init__(self, message):
        ...
