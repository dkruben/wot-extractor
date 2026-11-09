# wot-extractor: codigo DESCOMPILADO de sources/res/server_side_replay/scripts/client/server_side_replay/gui/shared/event_dispatcher.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: server_side_replay/scripts/client/server_side_replay/gui/shared/event_dispatcher.py
from __future__ import absolute_import
from helpers import dependency
from gui.impl.gen import R
from gui.shared import events, g_eventBus
from gui.shared.event_bus import EVENT_BUS_SCOPE
from skeletons.gui.impl import IGuiLoader
from gui.Scaleform.framework import ScopeTemplates
from gui.Scaleform.framework.managers.loaders import GuiImplViewLoadParams

def showReplays(location=None):
    from server_side_replay.gui.impl.lobby.replays_root_view import ReplaysRootView
    uiLoader = dependency.instance(IGuiLoader)
    layoutID = R.views.server_side_replay.lobby.MetaReplaysView()
    if uiLoader.windowsManager.getViewByLayoutID(layoutID) is None:
        g_eventBus.handleEvent(events.LoadGuiImplViewEvent(GuiImplViewLoadParams(layoutID=layoutID, viewClass=ReplaysRootView, scope=ScopeTemplates.LOBBY_SUB_SCOPE), ctx={'location': location}), scope=EVENT_BUS_SCOPE.LOBBY)
    return
