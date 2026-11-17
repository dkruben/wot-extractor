# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/veh_mechanics/battle/updaters/mechanics/rocket_accelerator_updater.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import BigWorld as BigWorld
from constants import ROCKET_ACCELERATION_STATE as ROCKET_ACCELERATION_STATE
from events_handler import eventHandler as eventHandler
from gui.Scaleform.genConsts.MECHANICS_WIDGET_CONST import MECHANICS_WIDGET_CONST as MECHANICS_WIDGET_CONST
from gui.shared.utils.TimeInterval import TimeInterval as TimeInterval
from gui.veh_mechanics.battle.updaters.mechanics.mechanics_common import VehicleMechanicUpdater as VehicleMechanicUpdater
from items.vehicle_mechanics_types import VehicleMechanicKeys as VehicleMechanicKeys
from RocketAccelerationController import RocketAccelerationController as RocketAccelerationController
UI_ROCKET_STATE_MAP: dict

class IRocketAcceleratorView(object):
    def setCount(self, count):
        ...
    def setProgress(self, progress):
        ...
    def setState(self, state, isInstantly=False):
        ...
    def setTime(self, time):
        ...

class RocketAcceleratorUpdater(VehicleMechanicUpdater):
    __timeInterval: Any
    __rocketComponent: Any
    def __init__(self, view):
        ...
    # decorador original: @eventHandler
    def onMechanicComponentCatching(self, component):
        ...
    # decorador original: @eventHandler
    def onMechanicComponentReleasing(self, component):
        ...
    def finalize(self):
        ...
    def destroy(self):
        ...
    def _updateProgress(self):
        ...
    def __onRocketAcceleratorStateChanged(self, stateStatus, isInitial=False):
        ...
