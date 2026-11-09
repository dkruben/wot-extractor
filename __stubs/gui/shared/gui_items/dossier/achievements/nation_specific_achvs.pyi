# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/gui_items/dossier/achievements/nation_specific_achvs.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from dossiers2.custom.helpers import getMechanicEngineerRequirements as getMechanicEngineerRequirements, getVehicleCollectorRequirements as getVehicleCollectorRequirements, getTankExpertRequirements as getTankExpertRequirements, getAllCollectorVehicles as getAllCollectorVehicles
from gui.shared.gui_items.dossier.achievements.abstract import NationSpecificAchievement as NationSpecificAchievement
from gui.shared.gui_items.dossier.achievements.abstract.mixins import HasVehiclesList as HasVehiclesList
from collector_vehicle import CollectorVehicleConsts as CollectorVehicleConsts
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache

class MechEngineerAchievement(HasVehiclesList, NationSpecificAchievement):
    itemsCache: Any
    _MEDAL_NAME = 'mechanicEngineer'
    _LIST_NAME = 'vehiclesToResearch'
    _vehTypeCompDescrs: Any
    def __init__(self, nationID, block, dossier, value=None):
        ...
    def isActive(self):
        ...
    def _readLevelUpValue(self, dossier):
        ...
    def _getVehiclesDescrsList(self):
        ...
    @classmethod
    def _parseVehiclesDescrsList(cls, name, nationID, dossier):
        ...

class VehicleCollectorAchievement(HasVehiclesList, NationSpecificAchievement):
    __itemsCache: Any
    __slots__: tuple
    _MEDAL_NAME = CollectorVehicleConsts.COLLECTOR_MEDAL_PREFIX
    _NATIONAL_VEHICLES = 'collectorVehiclesByNations'
    _LIST_NAME = 'vehiclesToBuy'
    __hasCollectibleVehicles: Any
    _vehTypeCompDescrs: Any
    def __init__(self, nationID, block, dossier, value=None):
        ...
    def isHidden(self):
        ...
    def isActive(self):
        ...
    def _readLevelUpValue(self, dossier):
        ...
    def _getVehiclesDescrsList(self):
        ...
    @classmethod
    def _getAllSuitableVehicles(cls):
        ...
    @classmethod
    def _parseVehiclesDescrsList(cls, name, nationID, dossier, inventoryVehicles=None):
        ...
    @classmethod
    def __getInventoryCollectibleVehicles(cls, nationID):
        ...

class TankExpertAchievement(HasVehiclesList, NationSpecificAchievement):
    _LIST_NAME = 'vehiclesToKill'
    __vehTypeCompDescrs: Any
    __achieved: Any
    def __init__(self, nationID, block, dossier, value=None):
        ...
    def isActive(self):
        ...
    def _readLevelUpValue(self, dossier):
        ...
    def _getVehiclesDescrsList(self):
        ...
    @classmethod
    def _parseVehiclesDescrsList(cls, name, dossier):
        ...
