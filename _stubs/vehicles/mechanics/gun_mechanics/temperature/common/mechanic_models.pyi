# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicles/mechanics/gun_mechanics/temperature/common/mechanic_models.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import BigWorld as BigWorld
from cache import last_cached_method as last_cached_method
from constants import SERVER_TICK_LENGTH as SERVER_TICK_LENGTH
from gui.shared.utils.decorators import ReprInjector as ReprInjector
from math_utils import clamp as clamp
from vehicles.mechanics.gun_mechanics.temperature.common.mechanic_interfaces import ITemperatureComponentParams as ITemperatureComponentParams, ITemperatureMechanicState as ITemperatureMechanicState

# decorador original: @ReprInjector.simple(...)
class TemperatureComponentParams(ITemperatureComponentParams):
    __maxTemperature: Any
    __coolingPerSec: Any
    def __init__(self, maxTemperature, coolingPerSec):
        ...
    @property
    def coolingPerSec(self):
        ...
    @property
    def maxTemperature(self):
        ...

# decorador original: @ReprInjector.simple(...)
class TemperatureMechanicState(ITemperatureMechanicState):
    _state: Any
    _thermalStateID: Any
    _temperature: Any
    _updateTime: Any
    _directionFactor: Any
    _coolingSpeed: Any
    _isStaticTemperature: Any
    _params: Any
    def __init__(self, state, thermalStateID, temperature, updateTime, directionFactor, coolingPerSecFactor, isStaticTemperature, params):
        ...
    @property
    def state(self):
        ...
    @property
    def currentTemperature(self):
        ...
    @property
    def maxTemperature(self):
        ...
    @property
    def temperatureProgress(self):
        ...
    def isTransition(self, other):
        ...
    def getTransitionKey(self):
        ...
    # decorador original: @last_cached_method(...)
    def __getCurrentTemperature(self, serverTime):
        ...
