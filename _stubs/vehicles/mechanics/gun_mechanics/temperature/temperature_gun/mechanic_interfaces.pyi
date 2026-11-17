# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicles/mechanics/gun_mechanics/temperature/temperature_gun/mechanic_interfaces.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from vehicles.mechanics.gun_mechanics.temperature.common import ITemperatureComponentParams as ITemperatureComponentParams, ITemperatureMechanicState as ITemperatureMechanicState
from items.components.shared_components import TemperatureGunParams as TemperatureGunParams

class ITemperatureGunComponentParamsLogic(object):
    @classmethod
    def fromMechanicParams(cls, params):
        ...
    @property
    def coolingDelay(self):
        ...

class ITemperatureGunComponentParams(ITemperatureComponentParams, ITemperatureGunComponentParamsLogic):
    ...

class ITemperatureGunMechanicStateLogic(object):
    @classmethod
    def fromComponentStatus(cls, status, params):
        ...
    def getCoolingTime(self, targetTemperature):
        ...

class ITemperatureGunMechanicState(ITemperatureMechanicState, ITemperatureGunMechanicStateLogic):
    ...
