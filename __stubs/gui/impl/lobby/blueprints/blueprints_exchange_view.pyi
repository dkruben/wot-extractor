# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/blueprints/blueprints_exchange_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from functools import partial as partial
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.daapi.view.lobby.shared.web_view import WebViewTransparent as WebViewTransparent
from gui.shared.event_dispatcher import showBlueprintsSalePage as showBlueprintsSalePage, showHangar as showHangar
from web.web_client_api.ui import OpenTabWebApi as OpenTabWebApi

class _OpenTabWebApi(OpenTabWebApi):
    def _getVehiclePreviewReturnAlias(self, cmd):
        ...
    def _getVehiclePreviewReturnCallback(self, cmd):
        ...
    def _getVehicleStylePreviewCallback(self, cmd):
        ...
    def __getBackCallback(self, cmd):
        ...
    def __goBack(self, url):
        ...

class BlueprintsExchangeView(WebViewTransparent):
    def __init__(self, ctx=None):
        ...
    @property
    def webHandlersReplacements(self):
        ...
