# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/vehicle_hub/views/sub_models/armor_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import Enum as Enum
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.vehicle_hub.views.sub_models.armor_attacker import ArmorAttacker as ArmorAttacker
from gui.impl.gen.view_models.views.lobby.vehicle_hub.views.sub_models.armor_value_model import ArmorValueModel as ArmorValueModel
from gui.impl.gen.view_models.views.lobby.vehicle_hub.views.sub_models.armor_vehicle import ArmorVehicle as ArmorVehicle

class Modes(Enum):
    NOMINAL = 'nominal'
    PENETRATION = 'penetration'
    NO_ARMOR = 'no_armor'

class DCCType(Enum):
    PENETRATION = 'penetration'
    RICOCHET = 'ricochet'
    NO_DAMAGE = 'no_damage'

class MinorShortTooltipTypes(Enum):
    MAIN_ARMOR = 'mainArmor'
    SPACED_ARMOR = 'spacedArmor'
    DEALING_DAMAGE_CHANCE = 'dealingDamageChance'
    NO_DAMAGE = 'noDamage'
    RICOCHET = 'ricochet'
    ATTACKING_CONFIGURATION = 'attackingConfiguration'

class ArmorModel(ViewModel):
    __slots__: tuple
    onDragModule: Any
    onDragStateChanged: Any
    onModeChanged: Any
    onAttackerClicked: Any
    onGunItemClick: Any
    onTurretItemClick: Any
    onAttackerGunItemClick: Any
    onAttackerShellItemClick: Any
    def __init__(self, properties=11, commands=8):
        ...
    @property
    def attacker(self):
        ...
    @staticmethod
    def getAttackerType():
        ...
    @property
    def vehicle(self):
        ...
    @staticmethod
    def getVehicleType():
        ...
    def getMainArmor(self):
        ...
    def setMainArmor(self, value):
        ...
    @staticmethod
    def getMainArmorType():
        ...
    def getSpacedArmor(self):
        ...
    def setSpacedArmor(self, value):
        ...
    @staticmethod
    def getSpacedArmorType():
        ...
    def getMainGradient(self):
        ...
    def setMainGradient(self, value):
        ...
    def getSpacedGradient(self):
        ...
    def setSpacedGradient(self, value):
        ...
    def getPenetrationChance(self):
        ...
    def setPenetrationChance(self, value):
        ...
    @staticmethod
    def getPenetrationChanceType():
        ...
    def getNoDamage(self):
        ...
    def setNoDamage(self, value):
        ...
    @staticmethod
    def getNoDamageType():
        ...
    def getPenetrationGradient(self):
        ...
    def setPenetrationGradient(self, value):
        ...
    def getDragModuleMode(self):
        ...
    def setDragModuleMode(self, value):
        ...
    def getSelectedMode(self):
        ...
    def setSelectedMode(self, value):
        ...
    def _initialize(self):
        ...
