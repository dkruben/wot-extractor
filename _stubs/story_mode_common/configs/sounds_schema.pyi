# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/common/story_mode_common/configs/sounds_schema.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from dict2model import models as models
from dict2model.schemas import Schema as Schema
from dict2model.fields import String as String
from soft_exception import SoftException as SoftException
from dict2model.types import ValidatorsType as ValidatorsType
from dict2model.fields import Field as Field
_SoundModelType: Any
soundSchema: Any

class SoundModel(models.Model):
    __slots__: tuple
    start: Any
    stop: Any
    group: Any
    state: Any
    def __init__(self, start, stop, group, state):
        ...

# base nao representavel no stub: Schema[...]
class SoundSchema:
    def __init__(self, fields=None, modelClass=..., checkUnknown=True, serializedValidators=None, deserializedValidators=None):
        ...
