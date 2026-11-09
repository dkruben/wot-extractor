# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/veh_post_progression/models/progression_step.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from enum import Enum as Enum, unique as unique
from gui.veh_post_progression.models.ext_money import ExtendedMoney as ExtendedMoney, ExtendedGuiItemEconomyCode as ExtendedGuiItemEconomyCode
from gui.veh_post_progression.models.modifications import getActionModel as getActionModel
from gui.veh_post_progression.models.purchase import PurchaseProvider as PurchaseProvider, PurchaseCheckResult as PurchaseCheckResult, VALID_CHECK_RESULT as VALID_CHECK_RESULT
from items.components.post_progression_components import TreeStep as TreeStep
from post_progression_prices_common import getPostProgressionPrice as getPostProgressionPrice
from items.artefacts_helpers import VehicleFilter as VehicleFilter
from gui.veh_post_progression.models.modifications import SimpleModItem as SimpleModItem, MultiModsItem as MultiModsItem, FeatureModItem as FeatureModItem, RoleSlotModItem as RoleSlotModItem
from gui.veh_post_progression.models.progression import PostProgressionItem as PostProgressionItem
from post_progression_common import VehicleState as VehicleState
_STATE_TO_RESTRICTION: dict

# decorador original: @unique
class PostProgressionStepState(Enum):
    RESTRICTED = 'restricted'
    LOCKED = 'locked'
    UNLOCKED = 'unlocked'
    RECEIVED = 'received'

class PostProgressionStepItem(PurchaseProvider):
    __slots__: tuple
    __action: Any
    __descriptor: Any
    __isRestricted: Any
    __price: Any
    __state: Any
    def __init__(self, descriptor, progression):
        ...
    def __repr__(self):
        ...
    @property
    def action(self):
        ...
    @property
    def stepID(self):
        ...
    def isLocked(self):
        ...
    def isReceived(self):
        ...
    def isRestricted(self):
        ...
    def isUnlocked(self):
        ...
    def getLevel(self):
        ...
    def getNextStepIDs(self):
        ...
    def getParentStepID(self):
        ...
    def getParentStepIDs(self):
        ...
    def getPrice(self):
        ...
    def getRestrictions(self):
        ...
    def getState(self):
        ...
    def getPosition(self):
        ...
    def getDirections(self):
        ...
    def getType(self):
        ...
    def getUnlockStrategy(self):
        ...
    def mayPurchase(self, balance, ignoreState=False):
        ...
    def mayPurchaseWithExchange(self, balance, creditsRate, ignoreState=False):
        ...
    def __getState(self, progressionState):
        ...
    def __getStateCheckResult(self):
        ...
