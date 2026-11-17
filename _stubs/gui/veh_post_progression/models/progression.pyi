# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/veh_post_progression/models/progression.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from collections import namedtuple as namedtuple
from enum import Enum as Enum, unique as unique
from AccountCommands import LOCK_REASON as LOCK_REASON
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE, GUI_ITEM_TYPE_NAMES as GUI_ITEM_TYPE_NAMES
from gui.veh_post_progression.models.ext_money import ExtendedMoney as ExtendedMoney
from gui.veh_post_progression.models.iterators import OrderedStepsIterator as OrderedStepsIterator, UnorederdStepsIterator as UnorederdStepsIterator
from gui.veh_post_progression.models.progression_step import PostProgressionStepItem as PostProgressionStepItem
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache
from items import vehicles as vehicles
from post_progression_common import FEATURE_BY_GROUP_ID as FEATURE_BY_GROUP_ID, ROLESLOT_FEATURE as ROLESLOT_FEATURE, VEH_SKILL_TREE_ID_OFFSET as VEH_SKILL_TREE_ID_OFFSET, VehicleState as VehicleState
from skeletons.gui.game_control import IVehiclePostProgressionController as IVehiclePostProgressionController
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
from helpers.server_settings import VehiclePostProgressionConfig as VehiclePostProgressionConfig
from items.components.post_progression_components import ProgressionTree as ProgressionTree
from items.vehicles import VehicleType as VehicleType
_LOCK_TO_STATE: dict

# decorador original: @unique
class PostProgressionAvailability(Enum):
    AVAILABLE = 'available'
    NOT_EXISTS = 'not_exits'
    VEH_NOT_ELITE = ' veh_not_elite'
    VEH_NOT_IN_INVENTORY = 'veh_not_in_inventory'
    VEH_IS_RENTED = 'veh_is_rented'
    VEH_IS_RENT_OVER = 'veh_is_rent_over'
    VEH_IN_BATTLE = 'veh_in_battle'
    VEH_IN_FORMATION = 'veh_in_formation'
    VEH_IN_QUEUE = 'veh_in_queue'
    VEH_IN_BREAKER = 'veh_in_breaker'
    VEH_IS_BROKEN = 'veh_is_broken'

# decorador original: @unique
class PostProgressionCompletion(Enum):
    EMPTY = 'empty'
    PARTIAL = 'partial'
    FULL = 'full'

# base nao representavel no stub: namedtuple(...)
class AvailabilityCheckResult:
    def __nonzero__(self):
        ...

class PostProgressionItem(object):
    __postProgressionCtrl: Any
    __itemsCache: Any
    __slots__: tuple
    __state: Any
    __stepsCache: Any
    __tree: Any
    __vehType: Any
    def __init__(self, state, vehType):
        ...
    def __repr__(self):
        ...
    @property
    def itemTypeID(self):
        ...
    @property
    def itemTypeName(self):
        ...
    def isActive(self, veh):
        ...
    def isAvailable(self, veh, unlockOnly=False):
        ...
    def isDefined(self):
        ...
    def isDisabled(self, veh, settings=None, skipRentalIsOver=False):
        ...
    def isExists(self, settings=None):
        ...
    def isFeatureEnabled(self, featureName):
        ...
    def isRoleSlotActive(self, veh):
        ...
    def isRoleSlotExists(self, externalState=None):
        ...
    def isSetupSwitchActive(self, veh, gID):
        ...
    def isPrebattleSwitchDisabled(self, groupID):
        ...
    def isVehSkillTree(self):
        ...
    def getFirstPurchasableStep(self, balance):
        ...
    def getActiveModifications(self, vehicle, ignoreDisabled=False):
        ...
    def getCompletion(self):
        ...
    def getInstalledMultiIds(self):
        ...
    def getRawTree(self):
        ...
    def getState(self, implicitCopy=True):
        ...
    def getStep(self, stepID):
        ...
    def getVehType(self):
        ...
    def setState(self, state):
        ...
    def clone(self):
        ...
    def iterOrderedSteps(self):
        ...
    def iterUnorderedSteps(self):
        ...
    def __buildPostProgressionStep(self, stepID):
        ...
