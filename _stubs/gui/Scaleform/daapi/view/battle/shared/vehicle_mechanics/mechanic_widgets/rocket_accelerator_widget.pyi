# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/vehicle_mechanics/mechanic_widgets/rocket_accelerator_widget.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from gui.Scaleform.daapi.view.meta.RocketAcceleratorIndicatorMeta import RocketAcceleratorIndicatorMeta as RocketAcceleratorIndicatorMeta
from gui.veh_mechanics.battle.updaters.mechanics.mechanic_passenger_updater import VehicleMechanicPassengerUpdater as VehicleMechanicPassengerUpdater
from gui.veh_mechanics.battle.updaters.mechanics.rocket_accelerator_updater import IRocketAcceleratorView as IRocketAcceleratorView, RocketAcceleratorUpdater as RocketAcceleratorUpdater
from items.vehicle_mechanics_types import VehicleMechanicKeys as VehicleMechanicKeys
from gui.veh_mechanics.battle.updaters.updaters_common import IViewUpdater as IViewUpdater

class RocketAcceleratorMechanicIndicator(RocketAcceleratorIndicatorMeta, IRocketAcceleratorView):
    def setCount(self, count):
        ...
    def setProgress(self, progress):
        ...
    def setState(self, state, isInstantly=False):
        ...
    def setTime(self, time):
        ...
    def _getViewUpdaters(self):
        ...
