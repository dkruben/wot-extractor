# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/items_parameters/bonus_helper.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import copy as copy
import typing as typing
from future.utils import itervalues as itervalues
from constants import BonusTypes as BonusTypes
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE, KPI as KPI, VEHICLE_ATTR_TO_KPI_NAME_MAP as VEHICLE_ATTR_TO_KPI_NAME_MAP
from gui.shared.items_parameters import isAutoReloadGun as isAutoReloadGun, isAutoShootGun as isAutoShootGun
from gui.shared.items_parameters.comparator import CONDITIONAL_BONUSES as CONDITIONAL_BONUSES, getParamExtendedData as getParamExtendedData
from gui.shared.items_parameters.params import VehicleParams as VehicleParams
from gui.shared.items_parameters.params_constants import EXTRAS_CAMOUFLAGE as EXTRAS_CAMOUFLAGE
from helpers import dependency as dependency
from items import vehicles as vehicles
from items.components.c11n_components import SeasonType as SeasonType
from post_progression_common import ACTION_TYPES as ACTION_TYPES
from shared_utils import findFirst as findFirst
from skeletons.gui.shared import IItemsCache as IItemsCache
import gui as gui
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
from items.vehicle_items import Gun as Gun
_SITUATIONAL_BONUSES: tuple
CREW_MASTERY_BONUSES: tuple
_PARTIALLY_SITUATIONAL_BONUSES: dict
_VEHICLE_RESTRICTION_BONUSES: dict
_VEHICLE_MODIFIERS: dict
_NOT_STACK_BONUSES: dict

class _BonusSorter(object):
    __paramName: Any
    def __init__(self, paramName):
        ...
    def sort(self, bonuses):
        ...
    def __conditionsSorter(self, bonuses):
        ...
    def __getNumDependencies(self, bonus, dependenciesNum=0):
        ...
    def __notStackSorter(self, bonuses):
        ...

class BonusExtractor(object):
    itemsCache: Any
    __vehicle: Any
    __paramName: Any
    __bonuses: Any
    __situationalBonuses: Any
    __removeCamouflage: Any
    def __init__(self, vehicle, bonuses, paramName):
        ...
    def getBonusInfo(self):
        ...
    def extractBonus(self, bonusGroup, bonusID):
        ...
    def _removeNonTargetSituationalBonuses(self, targetBonusID, bonusGroup):
        ...
    def _getCopyVehicle(self, vehicle):
        ...
    def __extractParamValue(self, vehicle, paramName, situationalBonuses=None):
        ...
    @staticmethod
    def __reorderDevices(devices):
        ...
    @staticmethod
    def __reorderSkills(bonuses, vehicle):
        ...
    def __removeNoEffectCrewBooster(self, vehicle):
        ...

class EasyTankEquipBonusExtractor(BonusExtractor):
    def _getCopyVehicle(self, vehicle):
        ...

class TankSetupBonusExtractor(BonusExtractor):
    def _getCopyVehicle(self, vehicle):
        ...

class PostProgressionBonusExtractor(BonusExtractor):
    def _getCopyVehicle(self, vehicle):
        ...

class _CustomizedVehicleParams(VehicleParams):
    __removeCamouflage: Any
    def __init__(self, vehicle, removeCamouflage, situationalBonuses=None):
        ...
    def _getVehicleDescriptor(self, vehicle):
        ...

def isSituationalBonus(bonusName, bonusType='', paramName=''):
    ...
def isAppropriateVehicle(bonusName, vehicle):
    ...
def _loaderMagMasteryValidator(vehicle):
    ...
def _loaderSecondChanceValidator(vehicle):
    ...
def _removeCamouflageModifier(vehicle, bonusID):
    ...
def _removeSkillModifier(vehicle, skillName):
    ...
def _removeBattleBoosterModifier(vehicle, boosterName):
    ...
def _removeOptionalDeviceModifier(vehicle, optDevName):
    ...
def _removeEquipmentModifier(vehicle, eqName):
    ...
def _removePostProgressionModification(vehicle, modificationName):
    ...
def _removePostProgressionBaseModifications(vehicle, modificationsName):
    ...
