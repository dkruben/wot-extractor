# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/serialization/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from serialization.components.empty import EmptyComponent as EmptyComponent
from .component_bin_serializer import ComponentBinSerializer as ComponentBinSerializer
from .component_bin_deserializer import ComponentBinDeserializer as ComponentBinDeserializer
from .component_xml_deserializer import ComponentXmlDeserializer as ComponentXmlDeserializer
from .serializable_component import SerializableComponent as SerializableComponent
from .exceptions import SerializationException as SerializationException, FoundItemException as FoundItemException
from .definitions import FieldTypes as FieldTypes, FieldFlags as FieldFlags, FieldType as FieldType
from .field import arrayField as arrayField, intField as intField, strField as strField, xmlOnlyIntField as xmlOnlyIntField, xmlOnlyFloatField as xmlOnlyFloatField, xmlOnlyFloatArrayField as xmlOnlyFloatArrayField, applyAreaEnumField as applyAreaEnumField, xmlOnlyApplyAreaEnumField as xmlOnlyApplyAreaEnumField, xmlOnlyTagsField as xmlOnlyTagsField, optionsEnumField as optionsEnumField, customFieldType as customFieldType, intArrayField as intArrayField, customArrayField as customArrayField
from .utils import makeCompDescr as makeCompDescr, parseCompDescr as parseCompDescr
__all__: tuple
