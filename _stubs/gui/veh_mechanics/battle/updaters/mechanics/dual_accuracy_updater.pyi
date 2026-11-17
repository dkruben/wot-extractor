# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/veh_mechanics/battle/updaters/mechanics/dual_accuracy_updater.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from events_handler import eventHandler as eventHandler
from gui.veh_mechanics.battle.updaters.mechanics.mechanics_common import VehicleMechanicUpdater as VehicleMechanicUpdater
from items.vehicle_mechanics_types import VehicleMechanicKeys as VehicleMechanicKeys
from DualAccuracy import DualAccuracy as DualAccuracy

class IDualAccuracyView(object):
    def setDualAccuracyState(self, isActive):
        ...

class DualAccuracyUpdater(VehicleMechanicUpdater):
    __dualAccuracyComponent: Any
    def __init__(self, view):
        ...
    # decorador original: @eventHandler
    def onMechanicComponentCatching(self, component):
        ...
    # decorador original: @eventHandler
    def onMechanicComponentReleasing(self, component):
        ...
    def destroy(self):
        ...
    def __onSetDualAccState(self, isActive):
        ...
