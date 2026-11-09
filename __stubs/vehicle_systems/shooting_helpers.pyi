# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicle_systems/shooting_helpers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
import BigWorld as BigWorld
from cgf_events import gun_events as gun_events
from constants import IS_CLIENT as IS_CLIENT, DEFAULT_GUN_INDEX as DEFAULT_GUN_INDEX
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from vehicle_systems.instant_status_helpers import invokeShotsDoneStatus as invokeShotsDoneStatus
from items.components.gun_installation_components import GunInstallationSlot as GunInstallationSlot
from Vehicle import Vehicle as Vehicle

def processVehicleSingleShot(vehicle, gunInstallationSlot, gunIndex=...):
    ...
def processVehicleMultiShot(vehicle, gunInstallationSlot, gunIndexes):
    ...
def processVehicleDiscreteShots(vehicle, gunInstallationSlot):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def notifyVehicleDiscreteShots(vehicle, gunInstallationSlot, sessionProvider=None):
    ...
def notifyArenaVehicleShot(vehicle):
    ...
