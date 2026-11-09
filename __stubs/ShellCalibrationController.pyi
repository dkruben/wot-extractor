# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/ShellCalibrationController.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from constants import SHELL_CALIBRATION_STATE as SHELL_CALIBRATION_STATE
from collections import namedtuple as namedtuple
from events_handler import eventHandler as eventHandler
from gui.shared.utils.decorators import ReprInjector as ReprInjector
from items.vehicle_mechanics_types import VehicleMechanicKey as VehicleMechanicKey, VehicleMechanicKeys as VehicleMechanicKeys
from vehicles.components.vehicle_component import VehicleDynamicComponent as VehicleDynamicComponent
from vehicles.components.vehicle_prefabs import createMechanicPrefabSpawner as createMechanicPrefabSpawner
from vehicles.mechanics.generic_mechanics.shell_calibration.mechanic_models import ShellCalibrationAmmoState as ShellCalibrationAmmoState
from vehicles.mechanics.gun_mechanics.common import IGunMechanicComponent as IGunMechanicComponent
from vehicles.mechanics.mechanic_helpers import getVehicleDescrMechanicParams as getVehicleDescrMechanicParams
from vehicles.mechanics.mechanic_states import IMechanicStatesComponent as IMechanicStatesComponent, createMechanicStatesEvents as createMechanicStatesEvents, IMechanicStatesEvents as IMechanicStatesEvents, IMechanicState as IMechanicState

# base nao representavel no stub: namedtuple(...)
# decorador original: @ReprInjector.simple(...)
class ShellCalibrationModeState(IMechanicState):
    def isTransition(self, other):
        ...
    @property
    def isPenBonusActive(self):
        ...
    @property
    def isNonPenBonusActive(self):
        ...
    @property
    def isWaitingResult(self):
        ...

class ShellCalibrationController(VehicleDynamicComponent, IGunMechanicComponent, IMechanicStatesComponent):
    __mechanicPrefabSpawner: Any
    __statesEvents: Any
    __calibrationShells: Any
    def __init__(self):
        ...
    def set_status(self, _):
        ...
    @property
    def vehicleMechanicKey(self):
        ...
    @property
    def statesEvents(self):
        ...
    def getMechanicState(self):
        ...
    # decorador original: @eventHandler
    def onCollectAmmoStates(self, ammoStates):
        ...
    def onDestroy(self):
        ...
    def _onAppearanceReady(self):
        ...
    def _onComponentAppearanceUpdate(self, **kwargs):
        ...
    def _onComponentAvatarUpdate(self, player):
        ...
    def _collectComponentParams(self, typeDescriptor):
        ...
