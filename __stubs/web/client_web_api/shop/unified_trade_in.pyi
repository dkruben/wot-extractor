# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/web/client_web_api/shop/unified_trade_in.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.Scaleform.framework.entities.EventSystemEntity import EventSystemEntity as EventSystemEntity
from gui.shared import events as events
from helpers import dependency as dependency
from skeletons.gui.game_control import ITradeInController as ITradeInController
from web.client_web_api.api import C2WHandler as C2WHandler, c2w as c2w

class UnifiedTradeInEventHandler(C2WHandler, EventSystemEntity):
    __tradeIn: Any
    tradeInHelper: Any
    def __init__(self, sender):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def __onTokensUpdate(self, diff):
        ...
    # decorador original: @c2w(...)
    def __onTradeInDataChanged(self, *args, **kwargs):
        ...
