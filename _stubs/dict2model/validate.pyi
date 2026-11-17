# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/dict2model/validate.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import re as re
from soft_exception import SoftException as SoftException
from dict2model.exceptions import ValidationError as ValidationError, ValidationErrorMessage as ValidationErrorMessage, CumulativeIterableValidationError as CumulativeIterableValidationError
from dict2model.types import ValidatorType as ValidatorType, ValidatorsType as ValidatorsType

class Validator(object):
    __slots__: tuple
    def __call__(self, incoming, *args, **kwargs):
        ...
    def __repr__(self):
        ...
    def _reprArgs(self):
        ...

class Range(Validator):
    _messageMin = 'Must be at least {min}.'
    _messageMax = 'Must be at most {max}.'
    _messageAll = 'Must be between {min} and {max}.'
    __slots__: tuple
    _min: Any
    _max: Any
    def __init__(self, minValue=None, maxValue=None):
        ...
    def __call__(self, incoming, *args, **kwargs):
        ...
    def _reprArgs(self):
        ...
    def _formatError(self, message):
        ...

class Length(Range):
    _messageMin = 'Shorter than minimum length {min}.'
    _messageMax = 'Longer than maximum length {max}.'
    _messageAll = 'Length must be between {min} and {max}.'
    _messageEqual = 'Length must be {equal}.'
    __slots__: tuple
    _equal: Any
    def __init__(self, minValue=None, maxValue=None, equalValue=None):
        ...
    def __call__(self, incoming, *args, **kwargs):
        ...
    def _reprArgs(self):
        ...
    def _formatError(self, message):
        ...

class URL(Validator):
    _regex: Any
    _message = 'Not a valid URL.'
    _schemes: set
    __slots__: tuple
    relative: Any
    requireTld: Any
    _memoized: Any
    class RegexMemoizer(object):
        __slots__: tuple
        _memoized: Any
        def __init__(self):
            ...
        def __call__(self, relative, requireTld):
            ...
        @staticmethod
        def _regexGenerator(relative, requireTld):
            ...
    def __init__(self, relative=False, requireTld=True):
        ...
    def __call__(self, incoming, *args, **kwargs):
        ...
    def _reprArgs(self):
        ...

class NoneOf(Validator):
    _message = 'Value: {value} must not be one of: {values}.'
    __slots__: tuple
    _choices: Any
    _choicesText: Any
    def __init__(self, choices):
        ...
    def __call__(self, incoming, *args, **kwargs):
        ...
    def _reprArgs(self):
        ...

class OneOf(NoneOf):
    _message = 'Value: {value} must be one of: {values}.'
    __slots__: tuple
    def __call__(self, incoming, *args, **kwargs):
        ...

class Regexp(Validator):
    _message = 'String: {value} does not match pattern: {pattern}.'
    __slots__: tuple
    _regex: Any
    def __init__(self, regex, flags=0):
        ...
    def __call__(self, incoming, *args, **kwargs):
        ...
    def _reprArgs(self):
        ...

class IterableValidator(Validator):
    __slots__: tuple
    def __call__(self, incoming, storage, isLastIteration, *args, **kwargs):
        ...
    def createStorage(self):
        ...

class _IterableAttrValidator(IterableValidator):
    __slots__: tuple
    _attrName: Any
    def __init__(self, attrName=None):
        ...
    def getValue(self, incoming):
        ...

class IterableOfUnique(_IterableAttrValidator):
    __slots__: tuple
    def __call__(self, incoming, storage, *args, **kwargs):
        ...
    def createStorage(self):
        ...

class IterableOfSequential(_IterableAttrValidator):
    __slots__: tuple
    _firstValue: Any
    def __init__(self, attrName=None, firstValue=1):
        ...
    def __call__(self, incoming, storage, *args, **kwargs):
        ...
    def createStorage(self):
        ...

class IterableAnyTrue(_IterableAttrValidator):
    __slots__: tuple
    def __call__(self, incoming, storage, lastIteration, *args, **kwargs):
        ...
    def createStorage(self):
        ...

class ValidateIterable(Validator):
    __slots__: tuple
    _validators: Any
    _storageCreator: Any
    def __init__(self, validators, storageCreator=...):
        ...
    def __call__(self, incoming, *args, **kwargs):
        ...

def prepareValidators(validators):
    ...
def runValidators(validations, toValidate):
    ...
