# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/blueprints/FragmentTypes.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from past.builtins import long as long
import nations as nations
from backports.functools_lru_cache import lru_cache as lru_cache
from items import vehicles as vehicles, ITEM_TYPES as ITEM_TYPES
from random_utils import wchoices as wchoices
from debug_utils import LOG_DEBUG_DEV as LOG_DEBUG_DEV, LOG_ERROR as LOG_ERROR, LOG_WARNING as LOG_WARNING
from . import g_cache as g_cache, BlueprintsException as BlueprintsException, getAllResearchableVehicles as getAllResearchableVehicles
from blueprints.BlueprintTypes import BlueprintTypes as BlueprintTypes
from math_common import round_py2_style as round_py2_style
from typing import Optional as Optional, Tuple as Tuple
_LEGACY_SENTINEL_VEHICLE_ID = 255
_NO_NATION_ID = 15
_NATION_IDS: Any

class BlueprintFragment(object):
    __slots__: tuple
    FTYPE = BlueprintTypes.NONE
    nationID: Any
    vehTypeCD: Any
    total: Any
    def __init__(self, vehTypeCD=0, total=0, enableException=True):
        ...
    def getXPValueForFragments(self, count):
        ...
    def makeIntCompDescr(self, normalized=False):
        ...
    def isUniversal(self):
        ...
    def getRequiredFragmentCounts(self, count=1):
        ...
    def getRequiredIntelligenceDataCounts(self, count=1):
        ...
    def decayExtraFragments(self, count=1):
        ...
    @staticmethod
    def fromIntFragmentCD(fragmentCD, enableException=True):
        ...

class NationalBlueprintFragment(BlueprintFragment):
    __slots__: tuple
    FTYPE = BlueprintTypes.NATIONAL
    @staticmethod
    # decorador original: @lru_cache(...)
    def fromNation(nationNameOrId):
        ...
    def __repr__(self):
        ...
    def isUniversal(self):
        ...

class VehicleBlueprintFragment(BlueprintFragment):
    __slots__: tuple
    FTYPE = BlueprintTypes.VEHICLE
    total: Any
    progressPerFragment: Any
    require: Any
    decays: Any
    nationalRequiredOptions: Any
    @staticmethod
    def fromVehicleType(vehNameOrTypeDescr, enableException=True):
        ...
    def __init__(self, vehTypeCD, enableException=True):
        ...
    def __repr__(self):
        ...
    @property
    def asNationalCD(self):
        ...
    @property
    def asIntelligenceDataCD(self):
        ...
    def getXPValueForFragments(self, count):
        ...
    def getRequiredFragmentCounts(self, count=1):
        ...
    def getRequiredIntelligenceDataCounts(self, count=1):
        ...
    def decayExtraFragments(self, count=1):
        ...
    @staticmethod
    # decorador original: @lru_cache(...)
    def __getNationalRequiredOptions(nationID, vehicleLevel):
        ...

class IntelligenceDataFragment(BlueprintFragment):
    __slots__: tuple
    FTYPE = BlueprintTypes.INTELLIGENCE_DATA
    nationID: Any
    def isUniversal(self):
        ...
    def __repr__(self):
        ...

def getFragmentType(ifragmentCD):
    ...
def upgradeLegacyFragmentCD(ifragmentCD):
    ...
def fromIntFragmentCD(ifragmentCD, enableException=True):
    ...
def toIntFragmentCD(fragment):
    ...
def isValidFragment(maybeFragment, defaultUnlocks):
    ...
def isValidFragmentType(maybeFragment):
    ...
def isUniversalFragment(maybeFragment):
    ...
def isSimilar(fragmentTypeCD1, fragmentTypeCD2, strict=True):
    ...
# decorador original: @lru_cache(...)
def normalizeFragment(ifragmentCD):
    ...
# decorador original: @lru_cache(...)
def _makeIntCompDescr(vehTypeCD, fType, normalized):
    ...
# decorador original: @lru_cache(...)
def getFragmentSpecs(fragmentCD):
    ...
# decorador original: @lru_cache(...)
def _getFragmentSpecs(fragmentCD, enableException=True):
    ...
