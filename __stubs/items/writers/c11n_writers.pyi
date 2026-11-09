# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/items/writers/c11n_writers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import re as re
import typing as typing
from collections import namedtuple as namedtuple
from future.utils import iteritems as iteritems, itervalues as itervalues, lmap as lmap
import Math as Math
import ResMgr as ResMgr
import items.vehicles as iv
from constants import IS_EDITOR as IS_EDITOR
from items import _xml as _xml, parseIntCompactDescr as parseIntCompactDescr
from serializable_types.types import C11nSerializationTypes as _C11nSerializationTypes
from soft_exception import SoftException as SoftException
from items.components.c11n_constants import SeasonType as SeasonType, DecalType as DecalType, CamouflageTilingType as CamouflageTilingType, CustomizationType as CustomizationType, RENT_DEFAULT_BATTLES as RENT_DEFAULT_BATTLES, EMPTY_ITEM_ID as EMPTY_ITEM_ID, ProjectionDecalType as ProjectionDecalType, CustomizationTypeNames as CustomizationTypeNames, DEFAULT_SCALE_FACTOR_ID as DEFAULT_SCALE_FACTOR_ID, DEFAULT_GLOSS as DEFAULT_GLOSS, DEFAULT_METALLIC as DEFAULT_METALLIC, DEFAULT_SCALE as DEFAULT_SCALE, DEFAULT_ROTATION as DEFAULT_ROTATION, DEFAULT_POSITION as DEFAULT_POSITION
from items.components.c11n_components import StyleItem as StyleItem, ApplyArea as ApplyArea
from items.customizations import FieldTypes as FieldTypes, FieldFlags as FieldFlags, FieldType as FieldType, SerializableComponent as SerializableComponent, SerializationException as SerializationException
from items.type_traits import equalComparator as equalComparator
from nations import NAMES as NAMES
from items.utils import getDefaultGlossTexture as getDefaultGlossTexture
from items.customizations import getEditorOnlySection as getEditorOnlySection
isPropertyShared: Any
DECAL_TYPE_STRING: dict
Description: Any
VEHICLE_FILTER_VALUE_DESCRIPTION: tuple
ITEMS_FILTER_VALUE_DESCRIPTION: tuple
FILTER_ID_NAME: dict
ALTERNATE_TO_NAME: dict
CUSTOMIZATION_ITEMS_TYPE_TO_NAME: dict
CUSTOMIZATION_ITEMS_NAME_TO_TYPE: dict
rewriteInt: Any
rewriteBool: Any
rewriteString: Any
rewriteFloat: Any
rewriteVector2: Any
rewriteVector3: Any
rewriteVector4: Any

class GroupSectionPicker(object):
    ids: Any
    name: Any
    def __init__(self, group):
        ...
    def __call__(self, gsections):
        ...

class VehicleFilterTagsConvertor(object):
    def convertToString(self, valuesList):
        ...

class VehicleFilterLevelConvertor(object):
    def convertToString(self, valuesList):
        ...

class VehicleFilterNationConvertor(object):
    def convertToString(self, valuesList):
        ...

class VehicleFilterVehicleConvertor(object):
    def convertToString(self, valuesList):
        ...

class StringFilterConvertor(object):
    def convertToString(self, valuesList):
        ...

class IntegerFilterConvertor(object):
    def convertToString(self, valuesList):
        ...

class BoolFilterConvertor(object):
    def convertToString(self, valuesList):
        ...

class ItemsFilterDecalTypeConvertor(object):
    def convertToString(self, valuesList):
        ...

class BaseCustomizationItemXmlWriter(object):
    def writeBase(self, item, section):
        ...
    def writeBaseGroup(self, item, section):
        ...

class PaintXmlWriter(BaseCustomizationItemXmlWriter):
    def write(self, item, section, group=None):
        ...

class DecalXmlWriter(BaseCustomizationItemXmlWriter):
    def write(self, item, section, group=None):
        ...

class ProjectionDecalXmlWriter(BaseCustomizationItemXmlWriter):
    def write(self, item, section, group=None):
        ...

class CamouflageXmlWriter(BaseCustomizationItemXmlWriter):
    def write(self, item, section, group=None):
        ...

class ModificationXmlWriter(BaseCustomizationItemXmlWriter):
    def write(self, item, section, group=None):
        ...

class ComponentXmlSerializer(object):
    def __init__(self):
        ...
    def encode(self, section, target, defaultValuesDict=None, deprecatedFieldsToWrite=None):
        ...
    def __encodeCustomType(self, section, key, obj, defaultValuesDict=None, deprecatedFieldsToWrite=None, valueType=0):
        ...
    def __encodeArray(self, section, key, value, fieldType, defaultValuesDict=None, deprecatedFieldsToWrite=None, valueType=0):
        ...
    def __encodeValue(self, section, key, value, fieldType, defaultValuesDict=None, deprecatedFieldsToWrite=None, valueType=0):
        ...

class StyleXmlWriter(BaseCustomizationItemXmlWriter):
    __outfitSerializer: Any
    def write(self, item, section, group=None):
        ...
    def __writeOutfits(self, outfits, section):
        ...
    def __writeOutfit(self, oSections, season, outfit):
        ...
    def __writeAlternateItems(self, alterItems, isection):
        ...
    def __writeDependencies(self, dependencies, isection):
        ...
    def __writeFiltersItems(self, filters, isection):
        ...
    def __write3dProgression(self, progression, isection):
        ...

class PersonalNumberXmlWriter(BaseCustomizationItemXmlWriter):
    def write(self, item, section, group=None):
        ...

class InsigniaXmlWriter(BaseCustomizationItemXmlWriter):
    def write(self, item, section, group=None):
        ...

class AttachmentXmlWriter(BaseCustomizationItemXmlWriter):
    def write(self, item, section, group=None):
        ...

class StatTrackerXmlWriter(BaseCustomizationItemXmlWriter):
    def write(self, item, section, group=None):
        ...

class SequenceXmlWriter(BaseCustomizationItemXmlWriter):
    def write(self, item, section, group=None):
        ...

class FontXmlWriter(object):
    def write(self, item, section, group=None):
        ...

def findOrCreate(section, subsectionName):
    ...
def resizeSection(section, newSize, newName):
    ...
def saveCustomizationItems(cache, folder):
    ...
def writeItemType(writer, cache, folder, itemName, endGroupWriter=None):
    ...
def writeGroup(itemWriter, group, groupSection, itemName, endGroupWriter=None):
    ...
def writeFontType(writer, cache, folder, itemName):
    ...
def _natkey(s):
    ...
def natsorted(seq):
    ...
def saveItemFilter(filter, section, filterName, valueDescription):
    ...
def rewriteEffects(item, section):
    ...
def writeFontAlphabet(item):
    ...
def _needWrite(item, propertyPath):
    ...
def _rewriteFn(tp):
    ...
def rewriteTags(section, item):
    ...
def rewritePalettes(section, item):
    ...
def rewriteCamouflageRotation(section, camouflageItem):
    ...
def rewriteCamouflageScales(section, camouflageItem):
    ...
def correctTankNameByCurrentSectionName(section, tankName):
    ...
def rewriteCamouflageTiling(section, camouflageItem):
    ...
def rewriteCamouflageTilingSettings(section, camouflageItem):
    ...
def rewriteCamouflageGlossMetallicSettings(section, camouflageItem):
    ...
def rewriteCamouflageNormalSettings(section, camouflageItem):
    ...
def rewriteEmissionParams(section, item):
    ...
def encodeFlagEnum(enumClass, intValue):
    ...
def encodeEnum(enumClass, intValue):
    ...
