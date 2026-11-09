# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/profile/states.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/profile/states.py
from __future__ import absolute_import
import typing
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.framework.entities.View import ViewKey
from gui.impl import backport
from gui.impl.gen import R
from gui.lobby_state_machine.states import SFViewLobbyState, SubScopeSubLayerState, LobbyStateDescription
from helpers import dependency
from skeletons.gui.app_loader import IAppLoader
if typing.TYPE_CHECKING:
    from gui.Scaleform.daapi.view.lobby.profile.ProfilePage import ProfilePage

def registerStates(machine):
    machine.addState(ServiceRecordState())


def registerTransitions(machine):
    machine.addNavigationTransitionFromParent(machine.getStateByCls(ServiceRecordState))


@SubScopeSubLayerState.parentOf
class ServiceRecordState(SFViewLobbyState):
    STATE_ID = VIEW_ALIAS.LOBBY_PROFILE
    VIEW_KEY = ViewKey(VIEW_ALIAS.LOBBY_PROFILE)
    __appLoader = dependency.descriptor(IAppLoader)

    def registerTransitions(self):
        from gui.impl.lobby.vehicle_hub import OverviewState, ModulesState
        from gui.impl.lobby.collection.states import CollectionState
        from gui.Scaleform.daapi.view.lobby.store.browser.states import ShopState
        lsm = self.getMachine()
        self.addNavigationTransition(lsm.getStateByCls(OverviewState), record=True)
        self.addNavigationTransition(lsm.getStateByCls(ModulesState), record=True)
        self.addNavigationTransition(lsm.getStateByCls(CollectionState), record=True)
        self.addNavigationTransition(lsm.getStateByCls(ShopState), record=True)

    def serializeParams(self):
        view = self.getMachine().getRelatedView(self)
        tabId = view.tabId
        if tabId:
            return {'ctx': {'selectedAlias': tabId}}
        return {}

    def getNavigationDescription(self):
        return LobbyStateDescription(title=backport.text(R.strings.pages.titles.service_record()))
