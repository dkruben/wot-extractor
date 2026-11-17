# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/MessengerEntry.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from PlayerEvents import g_playerEvents as g_playerEvents
from helpers import dependency as dependency
from messenger import g_settings as g_settings
from messenger.ext.filters import MessageFiltersChain as MessageFiltersChain
from messenger.ext.player_helpers import CurrentPlayerHelper as CurrentPlayerHelper
from messenger.gui.entry_decorator import GUIDecorator as GUIDecorator
from messenger.m_constants import MESSENGER_SCOPE as MESSENGER_SCOPE
from messenger.proto import ProtoPluginsDecorator as ProtoPluginsDecorator
from messenger.storage import StorageDecorator as StorageDecorator
from skeletons.connection_mgr import IConnectionManager as IConnectionManager
g_instance: Any

class MessengerEntry(object):
    connectionMgr: Any
    __protoPlugins: Any
    __storage: Any
    __gui: Any
    __playerHelper: Any
    __msgFiltersChain: Any
    def __init__(self):
        ...
    @property
    def protos(self):
        ...
    @property
    def storage(self):
        ...
    @property
    def gui(self):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def onAccountShowGUI(self):
        ...
    def onAvatarInitGUI(self):
        ...
    def onAvatarShowGUI(self):
        ...
    def __pe_onAccountShowGUI(self, _):
        ...
    def __pe_onGuiCacheSyncCompleted(self, _):
        ...
    def __pe_onAccountBecomePlayer(self):
        ...
    def __pe_onAvatarBecomePlayer(self):
        ...
    def __pe_onAccountBecomeNonPlayer(self):
        ...
    def __pe_onAvatarBecomeNonPlayer(self):
        ...
    def __cm_onDisconnected(self):
        ...
