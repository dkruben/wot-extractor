# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/legacy_mechanics/siege_component.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from gui.shared.utils.TimeInterval import TimeInterval as TimeInterval
from constants import VEHICLE_SIEGE_STATE as VEHICLE_SIEGE_STATE

class _ComponentUpdater(object):
    __slots__: tuple
    staticMode: Any
    _parentObj: Any
    _totalTime: Any
    _timeLeft: Any
    _siegeState: Any
    _deviceState: Any
    _isSmooth: Any
    _staticMode: Any
    def __init__(self, parentObj, totalTime, timeLeft, siegeState, deviceState, isSmooth):
        ...
    def __repr__(self):
        ...
    def clear(self):
        ...
    def show(self):
        ...
    def _startTick(self):
        ...
    def _stopTick(self):
        ...
    def set_staticMode(self, value):
        ...

class _ActionScriptUpdater(_ComponentUpdater):
    __slots__: tuple
    def _startTick(self):
        ...
    def _stopTick(self):
        ...

class _PythonUpdater(_ComponentUpdater):
    __slots__: tuple
    _timeInterval: Any
    _startTime: Any
    _finishTime: Any
    _isSmooth: Any
    def __init__(self, parentObj, totalTime, timeLeft, siegeState, deviceState, isSmooth):
        ...
    def clear(self):
        ...
    def _startTick(self):
        ...
    def _stopTick(self):
        ...
    def _tick(self):
        ...
    def _updateSnapshot(self, timeLeft):
        ...

class _SiegeComponent(object):
    __slots__: tuple
    staticMode: Any
    _componentUpdater: Any
    _parentObj: Any
    _clazz: Any
    _staticMode: Any
    def __init__(self, parentObj, clazz):
        ...
    def invalidate(self, totalTime, timeLeft, siegeState, deviceState, isSmooth):
        ...
    def clear(self):
        ...
    def _clearUpdater(self):
        ...
    def set_staticMode(self, value):
        ...

class _DefaultSiegeComponent(_SiegeComponent):
    __slots__: tuple
    def __init__(self, parentObj):
        ...

class _ReplaySiegeComponent(_SiegeComponent):
    __slots__: tuple
    def __init__(self, parentObj):
        ...

def createSiegeComponent(siegeModeIndicator, isReplayPlaying):
    ...
