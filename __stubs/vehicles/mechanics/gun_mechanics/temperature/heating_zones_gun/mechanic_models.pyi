# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicles/mechanics/gun_mechanics/temperature/heating_zones_gun/mechanic_models.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from constants import HEATING_ZONES_GUN_STATE as HEATING_ZONES_GUN_STATE
from gui.shared.utils.decorators import ReprInjector as ReprInjector
from vehicles.mechanics.gun_mechanics.temperature.heating_zones_gun.mechanic_interfaces import IHeatingZonesGunComponentParams as IHeatingZonesGunComponentParams, IHeatingZonesGunMechanicState as IHeatingZonesGunMechanicState
from items.components.shared_components import HeatingZonesGunParams as HeatingZonesGunParams

# decorador original: @ReprInjector.simple(...)
class HeatingZonesGunComponentParams(IHeatingZonesGunComponentParams):
    __lowZonePercent: Any
    __mediumZonePercent: Any
    def __init__(self, lowZonePercent, mediumZonePercent):
        ...
    @classmethod
    def fromMechanicParams(cls, params):
        ...
    @property
    def lowZonePercent(self):
        ...
    @property
    def mediumZonePercent(self):
        ...

# decorador original: @ReprInjector.simple(...)
class HeatingZonesGunMechanicState(IHeatingZonesGunMechanicState):
    __heatingZoneState: Any
    __params: Any
    def __init__(self, heatingZoneState, params):
        ...
    @classmethod
    def fromComponentStatus(cls, heatingZoneState, params):
        ...
    @property
    def isComfortZone(self):
        ...
    @property
    def heatingZoneState(self):
        ...
    def isTransition(self, other):
        ...
