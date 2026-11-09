# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/maps_blacklist/states.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/maps_blacklist/states.py
import typing
from gui.Scaleform.framework import ScopeTemplates
from gui.Scaleform.framework.entities.View import ViewKey
from gui.impl import backport
from gui.impl.lobby.maps_blacklist.maps_blacklist_view import MapsBlacklistView
from gui.lobby_state_machine.states import GuiImplViewLobbyState, SubScopeTopLayerState, LobbyStateDescription
from gui.impl.gen import R
if typing.TYPE_CHECKING:
    from gui.lobby_state_machine.lobby_state_machine import LobbyStateMachine

def registerStates(machine):
    machine.addState(MapsBlacklistState())


def registerTransitions(machine):
    state = machine.getStateByCls(MapsBlacklistState)
    machine.addNavigationTransitionFromParent(state)


@SubScopeTopLayerState.parentOf
class MapsBlacklistState(GuiImplViewLobbyState):
    STATE_ID = 'mapsBlacklist'
    VIEW_KEY = ViewKey(R.views.lobby.excluded_maps.ExcludedMapsView())

    def __init__(self):
        super(MapsBlacklistState, self).__init__(MapsBlacklistView, scope=ScopeTemplates.LOBBY_SUB_SCOPE)

    def getNavigationDescription(self):
        return LobbyStateDescription(title=backport.text(R.strings.pages.titles.maps_blacklist()))
