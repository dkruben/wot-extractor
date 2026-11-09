# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/items/customizations.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import copy as copy
from future.utils import viewitems as viewitems
from past.builtins import xrange as xrange
from typing import Dict as Dict, TypeVar as TypeVar, Optional as Optional, TYPE_CHECKING as TYPE_CHECKING
from constants import IS_CELLAPP as IS_CELLAPP, IS_BASEAPP as IS_BASEAPP
from debug_utils import LOG_CURRENT_EXCEPTION as LOG_CURRENT_EXCEPTION, LOG_ERROR as LOG_ERROR
from items import decodeEnum as decodeEnum, vehicles as vehicles
from items.components import c11n_components as cn
from items.components.c11n_constants import ApplyArea as ApplyArea, SeasonType as SeasonType, CustomizationType as CustomizationType, CustomizationTypeNames as CustomizationTypeNames, MAX_USERS_PROJECTION_DECALS as MAX_USERS_PROJECTION_DECALS, EMPTY_ITEM_ID as EMPTY_ITEM_ID, MAX_ATTACHMENTS as MAX_ATTACHMENTS, MAX_STAT_TRACKERS as MAX_STAT_TRACKERS
from math_common import round_py2_style_int as round_py2_style_int
from py2to3.compat import base64compat as base64compat
from serializable_types.customizations import PaintComponent as PaintComponent, CamouflageComponent as CamouflageComponent, getAllItemsFromOutfit as getAllItemsFromOutfit, AttachmentComponent as AttachmentComponent, ProjectionDecalComponent as ProjectionDecalComponent, SequenceComponent as SequenceComponent, PersonalNumberComponent as PersonalNumberComponent, InsigniaComponent as InsigniaComponent, CustomizationOutfit as CustomizationOutfit, DecalComponent as DecalComponent, CUSTOMIZATION_CLASSES as _CUSTOMIZATION_CLASSES, parseC11sComponentDescr as parseC11sComponentDescr, StatTrackerComponent as StatTrackerComponent
from serialization import ComponentBinDeserializer as ComponentBinDeserializer, ComponentXmlDeserializer as ComponentXmlDeserializer, SerializationException as SerializationException, EmptyComponent as EmptyComponent, makeCompDescr as makeCompDescr, FieldTypes as FieldTypes, FieldFlags as FieldFlags, FieldType as FieldType, SerializableComponent as SerializableComponent, intField as intField, intArrayField as intArrayField, xmlOnlyFloatField as xmlOnlyFloatField, xmlOnlyFloatArrayField as xmlOnlyFloatArrayField, applyAreaEnumField as applyAreaEnumField, customFieldType as customFieldType, customArrayField as customArrayField, optionsEnumField as optionsEnumField, arrayField as arrayField, strField as strField, xmlOnlyApplyAreaEnumField as xmlOnlyApplyAreaEnumField, xmlOnlyIntField as xmlOnlyIntField, xmlOnlyTagsField as xmlOnlyTagsField
from serialization.serializable_component import SerializableComponentChildType as SerializableComponentChildType
from soft_exception import SoftException as SoftException
from .named_vector import NamedVector as NamedVector
from .utils import getEditorOnlySection as getEditorOnlySection
from items.vehicles import VehicleDescrType as VehicleDescrType
parseCompDescr = parseC11sComponentDescr
_itemType: Any

class OutfitLogEntry(object):
    style_cd: Any
    modification_cd: Any
    _paints: Any
    _decals: Any
    _projection_decals: Any
    _camouflages: Any
    _personal_numbers: Any
    _attachments: Any
    _stat_trackers: Any
    chassis_paint_cd: Any
    hull_paint_cd: Any
    turret_paint_cd: Any
    gun_paint_cd0: Any
    gun_paint_cd1: Any
    hull_camouflage_cd: Any
    turret_camouflage_cd: Any
    gun_camouflage_cd: Any
    hull_decal_cd0: Any
    hull_decal_progression_level0: Any
    hull_decal_cd1: Any
    hull_decal_progression_level1: Any
    hull_decal_cd2: Any
    hull_decal_progression_level2: Any
    hull_decal_cd3: Any
    hull_decal_progression_level3: Any
    turret_decal_cd0: Any
    turret_decal_progression_level0: Any
    turret_decal_cd1: Any
    turret_decal_progression_level1: Any
    turret_decal_cd2: Any
    turret_decal_progression_level2: Any
    turret_decal_cd3: Any
    turret_decal_progression_level3: Any
    hull_personal_number0: Any
    hull_personal_number1: Any
    turret_personal_number0: Any
    turret_personal_number1: Any
    gun_personal_number0: Any
    gun_personal_number1: Any
    style_progression_level: Any
    serial_number: Any
    def __init__(self, outfit):
        ...
    @staticmethod
    def __getItemCompDescr(storage, area, cdFormatter):
        ...
    @staticmethod
    def __getItemCompDescrWithProgression(storage, area, cdFormatter):
        ...
    def __getPaintCd(self, area):
        ...
    def __getCamouflageCd(self, area):
        ...
    def __getDecalCd(self, area):
        ...
    def __getPersonalNumberCd(self, area):
        ...
    def __getProjectionDecalData(self, number):
        ...
    def __getPersonalNumberData(self, area):
        ...
    def __getAttachmentsData(self, number):
        ...
    def __getStatTrackersData(self, number):
        ...
    def toDict(self):
        ...

def checkItemInCompDescr(item, customizationElementCompDescr):
    ...
def parseOutfitDescr(outfitDescr):
    ...
def isEditedStyle(outfit):
    ...
def getNationalEmblemsOutfit(vehDescr):
    ...
def __ignoreItem(itemId, cache, ignoreEmpty, ignoreStyleOnly):
    ...
def getOutfitType(arenaKind, bonusType):
    ...
def getBattleOutfit(getter, vehType, arenaKind, bonusType):
    ...
def parseBattleOutfit(outfit, cache, arenaKind):
    ...
def makeLogOutfitValues(outfitDescr):
    ...
def getHullCamouflageCd(outfitDescr):
    ...
def getVehicleOutfit(outfits, vehTypeDescr, outfitType):
    ...
def createNationalEmblemComponents(vehDescr):
    ...
def _clamp(value, minValue, maxValue, limit):
    ...
def _unclamp(value, minValue, maxValue, limit):
    ...
def _clamp16(value, minValue, maxValue):
    ...
def _unclamp16(value, minValue, maxValue):
    ...
