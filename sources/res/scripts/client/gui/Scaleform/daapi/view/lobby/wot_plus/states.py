# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/wot_plus/states.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/wot_plus/states.py
from __future__ import absolute_import
import typing
from gui.impl import backport
from gui.impl.gen import R
from gui.lobby_state_machine.states import SFViewLobbyState, TopScopeTopLayerState, LobbyStateDescription
from gui.Scaleform.framework.entities.View import ViewKey
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS

def registerStates(machine):
    machine.addState(WotPlusInfoState())


def registerTransitions(_):
    pass


@TopScopeTopLayerState.parentOf
class WotPlusInfoState(SFViewLobbyState):
    STATE_ID = 'wotPlusInfo'
    VIEW_KEY = ViewKey(VIEW_ALIAS.WOT_PLUS_INFO_VIEW)

    def registerTransitions(self):
        lsm = self.getMachine()
        lsm.addNavigationTransitionFromParent(self)

    def getNavigationDescription(self):
        return LobbyStateDescription(backport.text(R.strings.pages.titles.browser.wotplus_info()))
