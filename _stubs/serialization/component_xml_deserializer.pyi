# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/serialization/component_xml_deserializer.py (BYTECODE: a descompilacao falhou; sem bases, decoradores nem valores por omissao).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
from typing import Tuple as Tuple, Any as Any
from future.utils import iteritems as iteritems
import ResMgr as ResMgr
from constants import IS_EDITOR as IS_EDITOR
from items import decodeEnum as decodeEnum
from items.components.c11n_constants import ApplyArea as ApplyArea, Options as Options
from items.utils import getEditorOnlySection as getEditorOnlySection
from serialization.definitions import FieldFlags as FieldFlags, FieldTypes as FieldTypes
from serialization.exceptions import SerializationException as SerializationException
from serialization.serializable_component import SerializableComponent as SerializableComponent
absolute_import: _Any
__all__: _Any

# gerado do bytecode: classes base desconhecidas
class ComponentXmlDeserializer:
    __slots__: _Any
    _ComponentXmlDeserializer__decodeCustomType: _Any
    _ComponentXmlDeserializer__decodeArray: _Any
    _ComponentXmlDeserializer__decodeEnum: _Any
    def __init__(self, customTypes):
        ...
    def decode(self, itemType, xmlCtx, section):
        ...
    def __decodeCustomType(self, customType, ctx, section):
        ...
    def __decodeArray(self, itemType, ctx, section):
        ...
    def __decodeEnum(self, value, enum):
        ...

def __getattr__(name: str) -> _Any: ...  # stub incompleto (gerado do bytecode)
