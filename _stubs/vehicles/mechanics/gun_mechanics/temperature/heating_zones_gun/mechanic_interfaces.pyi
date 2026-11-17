# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicles/mechanics/gun_mechanics/temperature/heating_zones_gun/mechanic_interfaces.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from vehicles.mechanics.mechanic_states import IMechanicState as IMechanicState
from items.components.shared_components import HeatingZonesGunParams as HeatingZonesGunParams

class IHeatingZonesGunComponentParams(object):
    @classmethod
    def fromMechanicParams(cls, params):
        ...
    @property
    def lowZonePercent(self):
        ...
    @property
    def mediumZonePercent(self):
        ...

class IHeatingZonesGunMechanicState(IMechanicState):
    @classmethod
    def fromComponentStatus(cls, heatingZoneState, params):
        ...
    @property
    def isComfortZone(self):
        ...
    @property
    def heatingZoneState(self):
        ...
