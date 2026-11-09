# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/AvatarInputHandler/player_notifications/siege_mode/notifier.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from Event import Event as Event
from items.vehicle_mechanics_types import VehicleMechanicKeys as VehicleMechanicKeys
from AvatarInputHandler.player_notifications.siege_mode.sound_notifications import SiegeModeSoundNotifications as SiegeModeSoundNotifications, TurboshaftModeSoundNotifications as TurboshaftModeSoundNotifications, TwinGunModeSoundNotifications as TwinGunModeSoundNotifications, PillboxSiegeSoundNotifications as PillboxSiegeSoundNotifications
from AvatarInputHandler.player_notifications.siege_mode.camera_shaker import SiegeModeCameraShaker as SiegeModeCameraShaker
from vehicles.mechanics.mechanic_helpers import hasVehicleDescrMechanic as hasVehicleDescrMechanic

class SiegeModeNotifier(object):
    onSiegeStateChanged: Any
    soundNotifications: Any
    def __init__(self):
        ...
    def destroy(self):
        ...
    def construct(self, vehicle):
        ...
    def start(self):
        ...
    def stop(self):
        ...
    def notifySiegeModeChanged(self, vehicleID, newState, timeToNextMode):
        ...
    @staticmethod
    def _getSoundNotifications(typeDescr):
        ...
