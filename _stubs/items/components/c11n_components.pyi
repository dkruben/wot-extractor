# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/items/components/c11n_components.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import itertools as itertools
import operator as operator
from copy import deepcopy as deepcopy
from bisect import bisect as bisect
from functools import partial as partial, reduce as reduce
from backports.functools_lru_cache import lru_cache as lru_cache
from future.utils import lmap as lmap, viewvalues as viewvalues, viewitems as viewitems
from past.builtins import xrange as xrange
from typing import TYPE_CHECKING as TYPE_CHECKING, Union as Union
import Math as Math
import items as items
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS as ARENA_BONUS_TYPE_CAPS
from constants import IS_EDITOR as IS_EDITOR, ARENA_BONUS_TYPE_NAMES as ARENA_BONUS_TYPE_NAMES, DEFAULT_QUEST_START_TIME as DEFAULT_QUEST_START_TIME
from debug_utils import LOG_CURRENT_EXCEPTION as LOG_CURRENT_EXCEPTION
from items import vehicles as vehicles
from items.components import shared_components as shared_components
from items.components.c11n_constants import ApplyArea as ApplyArea, SeasonType as SeasonType, Options as Options, ItemTags as ItemTags, CustomizationType as CustomizationType, MAX_CAMOUFLAGE_PATTERN_SIZE as MAX_CAMOUFLAGE_PATTERN_SIZE, DecalType as DecalType, HIDDEN_CAMOUFLAGE_ID as HIDDEN_CAMOUFLAGE_ID, PROJECTION_DECALS_SCALE_ID_VALUES as PROJECTION_DECALS_SCALE_ID_VALUES, MAX_USERS_PROJECTION_DECALS as MAX_USERS_PROJECTION_DECALS, CustomizationTypeNames as CustomizationTypeNames, DecalTypeNames as DecalTypeNames, ProjectionDecalFormTags as ProjectionDecalFormTags, DEFAULT_SCALE_FACTOR_ID as DEFAULT_SCALE_FACTOR_ID, CUSTOMIZATION_SLOTS_VEHICLE_PARTS as CUSTOMIZATION_SLOTS_VEHICLE_PARTS, CamouflageTilingType as CamouflageTilingType, SLOT_TYPE_NAMES as SLOT_TYPE_NAMES, EMPTY_ITEM_ID as EMPTY_ITEM_ID, SLOT_DEFAULT_ALLOWED_MODEL as SLOT_DEFAULT_ALLOWED_MODEL, EDITING_STYLE_REASONS as EDITING_STYLE_REASONS, CustomizationDisplayType as CustomizationDisplayType, AttachmentSize as AttachmentSize, AttachmentTags as AttachmentTags
from py2to3.patched_future import with_metaclass as with_metaclass
from soft_exception import SoftException as SoftException
from wrapped_reflection_framework import ReflectionMetaclass as ReflectionMetaclass
from editor_copy import edCopy as edCopy
from typing import List as List, Dict as Dict, Type as Type, Tuple as Tuple, Optional as Optional, FrozenSet as FrozenSet, Iterable as Iterable, Callable as Callable, Iterator as Iterator
from account_helpers import Tokens as Tokens
from serializable_types.customizations import CustomizationOutfit as CustomizationOutfit
CUSTOMIZATION_TYPES: dict
CUSTOMIZATION_CLASSES: dict
C11N_PROGRESS_LEVEL_IDX = 0
C11N_PROGRESS_PROGRESS_IDX = 1
C11N_PROGRESS_VALUE_IDX = 2

# base nao representavel no stub: with_metaclass(...)
class BaseCustomizationItem:
    __slots__: tuple
    allSlots = __slots__
    itemType = 0
    id: Any
    tags: Any
    filter: Any
    season: Any
    customizationDisplayType: Any
    i18n: Any
    priceGroup: Any
    priceGroupTags: Any
    requiredToken: Any
    requiredTokenCount: Any
    maxNumber: Any
    texture: Any
    progression: Any
    rarity: Any
    parentGroup: Any
    def __init__(self, parentGroup=None):
        ...
    def _copy(self, newItem):
        ...
    def matchVehicleType(self, vehTypeDescr):
        ...
    def isVehicleBound(self):
        ...
    def hasBattleEffect(self):
        ...
    def isUnlocked(self, tokens):
        ...
    def isRare(self):
        ...
    def isHiddenInUI(self):
        ...
    def isProgressive(self):
        ...
    @property
    def isProgressionRewindEnabled(self):
        ...
    @property
    def isUnique(self):
        ...
    @property
    def isStyleOnly(self):
        ...
    @property
    def isQuestsProgression(self):
        ...
    @classmethod
    def makeIntDescr(cls, itemId):
        ...
    @property
    def compactDescr(self):
        ...
    @property
    def userString(self):
        ...
    @property
    def userKey(self):
        ...
    @property
    def description(self):
        ...
    @property
    def shortDescriptionSpecial(self):
        ...
    @property
    def longDescriptionSpecial(self):
        ...
    @property
    def name(self):
        ...

# base nao representavel no stub: with_metaclass(...)
class PaintItem:
    itemType = CustomizationType.PAINT
    __slots__: tuple
    allSlots: Any
    color: Any
    usageCosts: Any
    gloss: Any
    metallic: Any
    def __init__(self, parentGroup=None):
        ...
    def getAmount(self, parts):
        ...

class EmissionParams:
    emissionTexture: Any
    emissionDeferredPower: Any
    emissionForwardPower: Any
    def __init__(self):
        ...

# base nao representavel no stub: with_metaclass(...)
class DecalItem:
    itemType = CustomizationType.DECAL
    __slots__: tuple
    allSlots: Any
    type: Any
    canBeMirrored: Any
    emissionParams: Any
    def __init__(self, parentGroup=None):
        ...
    def __deepcopy__(self, memodict=...):
        ...

# base nao representavel no stub: with_metaclass(...)
class ProjectionDecalItem:
    itemType = CustomizationType.PROJECTION_DECAL
    __slots__: tuple
    allSlots: Any
    canBeMirroredHorizontally: Any
    glossTexture: Any
    scaleFactorId: Any
    emissionParams: Any
    def __init__(self, parentGroup=None):
        ...
    def __deepcopy__(self, memodict=...):
        ...
    @property
    def canBeMirroredVertically(self):
        ...
    @property
    def canBeMirroredOnlyVertically(self):
        ...

# base nao representavel no stub: with_metaclass(...)
class CamouflageItem:
    itemType = CustomizationType.CAMOUFLAGE
    __slots__: tuple
    allSlots: Any
    compatibleParts: Any
    componentsCovering: Any
    palettes: Any
    invisibilityFactor: Any
    rotation: Any
    tiling: Any
    tilingSettings: Any
    scales: Any
    glossMetallicSettings: Any
    styleId: Any
    emissionParams: Any
    normalMapSettings: Any
    def __init__(self, parentGroup=None):
        ...
    def __deepcopy__(self, memodict=...):
        ...

# base nao representavel no stub: with_metaclass(...)
class PersonalNumberItem:
    itemType = CustomizationType.PERSONAL_NUMBER
    __prohibitedNumbers: tuple
    __slots__: tuple
    allSlots: Any
    compatibleParts: Any
    digitsCount: Any
    previewTexture: Any
    fontInfo: Any
    isMirrored: Any
    def __init__(self, parentGroup=None):
        ...
    @classmethod
    def setProhibitedNumbers(cls, prohibitedNumbers):
        ...
    @classmethod
    def getProhibitedNumbers(cls):
        ...

# base nao representavel no stub: with_metaclass(...)
class SequenceItem:
    itemType = CustomizationType.SEQUENCE
    __slots__: tuple
    allSlots: Any
    sequenceName: Any
    def __init__(self, parentGroup=None):
        ...

# base nao representavel no stub: with_metaclass(...)
class AttachmentItem:
    itemType = CustomizationType.ATTACHMENT
    __slots__: tuple
    allSlots: Any
    modelName: Any
    hangarModelName: Any
    crashModelName: Any
    leftModelName: Any
    rightModelName: Any
    sequenceId: Any
    attachmentLogic: Any
    applyType: Any
    size: Any
    def __init__(self, parentGroup=None):
        ...
    @property
    def scaleFactorId(self):
        ...
    @property
    def rotatable(self):
        ...
    @property
    def scalable(self):
        ...

# base nao representavel no stub: with_metaclass(...)
class StatTrackerItem:
    __prohibitedNumbers: tuple
    itemType = CustomizationType.STAT_TRACKER
    __slots__: tuple
    allSlots: Any
    trackedStatistic: Any
    def __init__(self, parentGroup=None):
        ...
    @classmethod
    def setProhibitedNumbers(cls, prohibitedNumbers):
        ...
    @classmethod
    def adjustToAllowedNumber(cls, number):
        ...

# base nao representavel no stub: with_metaclass(...)
class ModificationItem:
    itemType = CustomizationType.MODIFICATION
    __slots__: tuple
    allSlots: Any
    effects: Any
    useNewWear: Any
    def __init__(self, parentGroup=None):
        ...
    def getEffectValue(self, type, default=0.0):
        ...
    def getToggleValue(self, default=False):
        ...

# base nao representavel no stub: with_metaclass(...)
class StyleItem:
    itemType = CustomizationType.STYLE
    __slots__: tuple
    allSlots: Any
    outfits: Any
    isRent: Any
    rentCount: Any
    modelsSet: Any
    isEditable: Any
    alternateItems: Any
    itemsFilters: Any
    dependencies: Any
    dependenciesAncestors: Any
    _changeableSlotTypes: Any
    styleProgressions: Any
    questsProgression: Any
    nonTankMaterials: Any
    def __init__(self, parentGroup=None):
        ...
    def isVictim(self, color):
        ...
    def isItemInstallable(self, item):
        ...
    @property
    def changeableSlotTypes(self):
        ...
    @property
    def clearableSlotTypes(self):
        ...
    @property
    def isProgression(self):
        ...
    @property
    def isLockedOnVehicle(self):
        ...
    @property
    def isWithSerialNumber(self):
        ...
    @property
    def isProgressionRewindEnabled(self):
        ...
    @property
    def hasDependent(self):
        ...
    @property
    def hasContaineOutfitPart(self):
        ...
    @property
    def is3D(self):
        ...
    def _iteratePartsOutfit(self, season, intCDs, removeFromOutfit):
        ...
    def _opPartsOutfit(self, func, season, outfitComponent, vehicleCD, intCDs=None):
        ...
    def addPartsToOutfit(self, season, outfitComponent, vehicleCD, intCDs=None):
        ...
    def removePartrsFromOutfit(self, season, outfitComponent, vehicleCD, intCDs=None):
        ...
    def changePartsOutfitExceptGunInsignia(self, season, outfitComponent, *intCDs):
        ...

# base nao representavel no stub: with_metaclass(...)
class InsigniaItem:
    itemType = CustomizationType.INSIGNIA
    __slots__: tuple
    allSlots: Any
    atlas: Any
    alphabet: Any
    canBeMirrored: Any
    def __init__(self, parentGroup=None):
        ...

# base nao representavel no stub: with_metaclass(...)
class ItemGroup:
    itemType = CustomizationType.ITEM_GROUP
    __slots__: tuple
    itemPrototype: Any
    name: Any
    def __init__(self, itemClass):
        ...
    @property
    def id(self):
        ...
    @classmethod
    def makeIntDescr(cls, itemId):
        ...
    @property
    def compactDescr(self):
        ...

class PriceGroup(object):
    itemType = CustomizationType.ITEM_GROUP
    __slots__: tuple
    price: Any
    name: Any
    id: Any
    notInShop: Any
    tags: Any
    def __init__(self):
        ...
    @property
    def compactDescr(self):
        ...

# base nao representavel no stub: with_metaclass(...)
class Font:
    itemType = CustomizationType.FONT
    __slots__: tuple
    id: Any
    texture: Any
    alphabet: Any
    mask: Any
    def __init__(self):
        ...
    @property
    def compactDescr(self):
        ...

class _Filter(object):
    __slots__: tuple
    include: Any
    exclude: Any
    def __init__(self):
        ...
    def __deepcopy__(self, memodict=...):
        ...
    def __str__(self):
        ...
    def match(self, item):
        ...

# base nao representavel no stub: with_metaclass(...)
class VehicleFilterNode:
    __slots__: tuple
    nations: Any
    levels: Any
    tags: Any
    vehicles: Any
    def __init__(self):
        ...
    def __deepcopy__(self, memodict=...):
        ...
    def __str__(self):
        ...
    def match(self, vehicleDescr):
        ...
    def matchVehicleType(self, vehicleType):
        ...

# base nao representavel no stub: with_metaclass(...)
class VehicleFilter:
    def match(self, vehicleDescr):
        ...
    def matchVehicleType(self, vehicleType):
        ...

class ItemsFilterNode(object):
    __slots__: tuple
    ids: Any
    itemGroupNames: Any
    tags: Any
    types: Any
    customizationDisplayType: Any
    def __init__(self):
        ...
    def __str__(self):
        ...
    def matchItem(self, item):
        ...

# base nao representavel no stub: with_metaclass(...)
class ItemsFilter:
    def match(self, item):
        ...

class ProgressForCustomization(object):
    __slots__: tuple
    autobound: Any
    levels: Any
    autoGrantCount: Any
    bonusTypes: Any
    priceGroup: Any
    defaultLvl: Any
    def __init__(self):
        ...
    def __deepcopy__(self, memodict=...):
        ...
    def __str__(self):
        ...

class QuestProgressForCustomization(object):
    __slots__: tuple
    styleId: Any
    _groupTokens: Any
    def __init__(self, styleId, unlockChains):
        ...
    def getGroupTokens(self):
        ...
    def isGroupConcurrent(self, token):
        ...
    def getFinishTimes(self, token):
        ...
    def getUnlocks(self, token, count):
        ...
    def getUnlockedCount(self, token, count):
        ...
    def getTotalCount(self):
        ...
    def getItemsForGroup(self, token):
        ...
    def iterateItems(self, tokens=None, itemsFunc=None):
        ...
    def getLevel(self, token, count):
        ...
    def isEverythingUnlocked(self, token, count):
        ...
    def __deepcopy__(self, memodict=...):
        ...
    def __str__(self):
        ...

# base nao representavel no stub: with_metaclass(...)
class CustomizationCache:
    __slots__: tuple
    priceGroupTags: Any
    paints: Any
    camouflages: Any
    decals: Any
    projection_decals: Any
    personal_numbers: Any
    modifications: Any
    itemToPriceGroup: Any
    priceGroups: Any
    priceGroupNames: Any
    styles: Any
    insignias: Any
    defaultInsignias: Any
    defaultPlayerEmblems: Any
    defaultColors: Any
    fonts: Any
    sequences: Any
    attachments: Any
    stat_trackers: Any
    __victimStyles: Any
    customizationWithProgression: Any
    itemToQuestProgressionStyle: Any
    __questStyles: Any
    itemGroupByProgressionBonusType: Any
    topVehiclesByNation: Any
    itemTypes: Any
    def __init__(self):
        ...
    def getQuestProgressionStyles(self):
        ...
    def isVehicleBound(self, itemId):
        ...
    def splitByVehicleBound(self, itemsDict, vehType):
        ...
    def getVictimStyles(self, hunting, vehType):
        ...
    def validateOutfit(self, vehDescr, outfit, progressionStorage, serialNumbersStorage, tokens=None, season=...):
        ...
    def adjustProgression(self, vehTypeCompDescr, outfit, progressionStorage, itemForce=None):
        ...
    def adjustSerialNumber(self, outfit, serialNumberStorage, style):
        ...

class EditingStyleReason(object):
    __nonzero__: Any
    reason: Any
    def __init__(self, reson):
        ...
    def __bool__(self):
        ...

def constructProgression(level=0, progress=None, value=None):
    ...
def _adjustProgression(component, vehTypeCD, item, progressionStorage, attr, force=False):
    ...
def _adjustSerialNumber(component, style, serialNumbersStorage, force=False):
    ...
def _validateItem(typeName, item, season, tokens, vehType, styleID):
    ...
def _validateProgression(component, item, progressionStorage, vehType):
    ...
def _validateStyleProgression(outfit, usedStyle, progressionStorage, vehType):
    ...
def _validateSerialNumber(outfit, item, serialNumberStorage):
    ...
def _validateApplyTo(component, item):
    ...
def _validateCamouflage(component, item):
    ...
def _validateProjectionDecal(component, item, vehDescr, usedStyle=None):
    ...
def _validateAttachment(component, item, vehDescr):
    ...
def _validatePersonalNumber(component, item):
    ...
def _validateStyle(componentId, typeName, itemType, component, item, baseStyle, outfit, vehDescr, baseComponents, season=...):
    ...
def _validateDependencies(outfit, usedStyle, vehDescr, season):
    ...
def getAvailablePaintRegions(vehDescr):
    ...
def getAvailableDecalRegions(vehDescr):
    ...
def splitIntDescr(intDescr):
    ...
def validateCustomizationEnabled(gameParams):
    ...
def validateCustomizationTypeEnabled(gameParams, customizationType):
    ...
def getVehicleAttachmentSlotParams(vehicleDescr, vehicleSlotId):
    ...
def getVehicleProjectionDecalSlotParams(vehicleDescr, vehicleSlotId, partNames=...):
    ...
def getVehicleSlotParams(slotTypeName, vehicleDescr, vehicleSlotId, partNames=...):
    ...
def isPersonalNumberAllowed(personalNumber):
    ...
def adjustToAllowedStatTrackerNumber(number):
    ...
def getAvailableSlotsCount(item, vehicleDescriptor):
    ...
# decorador original: @lru_cache(...)
def isVehicleHasSlots(vehicleComponents, slotType):
    ...
def getItemSlotType(item):
    ...
def getSlotType(itemType, decalType=None):
    ...
