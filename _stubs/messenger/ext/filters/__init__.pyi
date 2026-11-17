# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/ext/filters/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui import GUI_SETTINGS as GUI_SETTINGS
from messenger import g_settings as g_settings
from messenger.ext.filters import chain as chain, collection as collection
from messenger.storage import MessengerStorageDescriptor as MessengerStorageDescriptor, PlayerCtxStorage as PlayerCtxStorage
__all__: tuple

class MessageFiltersChain(chain.FiltersChain):
    playerCtx: Any
    def __init__(self):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def __ms_onUserPreferencesUpdated(self):
        ...
    def __pc_onAccountAttrsChanged(self):
        ...
