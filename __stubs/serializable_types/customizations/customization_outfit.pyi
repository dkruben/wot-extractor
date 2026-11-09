# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/serializable_types/customizations/customization_outfit.py (BYTECODE: a descompilacao falhou; sem bases, decoradores nem valores por omissao).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
from collections import OrderedDict as OrderedDict, defaultdict as defaultdict
from data_structures import OrderedSet as OrderedSet
from functools import reduce as reduce
from future.utils import listitems as listitems, viewitems as viewitems
from typing import TYPE_CHECKING as TYPE_CHECKING
from debug_utils import LOG_ERROR as LOG_ERROR
from items.components import c11n_components as c11n_components
from items.components.c11n_constants import ApplyArea as ApplyArea, CustomizationType as CustomizationType, CustomizationTypeNames as CustomizationTypeNames, HIDDEN_CAMOUFLAGE_ID as HIDDEN_CAMOUFLAGE_ID, EMPTY_ITEM_ID as EMPTY_ITEM_ID
from items.named_vector import NamedVector as NamedVector
from items.utils import getDifferVehiclePartNames as getDifferVehiclePartNames
from py2to3.patched_future import with_metaclass as with_metaclass
from serialization import ComponentBinSerializer as ComponentBinSerializer
from serialization.field import intField as intField, strField as strField, intArrayField as intArrayField, customArrayField as customArrayField
from serialization.serializable_component import SerializableComponent as SerializableComponent
from soft_exception import SoftException as SoftException
from wrapped_reflection_framework import ReflectionMetaclass as ReflectionMetaclass
from stat_tracker import StatTrackerComponent as StatTrackerComponent
from attachment import AttachmentComponent as AttachmentComponent
from camouflage import CamouflageComponent as CamouflageComponent
from decal import DecalComponent as DecalComponent
from insignia import InsigniaComponent as InsigniaComponent
from paint import PaintComponent as PaintComponent
from personal_number import PersonalNumberComponent as PersonalNumberComponent
from projection_decal import ProjectionDecalComponent as ProjectionDecalComponent
from sequence import SequenceComponent as SequenceComponent
from types import C11nSerializationTypes as C11nSerializationTypes
from typing import List as List, Dict as Dict, Tuple as Tuple, Any as Any, Optional as Optional, Iterator as Iterator
absolute_import: _Any
cn: _Any
__all__: _Any

# gerado do bytecode: classes base desconhecidas
class CustomizationOutfit:
    customType: _Any
    fields: _Any
    __slots__: _Any
    __nonzero__: _Any
    def __init__(self, modifications=..., paints=..., camouflages=..., decals=..., projection_decals=..., personal_numbers=..., styleId=..., insignias=..., sequences=..., attachments=..., styleProgressionLevel=..., serial_number=..., stat_trackers=...):
        ...
    def __bool__(self):
        ...
    def getInvisibilityCamouflageId(self):
        ...
    def makeCompDescr(self):
        ...
    def empty(self):
        ...
    def applyAreaBitmaskToDict(components):
        ...
    def slotIdToDict(components):
        ...
    def shrinkAreaBitmask(components):
        ...
    def applyDiff(self, outfit, ignoreStyleDiff=...):
        ...
    def getDiff(self, outfit):
        ...
    def dismountComponents(self, applyArea, dismountTypes=...):
        ...
    def dismountUnsuitableComponents(self, vehDescr, oldVehDescr):
        ...
    def countComponents(self, componentId, typeId):
        ...
    def removeComponent(self, componentId, typeId, count):
        ...
    def removeComponents(self, typeIds):
        ...
    def wipe(self, gameParams, cache, getGroupedComponentPrice, vehType=...):
        ...
    def getGunInsignias(self):
        ...

def _setComponentsRegion(component, region):
    ...
def __ignoreItem(itemId, cache, ignoreEmpty, ignoreStyleOnly):
    ...
def getAllItemsFromOutfit(cc, outfit, ignoreHiddenCamouflage=..., ignoreEmpty=..., ignoreStyleOnly=..., skipCommonElements=...):
    ...

def __getattr__(name: str) -> _Any: ...  # stub incompleto (gerado do bytecode)
