# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/wgcg/promo_screens/handlers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import TYPE_CHECKING as TYPE_CHECKING
from gui.wgcg.base.handlers import RequestHandlers as RequestHandlers
from gui.wgcg.settings import WebRequestDataType as WebRequestDataType
from gui.wgcg.promo_screens.contexts import PromoGetTeaserRequestCtx as PromoGetTeaserRequestCtx, PromoSendTeaserShownRequestCtx as PromoSendTeaserShownRequestCtx, PromoGetUnreadCountRequestCtx as PromoGetUnreadCountRequestCtx, PromoSendActionLogCtx as PromoSendActionLogCtx
from typing import Callable as Callable

class PromoScreensRequestHandlers(RequestHandlers):
    def get(self):
        ...
    def __getTeaser(self, ctx, callback):
        ...
    def __sendShownTeaser(self, ctx, callback):
        ...
    def __getUnreadCount(self, ctx, callback):
        ...
    def __sendActionLog(self, ctx, callback):
        ...
