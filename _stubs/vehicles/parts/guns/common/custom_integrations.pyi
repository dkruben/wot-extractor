# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicles/parts/guns/common/custom_integrations.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
import weakref as weakref
import TriggersManager as TriggersManager
from aih_constants import ShakeReason as ShakeReason
from events_containers.common.containers import ContainersListener as ContainersListener
from events_handler import eventHandler as eventHandler
from TriggersManager import TRIGGER_TYPE as TRIGGER_TYPE
from vehicles.components.component_wrappers import ifAppearanceReady as ifAppearanceReady, ifPlayerVehicle as ifPlayerVehicle
from vehicles.parts.guns.common.guns_interfaces import IGunShootingListenerLogic as IGunShootingListenerLogic
from vehicle_systems.shake_helpers import shakeMultiGunPlayerDynamicCamera as shakeMultiGunPlayerDynamicCamera, shakeMultiGunsPlayerDynamicCamera as shakeMultiGunsPlayerDynamicCamera
from vehicle_systems.shooting_helpers import processVehicleDiscreteShots as processVehicleDiscreteShots
from Avatar import PlayerAvatar as PlayerAvatar
from Vehicle import Vehicle as Vehicle
from vehicles.parts.guns.common import IGunComponent as IGunComponent, IGunShootingEvents as IGunShootingEvents
_logger: Any

class GunShootingCustomIntegrations(ContainersListener, IGunShootingListenerLogic):
    _vehicle: Any
    _component: Any
    _gunInstallationSlot: Any
    def __init__(self, vehicle, component):
        ...
    def isAppearanceReady(self):
        ...
    def isPlayerVehicle(self, player):
        ...
    def isObservedVehicle(self, player, vehicle):
        ...
    # decorador original: @eventHandler
    def onEventsContainerDestroy(self, events):
        ...
    # decorador original: @eventHandler
    def onAppearanceReady(self):
        ...
    # decorador original: @eventHandler
    # decorador original: @ifAppearanceReady
    def onDiscreteShot(self, gunIndex):
        ...
    # decorador original: @eventHandler
    # decorador original: @ifAppearanceReady
    def onMultiShot(self, gunIndexes):
        ...
    # decorador original: @ifPlayerVehicle
    def _processAvatarSingleDiscreteShot(self, _=None):
        ...
