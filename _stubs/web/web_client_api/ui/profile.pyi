# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/web/web_client_api/ui/profile.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from past.builtins import basestring as basestring, long as long
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams as SFViewLoadParams
from gui.shared.event_bus import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.event_dispatcher import events as events, g_eventBus as g_eventBus, showProfileWindow as showProfileWindow, requestProfile as requestProfile
from web.web_client_api import w2c as w2c, W2CSchema as W2CSchema, Field as Field
_PROFILE_TAB_ALIASES: dict

class _OpenProfileWindowSchema(W2CSchema):
    database_id: Any
    user_name: Any

class _OpenProfileTabSchema(W2CSchema):
    selected_id: Any

class ProfileTabWebApiMixin(object):
    # decorador original: @w2c(...)
    def profile(self, cmd):
        ...

class ProfileWindowWebApiMixin(object):
    # decorador original: @w2c(...)
    def profile(self, cmd):
        ...
