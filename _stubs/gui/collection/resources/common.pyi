# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/collection/resources/common.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from gui.collection.resources.cdn.cache import CollectionsCdnCacheMgr as CollectionsCdnCacheMgr
from gui.collection.resources.local.cache import CollectionsLocalCacheMgr as CollectionsLocalCacheMgr
from helpers import dependency as dependency
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
_logger: Any

# decorador original: @dependency.replace_none_kwargs(...)
def makeCacheMgr(lobbyContext=None):
    ...
