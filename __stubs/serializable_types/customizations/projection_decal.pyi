# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/serializable_types/customizations/projection_decal.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import OrderedDict as OrderedDict
from constants import IS_EDITOR as IS_EDITOR
from items.components.c11n_constants import ApplyArea as ApplyArea, Options as Options, DEFAULT_SCALE_FACTOR_ID as DEFAULT_SCALE_FACTOR_ID, DEFAULT_SCALE as DEFAULT_SCALE, DEFAULT_ROTATION as DEFAULT_ROTATION, DEFAULT_POSITION as DEFAULT_POSITION, DEFAULT_DECAL_TINT_COLOR as DEFAULT_DECAL_TINT_COLOR, ProjectionDecalMatchingTags as ProjectionDecalMatchingTags
from py2to3.patched_future import with_metaclass as with_metaclass
from serialization import FieldFlags as FieldFlags
from serialization.field import intField as intField, optionsEnumField as optionsEnumField, xmlOnlyApplyAreaEnumField as xmlOnlyApplyAreaEnumField, xmlOnlyFloatArrayField as xmlOnlyFloatArrayField, xmlOnlyIntField as xmlOnlyIntField, intArrayField as intArrayField, xmlOnlyTagsField as xmlOnlyTagsField
from serialization.serializable_component import SerializableComponent as SerializableComponent
from wrapped_reflection_framework import ReflectionMetaclass as ReflectionMetaclass
from ..types import C11nSerializationTypes as C11nSerializationTypes
__all__: tuple

# base nao representavel no stub: with_metaclass(...)
class ProjectionDecalComponent:
    customType = C11nSerializationTypes.PROJECTION_DECAL
    fields: Any
    __slots__: tuple
    id: Any
    options: Any
    slotId: Any
    scaleFactorId: Any
    showOn: Any
    scale: Any
    rotation: Any
    position: Any
    tintColor: Any
    doubleSided: Any
    tags: Any
    preview: Any
    progressionLevel: Any
    def __init__(self, id=0, options=..., slotId=0, scaleFactorId=..., showOn=..., scale=..., rotation=..., position=..., tintColor=..., doubleSided=0, tags=None, preview=False, progressionLevel=0):
        ...
    def __str__(self):
        ...
    def isMirroredHorizontally(self):
        ...
    def isMirroredVertically(self):
        ...
    def isFilled(self):
        ...
    @property
    def matchingTag(self):
        ...
