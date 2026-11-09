# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/missions/regular/states.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/missions/regular/states.py
from __future__ import absolute_import
from frameworks_common.state_machine.transitions import TransitionType
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.framework.entities.View import ViewKey
from gui.impl import backport
from gui.impl.gen import R
from gui.lobby_state_machine.states import SubScopeSubLayerState, ViewLobbyState, LobbyStateDescription
from gui.shared.event_dispatcher import showHangar
from helpers import dependency
from skeletons.gui.app_loader import IAppLoader
from skeletons.gui.battle_matters import IBattleMattersController

def registerStates(machine):
    machine.addState(MissionsState())


def registerTransitions(machine):
    machine.addNavigationTransitionFromParent(machine.getStateByCls(MissionsState))


@SubScopeSubLayerState.parentOf
class MissionsState(ViewLobbyState):
    STATE_ID = 'missions'
    VIEW_KEY = ViewKey(VIEW_ALIAS.LOBBY_MISSIONS)
    __appLoader = dependency.descriptor(IAppLoader)
    __battleMattersController = dependency.descriptor(IBattleMattersController)

    def registerTransitions(self):
        from gui.impl.lobby.vehicle_hub import OverviewState
        from gui.Scaleform.daapi.view.lobby.store.browser.states import ShopState
        lsm = self.getMachine()
        self.addNavigationTransition(lsm.getStateByCls(OverviewState), record=True)
        self.addNavigationTransition(lsm.getStateByCls(ShopState), record=True)
        self.addNavigationTransition(self, transitionType=TransitionType.EXTERNAL)

    def getNavigationDescription(self):
        return LobbyStateDescription(title=backport.text(R.strings.pages.titles.userMissions()))

    def serializeParams(self):
        ctx = {}
        app = self.__appLoader.getApp()
        view = app.containerManager.getViewByKey(self.getViewKey())
        if view:
            ctx['tab'] = view.getCurrentTabAlias()
        return {'ctx': ctx}

    def _onEntered(self, event):
        if not self.__battleMattersController.isEnabled():
            showHangar()
        else:
            super(MissionsState, self)._onEntered(event)
