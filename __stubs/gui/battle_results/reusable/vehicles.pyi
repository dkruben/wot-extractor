# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_results/reusable/vehicles.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import weakref as weakref
from collections import defaultdict as defaultdict, namedtuple as namedtuple
import typing as typing
from constants import DEATH_REASON_ALIVE as DEATH_REASON_ALIVE
from gui.battle_results.reusable import shared as shared, ReusableInfoFactory as ReusableInfoFactory
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache
from .players import PlayerInfo as PlayerInfo
_VehicleShortInfo: Any

class VehiclesInfo(shared.UnpackedInfo):
    __slots__: tuple
    itemsCache: Any
    __vehicles: Any
    __vehicleToAccountID: Any
    __accountToVehicleID: Any
    __details: Any
    __bonusType: Any
    def __init__(self, bonusType, vehicles):
        ...
    def getAccountDBID(self, vehicleID):
        ...
    def getVehicleID(self, accountDBID):
        ...
    def getVehicleInfo(self, vehicleID):
        ...
    def getVehicleSummarizeInfo(self, player, result):
        ...
    def getAIBotVehicleSummarizeInfo(self, vehicleID, player, result):
        ...
    def __getVehicleSummarize(self, vehicleID, player, result):
        ...

def _getVehiclesGenerator(vehicles):
    ...
