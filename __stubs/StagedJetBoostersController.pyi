# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/StagedJetBoostersController.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
import BigWorld as BigWorld
from CommandMapping import CMD_CM_SPECIAL_ABILITY as CMD_CM_SPECIAL_ABILITY, CMD_CM_VEHICLE_SWITCH_AUTOROTATION as CMD_CM_VEHICLE_SWITCH_AUTOROTATION
from cgf_components_common.vehicle_mechanics.staged_jet_boosters import StagedJetBoostersControllerDescriptor as StagedJetBoostersControllerDescriptor
from cgf_script.registration import registerReplicableComponent as registerReplicableComponent
from constants import PHASED_MECHANIC_STATE as PHASED_MECHANIC_STATE, IS_CLIENT as IS_CLIENT, AcceleratorStatus as AcceleratorStatus
from gui.shared.utils.decorators import ReprInjector as ReprInjector
from items.components.shared_components import StagedJetBoostersParams as StagedJetBoostersParams
from items.vehicle_mechanics_types import VehicleMechanicKey as VehicleMechanicKey, VehicleMechanicKeys as VehicleMechanicKeys
from shared_utils import skipInEditor as skipInEditor
from vehicles.components.component_wrappers import ifPlayerVehicle as ifPlayerVehicle
from vehicles.components.vehicle_component import VehicleDynamicComponent as VehicleDynamicComponent
from vehicles.mechanics.common import IMechanicComponent as IMechanicComponent
from vehicles.mechanics.mechanic_commands import createMechanicCommandsEvents as createMechanicCommandsEvents, IMechanicCommandsEvents as IMechanicCommandsEvents, IMechanicCommandsComponent as IMechanicCommandsComponent
from vehicles.mechanics.mechanic_constants import VehicleMechanicCommand as VehicleMechanicCommand
from vehicles.mechanics.mechanic_helpers import getVehicleDescrMechanicParams as getVehicleDescrMechanicParams
from vehicles.mechanics.mechanic_logging import createMechanicInputLogger as createMechanicInputLogger, IMechanicInputLoggingComponent as IMechanicInputLoggingComponent
from vehicles.mechanics.mechanic_states import IMechanicStatesComponent as IMechanicStatesComponent, createMechanicStatesEvents as createMechanicStatesEvents, IMechanicStatesEvents as IMechanicStatesEvents, IMechanicState as IMechanicState
from wotdecorators import noexcept as noexcept
import Input as Input
from Input import TriggerEvent as TriggerEvent
from vehicles.mechanics.mechanic_inputs.mechanic_input_profile import PlayerVehicleInputPredicate as PlayerVehicleInputPredicate
_logger: Any

# base nao representavel no stub: typing.NamedTuple(...)
# decorador original: @ReprInjector.simple(...)
class StagedJetBoostersState(IMechanicState):
    @classmethod
    def fromComponentStatus(cls, status, acceleratorStatus, params):
        ...
    @property
    def progress(self):
        ...
    @property
    def timeLeft(self):
        ...
    def isTransition(self, other):
        ...

# decorador original: @registerReplicableComponent
class StagedJetBoostersController(VehicleDynamicComponent, StagedJetBoostersControllerDescriptor, IMechanicComponent, IMechanicCommandsComponent, IMechanicStatesComponent, IMechanicInputLoggingComponent):
    _INPUT_ACTION_NAME = 'ABILITY_0_INPUT_ACTION'
    _INPUT_PROFILE_NAME = 'ABILITY_0_INPUT_PROFILE'
    __params: Any
    __currentState: Any
    __commandsEvents: Any
    __statesEvents: Any
    __mechanicInputLogger: Any
    # decorador original: @skipInEditor
    def __init__(self):
        ...
    @property
    def vehicleMechanicKey(self):
        ...
    @property
    def commandsEvents(self):
        ...
    @property
    def statesEvents(self):
        ...
    # decorador original: @ifPlayerVehicle
    def attachInput(self, *_, **__):
        ...
    # decorador original: @ifPlayerVehicle
    def detachInput(self, *_, **__):
        ...
    # decorador original: @ifPlayerVehicle
    def createInputLogger(self, *_, **__):
        ...
    def getMechanicLogState(self):
        ...
    def getMechanicState(self):
        ...
    def tryActivate(self):
        ...
    # decorador original: @noexcept
    def set_stateStatus(self, _=None):
        ...
    # decorador original: @noexcept
    def set_acceleratorStatus(self, prev=None):
        ...
    def onDestroy(self):
        ...
    def _onAppearanceReady(self):
        ...
    def _collectComponentParams(self, typeDescriptor):
        ...
    def _onComponentAppearanceUpdate(self, **kwargs):
        ...
    def __updateMechanicState(self):
        ...
