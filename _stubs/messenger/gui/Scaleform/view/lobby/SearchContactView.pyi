# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/gui/Scaleform/view/lobby/SearchContactView.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.locale.MESSENGER import MESSENGER as MESSENGER
from helpers import i18n as i18n
from messenger.gui.Scaleform.data.search_data_providers import SearchUsersDataProvider as SearchUsersDataProvider
from messenger.gui.Scaleform.meta.SearchContactViewMeta import SearchContactViewMeta as SearchContactViewMeta
from messenger.gui.Scaleform.view.lobby import ACCOUNT_NAME_MIN_CHARS_LENGTH as ACCOUNT_NAME_MIN_CHARS_LENGTH, ACCOUNT_NAME_MAX_CHARS_LENGTH as ACCOUNT_NAME_MAX_CHARS_LENGTH
from messenger.m_constants import PROTO_TYPE as PROTO_TYPE
from messenger.proto import proto_getter as proto_getter
from messenger.proto.interfaces import ISearchHandler as ISearchHandler
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.rq_cooldown import getRequestCoolDown as getRequestCoolDown

class SearchContactView(SearchContactViewMeta, ISearchHandler):
    _searchDP: Any
    _cooldownInfo: Any
    def __init__(self):
        ...
    # decorador original: @proto_getter(...)
    def proto(self):
        ...
    def search(self, data):
        ...
    def onSearchComplete(self, result):
        ...
    def onSearchFailed(self, reason):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _getInitDataObject(self):
        ...
    def __handleSetSearchCoolDown(self, event):
        ...
