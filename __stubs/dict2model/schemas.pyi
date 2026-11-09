# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/dict2model/schemas.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import traceback as traceback
import typing as typing
from future.utils import viewitems as viewitems
from dict2model import validate as validate
from dict2model.exceptions import ValidationError as ValidationError, ValidationErrorMessage as ValidationErrorMessage
from dict2model.fields import AccessDeniedField as AccessDeniedField
from dict2model.models import Model as Model
from py2to3 import patched_typing as patched_typing
from soft_exception import SoftException as SoftException
from dict2model.fields import Field as Field
from dict2model.types import ValidatorsType as ValidatorsType, SchemaModelClassesType as SchemaModelClassesType, TFilter as TFilter
TRawData: Any
_logger: Any
SchemaModelType: Any
accessDeniedField: Any

# base nao representavel no stub: patched_typing.Generic[...]
class Schema:
    __slots__: tuple
    _fields: Any
    _modelClass: Any
    _checkUnknown: Any
    _serializedValidators: Any
    _deserializedValidators: Any
    def __init__(self, fields, modelClass=..., checkUnknown=True, serializedValidators=None, deserializedValidators=None):
        ...
    def serialize(self, incoming, filter_=None, silent=False, logError=True, skipValidation=False, **kwargs):
        ...
    def deserialize(self, incoming, filter_=None, silent=False, logError=True, skipValidation=False, **kwargs):
        ...
    def _serialize(self, incoming, filter_=None, skipValidation=False, **kwargs):
        ...
    def _deserialize(self, incoming, filter_=None, skipValidation=False, **kwargs):
        ...
