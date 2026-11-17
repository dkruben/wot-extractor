# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/gui/Scaleform/view/lobby/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from frameworks.wulf import WindowLayer as WindowLayer
from gui.Scaleform.framework import GroupedViewSettings as GroupedViewSettings, ComponentSettings as ComponentSettings
from gui.Scaleform.framework import ScopeTemplates as ScopeTemplates
from gui.Scaleform.framework.package_layout import PackageBusinessHandler as PackageBusinessHandler
from gui.Scaleform.genConsts.CONTACTS_ALIASES import CONTACTS_ALIASES as CONTACTS_ALIASES
from gui.Scaleform.genConsts.CONTEXT_MENU_HANDLER_TYPE import CONTEXT_MENU_HANDLER_TYPE as CONTEXT_MENU_HANDLER_TYPE
from gui.app_loader import settings as app_settings
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.utils.functions import getViewName as getViewName
ACCOUNT_NAME_MIN_CHARS_LENGTH = 2
ACCOUNT_NAME_MAX_CHARS_LENGTH = 24

class MESSENGER_VIEW_ALIAS(object):
    FAQ_WINDOW = 'messenger/faqWindow'
    CHANNEL_MANAGEMENT_WINDOW = 'messenger/channelsManagementWindow'
    LAZY_CHANNEL_WINDOW = 'messenger/lazyChannelWindow'
    LOBBY_CHANNEL_WINDOW = 'messenger/lobbyChannelWindow'
    CONNECT_TO_SECURE_CHANNEL_WINDOW = 'messenger/connectToSecureChannelWindow'
    CHANNEL_COMPONENT = 'channelComponent'

class _MessengerPackageBusinessHandler(PackageBusinessHandler):
    def __init__(self):
        ...
    def __showLazyChannelWindow(self, event):
        ...
    def __showLobbyChannelWindow(self, event):
        ...

def getContextMenuHandlers():
    ...
def getViewSettings():
    ...
def getBusinessHandlers():
    ...
