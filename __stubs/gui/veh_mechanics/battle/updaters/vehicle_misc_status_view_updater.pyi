# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/veh_mechanics/battle/updaters/vehicle_misc_status_view_updater.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE as VEHICLE_VIEW_STATE, DestroyTimerViewState as DestroyTimerViewState
from gui.veh_mechanics.battle.updaters.updaters_common import ViewUpdater as ViewUpdater
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
MISC_STATUS_LEVEL_CRITICAL = 'critical'
MISC_STATUS_LEVEL_WARNING = 'warning'
MISC_STATUSES_ORDER: tuple

class IVehicleMiscStatusView(object):
    def vehicleMiscStatusChanged(self, miscStatuses):
        ...

class _ObservableMiscStatuses(object):
    __observed: Any
    __miscStatuses: Any
    def __init__(self, observed):
        ...
    @property
    def statuses(self):
        ...
    @property
    def hasNegativeEffect(self):
        ...
    def addStatus(self, code, level):
        ...
    def updateStatus(self, code, level):
        ...
    def clear(self):
        ...

class VehicleMiscStatusUpdater(ViewUpdater):
    __sessionProvider: Any
    __miscStatuses: Any
    def __init__(self, observed, view):
        ...
    def initialize(self):
        ...
    def finalize(self):
        ...
    def __onVehicleStateUpdated(self, stateID, value):
        ...
