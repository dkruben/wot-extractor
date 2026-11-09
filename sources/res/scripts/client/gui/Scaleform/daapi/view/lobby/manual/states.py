# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/manual/states.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/manual/states.py
from __future__ import absolute_import
import typing
from frameworks_common.state_machine import StateFlags
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.framework.entities.View import ViewKey
from gui.impl import backport
from gui.impl.gen import R
from gui.lobby_state_machine.states import ViewLobbyState, SubScopeTopLayerState, LobbyStateDescription
if typing.TYPE_CHECKING:
    from gui.Scaleform.daapi.view.lobby.manual.manual_chapter_view import ManualChapterView

def registerStates(machine):
    machine.addState(ManualState())
    machine.addState(ManualChapterState())


def registerTransitions(machine):
    pass


@SubScopeTopLayerState.parentOf
class ManualState(ViewLobbyState):
    STATE_ID = VIEW_ALIAS.WIKI_VIEW
    VIEW_KEY = ViewKey(VIEW_ALIAS.WIKI_VIEW)

    @classmethod
    def goTo(cls, chapterIndex=None, pageIndex=None):
        super(ManualState, cls).goTo(chapterIndex=chapterIndex, pageIndex=pageIndex)

    def compareParams(self, params, otherParams):
        return True

    def registerTransitions(self):
        lsm = self.getMachine()
        lsm.addNavigationTransitionFromParent(self)

    def getNavigationDescription(self):
        return LobbyStateDescription(title=backport.text(R.strings.menu.headerButtons.wiki()))

    def _getViewLoadCtx(self, event):
        return {'ctx': (event.params)}


@SubScopeTopLayerState.parentOf
class ManualChapterState(ViewLobbyState):
    STATE_ID = VIEW_ALIAS.MANUAL_CHAPTER_VIEW
    VIEW_KEY = ViewKey(VIEW_ALIAS.MANUAL_CHAPTER_VIEW)

    def __init__(self, flags=StateFlags.UNDEFINED):
        super(ManualChapterState, self).__init__(flags=flags)
        self.__cachedParams = {}

    @classmethod
    def goTo(cls, chapterIndex, pageIndex=None):
        super(ManualChapterState, cls).goTo(chapterIndex=chapterIndex, pageIndex=pageIndex)

    def registerTransitions(self):
        lsm = self.getMachine()
        lsm.addNavigationTransitionFromParent(self)

    def getNavigationDescription(self):
        view = self.getMachine().getRelatedView(self)
        title = view.chapterData['details'][0]['chapterTitle']
        return LobbyStateDescription(title=title)

    def serializeParams(self):
        return self.__cachedParams

    def _getViewLoadCtx(self, event):
        return {'ctx': (event.params)}

    def _onEntered(self, event):
        self.__cachedParams = event.params
        super(ManualChapterState, self)._onEntered(event)

    def _onExited(self):
        self.__cachedParams = {}
        super(ManualChapterState, self)._onExited()
