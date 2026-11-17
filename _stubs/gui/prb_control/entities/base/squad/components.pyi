# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/prb_control/entities/base/squad/components.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import defaultdict as defaultdict
import typing as typing
from future.utils import viewitems as viewitems, viewkeys as viewkeys
import account_helpers as account_helpers
from constants import MAX_VEHICLE_LEVEL as MAX_VEHICLE_LEVEL
from items.vehicles import getVehicleType as getVehicleType
from typing import Dict as Dict, Generator as Generator, KeysView as KeysView, List as List, Tuple as Tuple, Union as Union
from gui.prb_control.entities.base.squad.entity import SquadEntity as SquadEntity
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
from items.vehicles import VehicleType as VehicleType

class SquadRestrictionsProvider(object):
    __slots__: tuple
    _unitEntity: Any
    def __init__(self):
        ...
    def init(self, unitEntity):
        ...
    def fini(self):
        ...
    def isValid(self):
        ...
    def hasSlotForVehicle(self, vehicle, ignoreOwnVehiclesInUnit=False):
        ...
    def _getAllSelectedVehicles(self, ignoreOwnVehiclesInUnit):
        ...
    @property
    def __squadRestrictions(self):
        ...
    @staticmethod
    def __getTagsWithoutSlot(vehicles, platoonTagRestrictions):
        ...
    @staticmethod
    def __applyVehicleGroupsRestrictions(intCDs, platoonVehicleGroupsRestrictions):
        ...

def _countVehiclesByCompDescr(intCDs):
    ...
def _countVehiclesByTagAndLevel(vehicles, tagsToCount):
    ...
def _totalVehNumberByLevels(countedVehiclesByLevels, levels):
    ...
def _getVehicleInfo(vehicle, tagsToGet):
    ...
