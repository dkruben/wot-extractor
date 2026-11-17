# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/game_params_common/schema.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from constants import IS_CLIENT as IS_CLIENT, IS_BASEAPP as IS_BASEAPP, IS_CELLAPP as IS_CELLAPP
from dict2model.schemas import Schema as Schema, SchemaModelType as SchemaModelType
from dict2model.types import SchemaModelClassesType as SchemaModelClassesType, ValidatorsType as ValidatorsType
from dict2model.fields import Field as Field
from section2dict import TReaders as TReaders

# base nao representavel no stub: Schema[...]
class GameParamsSchema:
    __slots__: tuple
    readers: Any
    usedInReplay: Any
    _gameParamsKey: Any
    def __init__(self, gameParamsKey, fields, modelClass=..., checkUnknown=True, serializedValidators=None, deserializedValidators=None, readers=None, usedInReplay=False):
        ...
    @property
    def gpKey(self):
        ...
    def getModel(self, **kwargs):
        ...
