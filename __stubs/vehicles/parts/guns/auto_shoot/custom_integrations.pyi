# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicles/parts/guns/auto_shoot/custom_integrations.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import TriggersManager as TriggersManager
from events_handler import eventHandler as eventHandler
from TriggersManager import TRIGGER_TYPE as TRIGGER_TYPE
from vehicles.components.component_wrappers import ifPlayerVehicle as ifPlayerVehicle
from vehicles.parts.guns.common import GunShootingCustomIntegrations as GunShootingCustomIntegrations
from vehicles.parts.guns.auto_shoot.guns_interfaces import IAutoShootingListenerLogic as IAutoShootingListenerLogic
from vehicle_systems.shake_helpers import shakePlayerDynamicCamera as shakePlayerDynamicCamera
from vehicle_systems.shooting_helpers import notifyArenaVehicleShot as notifyArenaVehicleShot
_logger: Any

class AutoShootCustomIntegrations(GunShootingCustomIntegrations, IAutoShootingListenerLogic):
    # decorador original: @eventHandler
    def onContinuousBurstActivation(self):
        ...
    # decorador original: @eventHandler
    def onContinuousBurstDeactivation(self):
        ...
    # decorador original: @eventHandler
    def onContinuousBurstUpdate(self):
        ...
    # decorador original: @ifPlayerVehicle
    def __processAvatarContinuousActivation(self, _=None):
        ...
    # decorador original: @ifPlayerVehicle
    def __processAvatarContinuousDeactivation(self, _=None):
        ...
