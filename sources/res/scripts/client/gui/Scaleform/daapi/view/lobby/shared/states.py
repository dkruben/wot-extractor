# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/shared/states.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/shared/states.py
from __future__ import absolute_import
from frameworks_common.state_machine import StateFlags
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.framework.entities.View import ViewKey
from gui.lobby_state_machine.states import SFViewLobbyState, SubScopeTopLayerState

def registerStates(machine):
    machine.addState(BrowserLobbyTopState())


def registerTransitions(machine):
    browser = machine.getStateByCls(BrowserLobbyTopState)
    machine.addNavigationTransitionFromParent(browser)


@SubScopeTopLayerState.parentOf
class BrowserLobbyTopState(SFViewLobbyState):
    STATE_ID = 'browser'
    VIEW_KEY = ViewKey(VIEW_ALIAS.BROWSER_LOBBY_TOP_SUB)

    def __init__(self, flags=StateFlags.UNDEFINED):
        super(BrowserLobbyTopState, self).__init__(flags=flags)
        self.__cachedParams = {}

    @classmethod
    def goTo(cls, ctx):
        super(BrowserLobbyTopState, cls).goTo(ctx=ctx)

    def serializeParams(self):
        return self.__cachedParams

    def _onEntered(self, event):
        self.__cachedParams = event.params
        super(BrowserLobbyTopState, self)._onEntered(event)

    def _getViewLoadCtx(self, event):
        ctx = event.params.get('ctx')
        return {'ctx': {'url': (ctx.get('url')), 
                   'allowRightClick': (ctx.get('allowRightClick', False)), 
                   'callbackOnLoad': (ctx.get('callbackOnLoad')), 
                   'callbackOnClose': (ctx.get('callbackOnClose')), 
                   'webHandlers': (ctx.get('webHandlers')), 
                   'forcedSkipEscape': (ctx.get('forcedSkipEscape')), 
                   'browserParams': (ctx.get('browserParams', {})), 
                   'hiddenLayers': (ctx.get('hiddenLayers', ()))}}
