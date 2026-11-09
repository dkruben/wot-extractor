# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicles/parts/guns/auto_shoot/shooting_events.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import BigWorld as BigWorld
import math_utils as math_utils
from cgf_events import gun_events as gun_events
from constants import SERVER_TICK_LENGTH as SERVER_TICK_LENGTH
from events_handler import eventHandler as eventHandler
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
from vehicles.parts.guns.auto_shoot.guns_interfaces import IAutoShootingEventsLogic as IAutoShootingEventsLogic, IAutoShootingListenerLogic as IAutoShootingListenerLogic
from vehicles.parts.guns.common import GunShootingEvents as GunShootingEvents, GunShootingCoreIntegration as GunShootingCoreIntegration, GunShootingEventsDebugger as GunShootingEventsDebugger
from vehicles.parts.guns.auto_shoot.guns_interfaces import IAutoShootGunComponent as IAutoShootGunComponent, IAutoShootGunComponentState as IAutoShootGunComponentState
CONTINUOUS_ACTIVATION_DELTA = 0.0

class AutoShootingEvents(GunShootingEvents, IAutoShootingEventsLogic):
    __componentState: Any
    __lastDiscreteShotTime: Any
    __callbackDelayer: Any
    onBurstActivation: Any
    onContinuousBurstActivation: Any
    onShotRateUpdate: Any
    onBurstDeactivation: Any
    onContinuousBurstDeactivation: Any
    onContinuousBurstUpdate: Any
    def __init__(self, component):
        ...
    def destroy(self):
        ...
    def processAppearanceReady(self):
        ...
    def processDiscreteShot(self, gunIndex):
        ...
    def updateAutoShootingState(self, componentState):
        ...
    def _createCoreIntegration(self):
        ...
    def _createEventsDebugger(self):
        ...
    def _lateSubscribe(self, listener):
        ...
    def __activateBurst(self, isContinuousBurst):
        ...
    def __activateContinuousBurst(self):
        ...
    def __deactivateBurst(self, isContinuousInProgress):
        ...
    def __deactivateContinuousBurst(self):
        ...
    def __destroyBurst(self):
        ...
    def __switchBurstPhase(self, isContinuousBurst):
        ...
    def __updateContinuousBurst(self):
        ...
    def __needDelayContinuousBurst(self):
        ...
    def __tryActivateContinuousBurst(self):
        ...
    def __lateBurstActivation(self, handler):
        ...
    def __lateContinuousBurstActivation(self, handler):
        ...
    def __lateShotRateUpdate(self, handler):
        ...

class AutoShootingCoreIntegration(GunShootingCoreIntegration, IAutoShootingListenerLogic):
    # decorador original: @eventHandler
    def onContinuousBurstActivation(self):
        ...
    # decorador original: @eventHandler
    def onContinuousBurstDeactivation(self):
        ...
    # decorador original: @eventHandler
    def onShotRateUpdate(self, rate):
        ...

class AutoShootingEventsDebugger(GunShootingEventsDebugger):
    IGNORED_EVENTS: Any
    _EVENTS_DEBUG_PREFIX = 'AUTO_GUN'
