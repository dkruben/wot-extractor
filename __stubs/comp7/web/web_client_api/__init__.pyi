# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/web/web_client_api/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from comp7.skeletons.gui.game_control import IComp7ShopController as IComp7ShopController
from comp7.web.web_client_api.ui.comp7_ui import OpenComp7Mixin as OpenComp7Mixin
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams as SFViewLoadParams
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared import events as events
from gui.shared import g_eventBus as g_eventBus
from helpers import dependency as dependency
from skeletons.gui.game_control import IComp7Controller as IComp7Controller
from web.web_client_api import w2capi as w2capi, w2c as w2c, W2CSchema as W2CSchema
from web.web_client_api.ui import OpenWindowWebApi as OpenWindowWebApi

# decorador original: @w2capi(...)
class Comp7WebApi(OpenComp7Mixin):
    __comp7Controller: Any
    __comp7ShopController: Any
    # decorador original: @w2c(...)
    def closeBrowser(self, _):
        ...
    # decorador original: @w2c(...)
    def getGamemodeState(self, _):
        ...

# decorador original: @w2capi(...)
class Comp7OpenWindowWebApi(OpenWindowWebApi, OpenComp7Mixin):
    ...
