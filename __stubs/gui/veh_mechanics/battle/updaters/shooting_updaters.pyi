# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/veh_mechanics/battle/updaters/shooting_updaters.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from gui.battle_control.controllers.vehicle_passenger import hasVehiclePassengerCtrl as hasVehiclePassengerCtrl, VehiclePassengerInfoWatcher as VehiclePassengerInfoWatcher
from gui.veh_mechanics.battle.updaters.updaters_common import ViewUpdater as ViewUpdater
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from items.components.gun_installation_components import GunInstallationSlot as GunInstallationSlot

class IShootingReactionsView(object):
    def onDiscreteShotsDone(self, gunInstallationSlot, isCurrentVehicle):
        ...

class ShootingReactionsUpdater(ViewUpdater, VehiclePassengerInfoWatcher):
    __sessionProvider: Any
    def initialize(self):
        ...
    def finalize(self):
        ...
    # decorador original: @hasVehiclePassengerCtrl(...)
    def __onDiscreteShotsDone(self, entityID, gunInstallationSlot, passengerCtrl=None):
        ...
