# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/live_ops_web_events/browser_view.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/live_ops_web_events/browser_view.py
from frameworks.wulf import ViewFlags
from gui.Scaleform.framework.entities.inject_component_adaptor import InjectComponentAdaptor
from gui.impl.gen import R
from gui.impl.lobby.common.browser_view import BrowserView, makeSettings
from gui.Scaleform.daapi.view.meta.LiveOpsWebEventsViewMeta import LiveOpsWebEventsViewMeta
from helpers import dependency
from skeletons.gui.game_control import ILiveOpsWebEventsController
from skeletons.gui.server_events import IEventsCache
from web.web_client_api import webApiCollection
from web.web_client_api.live_ops_web_events import LiveOpsWebEventsWebApi
from web.web_client_api.request import RequestWebApi
from web.web_client_api.ui import CloseWindowWebApi, UtilWebApi

def createWebHandlers():
    return webApiCollection(CloseWindowWebApi, RequestWebApi, UtilWebApi, LiveOpsWebEventsWebApi)


class LiveOpsWebEventsInjectView(InjectComponentAdaptor, LiveOpsWebEventsViewMeta):

    @staticmethod
    def markVisited():
        dependency.instance(IEventsCache).onEventsVisited()

    def _makeInjectView(self):
        return LiveOpsWebEventsBrowserView()


class LiveOpsWebEventsBrowserView(BrowserView):
    __liveOpsWebEventsController = dependency.descriptor(ILiveOpsWebEventsController)

    def __init__(self):
        super(LiveOpsWebEventsBrowserView, self).__init__(R.views.lobby.common.BrowserView(), settings=makeSettings(url=self.__liveOpsWebEventsController.eventUrl, webHandlers=createWebHandlers(), viewFlags=ViewFlags.VIEW, returnClb=self.__returnCallback))

    def _onLoading(self, *args, **kwargs):
        super(LiveOpsWebEventsBrowserView, self)._onLoading(*args, **kwargs)
        self.__markVisited()

    def __markVisited(self):
        self.__liveOpsWebEventsController.markEventTabVisited()

    @staticmethod
    def __returnCallback(*args, **kwargs):
        if kwargs.pop('forceClosed', False):
            from gui.shared.event_dispatcher import showHangar
            showHangar()
