# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/gui/Scaleform/view/lobby/ChannelsManagementWindow.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from constants import IS_CHINA as IS_CHINA
from debug_utils import LOG_ERROR as LOG_ERROR
from gui.Scaleform.locale.MESSENGER import MESSENGER as MESSENGER
from gui.Scaleform.managers.windows_stored_data import DATA_TYPE as DATA_TYPE, TARGET_ID as TARGET_ID, g_windowsStoredData as g_windowsStoredData
from gui.Scaleform.managers.windows_stored_data import stored_window as stored_window
from helpers import i18n as i18n
from messenger import MessengerEntry as MessengerEntry
from messenger.gui.Scaleform.data.search_data_providers import SearchChannelsDataProvider as SearchChannelsDataProvider
from messenger.gui.Scaleform.lobby_entry import LobbyEntry as LobbyEntry
from messenger.gui.Scaleform.meta.ChannelsManagementWindowMeta import ChannelsManagementWindowMeta as ChannelsManagementWindowMeta
from messenger.m_constants import PROTO_TYPE as PROTO_TYPE, MESSENGER_SCOPE as MESSENGER_SCOPE
from messenger.proto import proto_getter as proto_getter
from messenger.proto.events import g_messengerEvents as g_messengerEvents
from messenger.proto.interfaces import ISearchHandler as ISearchHandler

# decorador original: @stored_window(...)
class ChannelsManagementWindow(ChannelsManagementWindowMeta, ISearchHandler):
    _searchDP: Any
    def __init__(self, **kwargs):
        ...
    # decorador original: @proto_getter(...)
    def proto(self):
        ...
    def onWindowClose(self):
        ...
    def getSearchLimitLabel(self):
        ...
    def searchToken(self, token):
        ...
    def joinToChannel(self, index):
        ...
    def createChannel(self, name, usePassword, password, retype):
        ...
    def onSearchComplete(self, _):
        ...
    def onSearchFailed(self, _):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __setInitialGeometry(self):
        ...
