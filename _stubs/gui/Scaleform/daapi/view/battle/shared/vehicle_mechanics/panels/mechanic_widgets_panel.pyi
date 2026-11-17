# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/vehicle_mechanics/panels/mechanic_widgets_panel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from gui.Scaleform.daapi.view.meta.WidgetsPanelMeta import WidgetsPanelMeta as WidgetsPanelMeta
from gui.Scaleform.genConsts.BATTLE_WIDGETS_CONSTS import BATTLE_WIDGETS_CONSTS as BATTLE_WIDGETS_CONSTS
from gui.battle_control.controllers.vehicle_passenger import hasVehiclePassengerCtrl as hasVehiclePassengerCtrl, VehiclePassengerInfoWatcher as VehiclePassengerInfoWatcher
from items.vehicle_mechanics_types import VehicleMechanicKeys as VehicleMechanicKeys

class MechanicWidgetsPanel(WidgetsPanelMeta, VehiclePassengerInfoWatcher):
    _VEHICLE_MECHANIC_UI_COMPONENTS_MAP: dict
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _setIsReplay(self, isReplay):
        ...
    def _setIsVisible(self, isVisible):
        ...
    def _setCrosshairScaledPosition(self, position):
        ...
    def _setCrosshairViewID(self, viewID):
        ...
    def _addMechanicUIComponents(self, mechanicComponents):
        ...
    # decorador original: @hasVehiclePassengerCtrl(...)
    def __onVehicleControlling(self, _, passengerCtrl=None):
        ...
