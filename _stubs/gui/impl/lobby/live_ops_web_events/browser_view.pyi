# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/live_ops_web_events/browser_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewFlags as ViewFlags
from gui.Scaleform.framework.entities.inject_component_adaptor import InjectComponentAdaptor as InjectComponentAdaptor
from gui.impl.gen import R as R
from gui.impl.lobby.common.browser_view import BrowserView as BrowserView, makeSettings as makeSettings
from gui.Scaleform.daapi.view.meta.LiveOpsWebEventsViewMeta import LiveOpsWebEventsViewMeta as LiveOpsWebEventsViewMeta
from helpers import dependency as dependency
from skeletons.gui.game_control import ILiveOpsWebEventsController as ILiveOpsWebEventsController
from skeletons.gui.server_events import IEventsCache as IEventsCache
from web.web_client_api import webApiCollection as webApiCollection
from web.web_client_api.live_ops_web_events import LiveOpsWebEventsWebApi as LiveOpsWebEventsWebApi
from web.web_client_api.request import RequestWebApi as RequestWebApi
from web.web_client_api.ui import CloseWindowWebApi as CloseWindowWebApi, UtilWebApi as UtilWebApi

class LiveOpsWebEventsInjectView(InjectComponentAdaptor, LiveOpsWebEventsViewMeta):
    @staticmethod
    def markVisited():
        ...
    def _makeInjectView(self):
        ...

class LiveOpsWebEventsBrowserView(BrowserView):
    __liveOpsWebEventsController: Any
    def __init__(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def __markVisited(self):
        ...
    @staticmethod
    def __returnCallback(*args, **kwargs):
        ...

def createWebHandlers():
    ...
