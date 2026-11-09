# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/web/web_client_api/ui/clan.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from past.builtins import basestring as basestring, long as long
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.shared.event_dispatcher import showClanProfileWindow as showClanProfileWindow, showClanInvitesWindow as showClanInvitesWindow, showClanSearchWindow as showClanSearchWindow, showClanPersonalInvitesWindow as showClanPersonalInvitesWindow, showBrowserOverlayView as showBrowserOverlayView
from web.web_client_api import w2c as w2c, W2CSchema as W2CSchema, Field as Field

class _OpenBrowserOverlaySchema(W2CSchema):
    url: Any

class _OpenClanCardSchema(W2CSchema):
    clan_dbid: Any
    clan_abbrev: Any

class ClanWindowWebApiMixin(object):
    # decorador original: @w2c(...)
    def clanCardWindow(self, cmd):
        ...
    # decorador original: @w2c(...)
    def handleOpenClanInvites(self, cmd):
        ...
    # decorador original: @w2c(...)
    def handleOpenClanSearch(self, cmd):
        ...
    # decorador original: @w2c(...)
    def handleOpenPersonalInvites(self, cmd):
        ...
    # decorador original: @w2c(...)
    def handleOpenClanAds(self, cmd):
        ...
