# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/battle/shared/clip/shell_calibration_clip_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from events_containers.common.containers.interfaces import IClientEventsContainerListener as IClientEventsContainerListener
from events_handler import eventHandler as eventHandler, subscribeToEvents as subscribeToEvents, unsubscribeFromEvents as unsubscribeFromEvents
from gui.battle_control.battle_constants import SHELL_QUANTITY_UNKNOWN as SHELL_QUANTITY_UNKNOWN, SHELL_SET_RESULT as SHELL_SET_RESULT
from gui.impl.gen.view_models.views.battle.shared.clip.shell_calibration_clip_model import ClipState as ClipState, ShellCalibrationClipModel as ShellCalibrationClipModel
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.veh_mechanics.battle.updaters.mechanics.mechanic_states_updater import VehicleMechanicStatesUpdater as VehicleMechanicStatesUpdater
from helpers import dependency as dependency
from items.vehicle_mechanics_types import VehicleMechanicKeys as VehicleMechanicKeys
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from vehicles.mechanics.mechanic_states import IMechanicStatesListenerLogic as IMechanicStatesListenerLogic
from vehicles.mechanics.mechanic_trackers import IVehicleMechanicsTrackerListenerLogic as IVehicleMechanicsTrackerListenerLogic
from gui.battle_control.controllers.consumables.ammo_ctrl import _GunSettings as _GunSettings
from ShellCalibrationController import ShellCalibrationController as ShellCalibrationController, ShellCalibrationModeState as ShellCalibrationModeState
_logger: Any

class ShellCalibrationClipPresenter(ViewComponent, IClientEventsContainerListener, IMechanicStatesListenerLogic, IVehicleMechanicsTrackerListenerLogic):
    __sessionProvider: Any
    __clipCapacity: Any
    __statesUpdater: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def subscribeTo(self, events):
        ...
    def unsubscribeFrom(self, events):
        ...
    def lateSubscribeTo(self, events):
        ...
    # decorador original: @eventHandler
    def onEventsContainerDestroy(self, events):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _getEvents(self):
        ...
    # decorador original: @eventHandler
    def onMechanicComponentCatching(self, component):
        ...
    # decorador original: @eventHandler
    def onMechanicComponentReleasing(self, component):
        ...
    # decorador original: @eventHandler
    def onStatePrepared(self, state):
        ...
    # decorador original: @eventHandler
    def onStateTransition(self, prevState, newState):
        ...
    # decorador original: @eventHandler
    def onStateObservation(self, state):
        ...
    def __onGunSettingsSet(self, gunSettings):
        ...
    def __onShellsUpdated(self, intCD, quantity, quantityInClip, result):
        ...
    def __onCurrentShellChanged(self, intCD):
        ...
    def __onCurrentShellReset(self):
        ...
    def __applyGunSettings(self, gunSettings):
        ...
    def __computeClipState(self, quantityInClip):
        ...
    def __applyAmmoStock(self, quantity, quantityInClip, clipState):
        ...
    def __applyCalibrationState(self, state):
        ...
    def __resetCalibrationState(self):
        ...
