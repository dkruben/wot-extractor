# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/veh_post_progression/states.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/veh_post_progression/states.py
from __future__ import absolute_import
import typing
from account_helpers import AccountSettings
from account_helpers.AccountSettings import BECOME_ELITE_VEHICLES_WATCHED
from frameworks_common.state_machine import StateFlags
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.framework.entities.View import ViewKey
from gui.impl import backport
from gui.impl.gen import R
from gui.impl.lobby.veh_post_progression.post_progression_intro import getPostProgressionInfoWindowProc
from gui.lobby_state_machine.states import ViewLobbyState, LobbyStateDescription, SubScopeSubLayerState, SubScopeTopLayerState

def registerStates(machine):
    machine.addState(VehiclePostProgressionState())
    machine.addState(VehiclePostProgressionCmpState())


def registerTransitions(machine):
    machine.addNavigationTransitionFromParent(machine.getStateByCls(VehiclePostProgressionState))
    machine.addNavigationTransitionFromParent(machine.getStateByCls(VehiclePostProgressionCmpState))


@SubScopeSubLayerState.parentOf
class VehiclePostProgressionState(ViewLobbyState):
    STATE_ID = VIEW_ALIAS.VEH_POST_PROGRESSION
    VIEW_KEY = ViewKey(VIEW_ALIAS.VEH_POST_PROGRESSION)

    def __init__(self, flags=StateFlags.UNDEFINED):
        super(VehiclePostProgressionState, self).__init__(flags=flags)
        self.__cachedParams = {}

    def registerTransitions(self):
        from gui.impl.lobby.vehicle_hub.states import ModulesState, OverviewState, VehicleHubState
        lsm = self.getMachine()
        self.addNavigationTransition(lsm.getStateByCls(ModulesState), record=True)
        self.addNavigationTransition(lsm.getStateByCls(OverviewState), record=True)
        lsm.getStateByCls(VehicleHubState).addNavigationTransition(self)

    def serializeParams(self):
        return self.__cachedParams

    def getNavigationDescription(self):
        return LobbyStateDescription(title=backport.text(R.strings.pages.titles.vehicle_post_progression()), infos=(
         LobbyStateDescription.Info(type=LobbyStateDescription.Info.Type.INFO, onMoreInfoRequested=(lambda : getPostProgressionInfoWindowProc().show())),))

    def _onEntered(self, event):
        super(VehiclePostProgressionState, self)._onEntered(event)
        self.__cachedParams = event.params
        vehTypeCompDescr = event.params.get('intCD')
        if vehTypeCompDescr is not None:
            eliteWatchedList = AccountSettings.getSettings(BECOME_ELITE_VEHICLES_WATCHED)
            if vehTypeCompDescr not in eliteWatchedList:
                eliteWatchedList.add(vehTypeCompDescr)
                AccountSettings.setSettings(BECOME_ELITE_VEHICLES_WATCHED, eliteWatchedList)
        return

    def _onExited(self):
        super(VehiclePostProgressionState, self)._onExited()
        self.__cachedParams = {}

    def _getViewLoadCtx(self, event):
        return {'ctx': {'intCD': (event.params['intCD']), 
                   'overrideVehiclePreviewEvent': (event.params.get('overrideVehiclePreviewEvent', False)), 
                   'goToVehicleAllowed': (event.params.get('goToVehicleAllowed', False))}}


@SubScopeTopLayerState.parentOf
class VehiclePostProgressionCmpState(ViewLobbyState):
    STATE_ID = VIEW_ALIAS.VEH_POST_PROGRESSION_CMP
    VIEW_KEY = ViewKey(VIEW_ALIAS.VEH_POST_PROGRESSION_CMP)

    def __init__(self, flags=StateFlags.UNDEFINED):
        super(VehiclePostProgressionCmpState, self).__init__(flags=flags)
        self.__cachedParams = {}

    def serializeParams(self):
        return self.__cachedParams

    def getNavigationDescription(self):
        return LobbyStateDescription(title=backport.text(R.strings.pages.titles.vehicle_post_progression_cmp()))

    def _onEntered(self, event):
        super(VehiclePostProgressionCmpState, self)._onEntered(event)
        self.__cachedParams = event.params

    def _onExited(self):
        super(VehiclePostProgressionCmpState, self)._onExited()
        self.__cachedParams = {}

    def _getViewLoadCtx(self, event):
        return {'ctx': {'intCD': (event.params['intCD'])}}
