# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/clans/users.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import weakref as weakref
from adisp import adisp_async as adisp_async, adisp_process as adisp_process
from gui.wgcg.clan.contexts import AccountClanRatingsCtx as AccountClanRatingsCtx

class UserCache(object):
    __cache: Any
    __clanCtrl: Any
    def __init__(self, clanCtrl):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def requestUsers(self, dbIDs, callback):
        ...
