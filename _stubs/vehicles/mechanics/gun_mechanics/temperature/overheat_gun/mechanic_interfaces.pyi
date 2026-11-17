# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicles/mechanics/gun_mechanics/temperature/overheat_gun/mechanic_interfaces.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from vehicles.mechanics.mechanic_states import IMechanicState as IMechanicState
from items.components.shared_components import OverheatGunParams as OverheatGunParams
from vehicles.mechanics.gun_mechanics.temperature.temperature_gun import ITemperatureGunMechanicState as ITemperatureGunMechanicState

class IOverheatGunComponentParams(object):
    @classmethod
    def fromMechanicParams(cls, params):
        ...
    @property
    def overheatWarnPercent(self):
        ...
    @property
    def overheatOffPercent(self):
        ...
    @property
    def overheatOffThreshold(self):
        ...

class IOverheatGunMechanicState(IMechanicState):
    @classmethod
    def fromComponentStatus(cls, overheatState, params):
        ...
    @property
    def isOverheated(self):
        ...
    @property
    def overheatState(self):
        ...
    def overheatTimeLeft(self, temperatureGunState):
        ...
