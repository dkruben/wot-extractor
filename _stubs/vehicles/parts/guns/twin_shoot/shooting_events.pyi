# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicles/parts/guns/twin_shoot/shooting_events.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import BigWorld as BigWorld
from vehicles.parts.guns.twin_shoot.guns_interfaces import ITwinShootingEventsLogic as ITwinShootingEventsLogic, ITwinShootingListenerLogic as ITwinShootingListenerLogic
from vehicles.parts.guns.common import GunShootingEvents as GunShootingEvents, GunShootingCoreIntegration as GunShootingCoreIntegration, GunShootingEventsDebugger as GunShootingEventsDebugger
from vehicles.parts.guns.twin_shoot.guns_interfaces import ITwinShootGunComponent as ITwinShootGunComponent

class TwinShootingEvents(GunShootingEvents, ITwinShootingEventsLogic):
    __lastShotTime: Any
    onActiveGunsUpdate: Any
    onAnimatedGunsUpdate: Any
    def __init__(self, component):
        ...
    def destroy(self):
        ...
    def processNextGunsUpdate(self, nextGunIndexes):
        ...
    def processDiscreteShot(self, gunIndex):
        ...
    def processMultiShot(self, gunIndexes):
        ...
    def _createCoreIntegration(self):
        ...
    def _createEventsDebugger(self):
        ...
    def _lateSubscribe(self, listener):
        ...
    def __needDelayGunsAnimation(self):
        ...
    def __getAnimatedGunIndexes(self, gunIndexes=None, nextGunIndexes=None):
        ...
    def __lateActiveGunsUpdate(self, handler):
        ...
    def __lateAnimatedGunsUpdate(self, handler):
        ...

class TwinShootingCoreIntegration(GunShootingCoreIntegration, ITwinShootingListenerLogic):
    ...

class TwinShootingEventsDebugger(GunShootingEventsDebugger):
    _EVENTS_DEBUG_PREFIX = 'TWIN_GUN'
