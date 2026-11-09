# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/blueprints/states.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/blueprints/states.py
import typing
from gui.Scaleform.framework import ScopeTemplates
from gui.Scaleform.framework.entities.View import ViewKey
from gui.impl import backport
from gui.lobby_state_machine.states import GuiImplViewLobbyState, SubScopeSubLayerState, LobbyStateDescription
from gui.impl.gen import R

def registerStates(machine):
    machine.addState(BlueprintState())


def registerTransitions(machine):
    blueprint = machine.getStateByCls(BlueprintState)
    machine.addNavigationTransitionFromParent(blueprint)


@SubScopeSubLayerState.parentOf
class BlueprintState(GuiImplViewLobbyState):
    STATE_ID = 'blueprint'
    VIEW_KEY = ViewKey(R.views.lobby.blueprints.blueprint_screen.blueprint_screen.BlueprintScreen())

    def __init__(self):
        from gui.impl.lobby.blueprints.blueprint_screen import BlueprintScreen
        super(BlueprintState, self).__init__(BlueprintScreen, ScopeTemplates.LOBBY_SUB_SCOPE)
        self._cachedParams = None
        return

    def _getViewLoadCtx(self, event):
        return {'ctx': {'vehicleCD': (event.params['vehicleCD'])}}

    def _onEntered(self, event):
        self._cachedParams = event.params
        super(BlueprintState, self)._onEntered(event)

    def serializeParams(self):
        return self._cachedParams

    def getNavigationDescription(self):
        return LobbyStateDescription(title=backport.text(R.strings.pages.titles.blueprints()))
