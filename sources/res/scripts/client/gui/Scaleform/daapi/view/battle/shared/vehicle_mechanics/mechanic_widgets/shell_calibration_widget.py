# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/vehicle_mechanics/mechanic_widgets/shell_calibration_widget.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/shared/vehicle_mechanics/mechanic_widgets/shell_calibration_widget.py
from __future__ import absolute_import
import typing
from ShellCalibrationController import ShellCalibrationModeState
from events_containers.common.containers import ContainersListener
from events_handler import eventHandler
from gui.Scaleform.daapi.view.battle.shared.vehicle_mechanics.mechanic_widgets.vehicle_mechanic_widget import VehicleMechanicWidget
from gui.Scaleform.genConsts.SHELL_CALIBRATION_WIDGET_CONSTS import SHELL_CALIBRATION_WIDGET_CONSTS
from gui.veh_mechanics.battle.updaters.mechanics.mechanic_passenger_updater import VehicleMechanicPassengerUpdater
from gui.veh_mechanics.battle.updaters.mechanics.mechanic_states_updater import VehicleMechanicStatesUpdater
from items.vehicle_mechanics_types import VehicleMechanicKeys
from vehicles.mechanics.mechanic_states import IMechanicStatesListenerLogic
if typing.TYPE_CHECKING:
    from gui.veh_mechanics.battle.updaters.updaters_common import IViewUpdater

class ShellCalibrationMechanicWidget(VehicleMechanicWidget, ContainersListener, IMechanicStatesListenerLogic):

    @eventHandler
    def onStatePrepared(self, state):
        self.__invalidateState(state, isInstantly=True)

    @eventHandler
    def onStateTransition(self, prevState, newState):
        self.__invalidateState(newState)

    def _getViewUpdaters(self):
        return [
         VehicleMechanicPassengerUpdater(VehicleMechanicKeys.SHELL_CALIBRATION, self),
         VehicleMechanicStatesUpdater(VehicleMechanicKeys.SHELL_CALIBRATION, self)]

    def __invalidateState(self, state, isInstantly=False):
        widgetState = SHELL_CALIBRATION_WIDGET_CONSTS.NO_BONUS
        if state.isPenBonusActive:
            widgetState = SHELL_CALIBRATION_WIDGET_CONSTS.DAMAGE_BONUS
        elif state.isNonPenBonusActive:
            widgetState = SHELL_CALIBRATION_WIDGET_CONSTS.PENETRATION_BONUS
        self.as_setStateS(widgetState, isInstantly)
