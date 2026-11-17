# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/items/readers/c11n_readers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
import re as re
import os as os
from copy import deepcopy as deepcopy
from future.utils import lmap as lmap, viewitems as viewitems, viewvalues as viewvalues
from past.builtins import intern as intern
import Math as Math
import items._xml as ix
import items.components.c11n_components as cc
import items.customizations as c11n
import items.vehicles as iv
import nations as nations
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS as ARENA_BONUS_TYPE_CAPS, parseArenaBonusType as parseArenaBonusType
from constants import IS_CLIENT as IS_CLIENT, IS_EDITOR as IS_EDITOR, IS_UE_EDITOR as IS_UE_EDITOR, IS_WEB as IS_WEB, IS_LOAD_GLOSSARY as IS_LOAD_GLOSSARY, DEFAULT_QUEST_FINISH_TIME as DEFAULT_QUEST_FINISH_TIME
from items.components import shared_components as shared_components
from items.components.c11n_constants import CustomizationType as CustomizationType, CustomizationTypeNames as CustomizationTypeNames, ProjectionDecalFormTags as ProjectionDecalFormTags, CustomizationNamesToTypes as CustomizationNamesToTypes, CustomizationDisplayType as CustomizationDisplayType, EMPTY_ITEM_ID as EMPTY_ITEM_ID, SeasonType as SeasonType, ApplyArea as ApplyArea, DecalType as DecalType, ModificationType as ModificationType, RENT_DEFAULT_BATTLES as RENT_DEFAULT_BATTLES, ItemTags as ItemTags, ProjectionDecalType as ProjectionDecalType, DEFAULT_GLOSS as DEFAULT_GLOSS, DEFAULT_METALLIC as DEFAULT_METALLIC
from extension_utils import ResMgr as ResMgr
from typing import Dict as Dict, Type as Type, Tuple as Tuple, Any as Any, TypeVar as TypeVar
from contextlib import contextmanager as contextmanager
from customization_quests_common import serializeToken as serializeToken, PREFIX as PREFIX
from bonus_readers import readUTC as readUTC
from soft_exception import SoftException as SoftException
from items.components.c11n_components import CUSTOMIZATION_CLASSES as CUSTOMIZATION_CLASSES
from reflection_framework.unintrusive_weakref import ref as UnintrusiveWeakRef
from meta_objects.items.components.c11n_components_meta import I18nExposedComponentMeta as I18nExposedComponentMeta
_itemType: _Any
__xmlReaders: dict

class BaseCustomizationItemXmlReader(object):
    __slots__: tuple
    def __init__(self):
        ...
    def _readFromXml(self, target, xmlCtx, section, cache=None):
        ...
    def _readClientOnlyFromXml(self, target, xmlCtx, section, cache=None):
        ...
    @staticmethod
    def readVehicleFilterFromXml(xmlCtx, section):
        ...
    @staticmethod
    def __readFilterNodeFromXml(xmlCtx, section):
        ...

class PaintXmlReader(BaseCustomizationItemXmlReader):
    __slots__: tuple
    def _readFromXml(self, target, xmlCtx, section, cache=None):
        ...
    def _readClientOnlyFromXml(self, target, xmlCtx, section, cache=None):
        ...
    @staticmethod
    def _readUsage(xmlCtx, section):
        ...

class DecalXmlReader(BaseCustomizationItemXmlReader):
    __slots__: tuple
    def _readFromXml(self, target, xmlCtx, section, cache=None):
        ...
    def _readClientOnlyFromXml(self, target, xmlCtx, section, cache=None):
        ...

class ProjectionDecalXmlReader(BaseCustomizationItemXmlReader):
    __slots__: tuple
    def _readFromXml(self, target, xmlCtx, section, cache=None):
        ...
    def _readClientOnlyFromXml(self, target, xmlCtx, section, cache=None):
        ...

class PersonalNumberXmlReader(BaseCustomizationItemXmlReader):
    __slots__: tuple
    def _readFromXml(self, target, xmlCtx, section, cache=None):
        ...
    def _readClientOnlyFromXml(self, target, xmlCtx, section, cache=None):
        ...

class SequenceXmlReader(BaseCustomizationItemXmlReader):
    __slots__: tuple
    def _readFromXml(self, target, xmlCtx, section, cache=None):
        ...
    def _readClientOnlyFromXml(self, target, xmlCtx, section, cache=None):
        ...

class AttachmentXmlReader(BaseCustomizationItemXmlReader):
    __slots__: tuple
    def _readFromXml(self, target, xmlCtx, section, cache=None):
        ...
    def _readClientOnlyFromXml(self, target, xmlCtx, section, cache=None):
        ...

class StatTrackerXmlReader(AttachmentXmlReader):
    __slots__: tuple
    def _readClientOnlyFromXml(self, target, xmlCtx, section, cache=None):
        ...

class ModificationXmlReader(BaseCustomizationItemXmlReader):
    __slots__: tuple
    def _readFromXml(self, target, xmlCtx, section, cache=None):
        ...
    def _readClientOnlyFromXml(self, target, xmlCtx, section, cache=None):
        ...

class CamouflageXmlReader(BaseCustomizationItemXmlReader):
    __slots__: tuple
    def _readFromXml(self, target, xmlCtx, section, cache=None):
        ...
    def _readClientOnlyFromXml(self, target, xmlCtx, section, cache=None):
        ...
    @staticmethod
    def getDefaultNationId(target):
        ...

class StyleXmlReader(BaseCustomizationItemXmlReader):
    __slots__: tuple
    __outfitDeserializer: _Any
    def __readOutfitSection(self, targetId, section, xmlCtx):
        ...
    def _readFromXml(self, target, xmlCtx, section, cache=None):
        ...
    @staticmethod
    def _readItemsFilterFromXml(itemType, xmlCtx, section):
        ...
    @staticmethod
    def __readItemFilterNodeFromXml(itemType, xmlCtx, section):
        ...
    def _readClientOnlyFromXml(self, target, xmlCtx, section, cache=None):
        ...

class InsigniaXmlReader(BaseCustomizationItemXmlReader):
    __slots__: tuple
    def _readFromXml(self, target, xmlCtx, section, cache=None):
        ...
    def _readClientOnlyFromXml(self, target, xmlCtx, section, cache=None):
        ...

# decorador original: @contextmanager
def storeChangedProperties(obj, props):
    ...
def readCustomizationCacheFromXml(cache, folder):
    ...
def _validateStyles(cache):
    ...
def _validateCamouflages(cache):
    ...
def _readProhibitedNumbers(itemCls, xmlCtx, section):
    ...
def __readProgressLevel(xmlCtx, section):
    ...
def __readCondition(xmlCtx, section, path):
    ...
def __readProgress(xmlCtx, section):
    ...
def _readProgression(cache, xmlCtx, section, progression):
    ...
def _readItems(cache, itemCls, xmlCtx, section, itemSectionName, storage, progression):
    ...
def _addEmptyItem(itemCls, storage, itemSectionName):
    ...
def _readPriceGroups(cache, xmlCtx, section, sectionName, prices=None):
    ...
def _readFonts(cache, xmlCtx, section, sectionName):
    ...
def _readDefault(cache, xmlCtx, section, sectionName):
    ...
def readQuestProgression(cache, xmlCtx, section, sectionName):
    ...
def readFlagEnum(xmlCtx, section, subsectionName, enumClass, defaultValue=None):
    ...
def readEnum(xmlCtx, section, subsectionName, enumClass, defaultValue=None):
    ...
def readEmissionParams(target, xmlCtx, section):
    ...
