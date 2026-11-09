# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/proto/xmpp/messages/formatters.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from messenger.formatters.chat_message import LobbyMessageBuilder as LobbyMessageBuilder
from messenger.m_constants import USER_GUI_TYPE as USER_GUI_TYPE
from messenger.proto.xmpp.xmpp_constants import XMPP_MUC_USER_TEMPLATE_GROUPS as XMPP_MUC_USER_TEMPLATE_GROUPS, XMPP_MUC_USER_TYPE_PRIORITY as XMPP_MUC_USER_TYPE_PRIORITY
from messenger.proto.xmpp.xmpp_constants import XMPP_MUC_USER_GUI_TYPE_OVERRIDE_TRIGGER as XMPP_MUC_USER_GUI_TYPE_OVERRIDE_TRIGGER

class XmppLobbyMessageBuilder(LobbyMessageBuilder):
    __slots__: tuple
    __affiliation: Any
    __role: Any
    def __init__(self):
        ...
    def setAffiliation(self, affiliation):
        ...
    def setRole(self, role):
        ...
    def __updateTemplateKey(self):
        ...

class XmppLobbyUsersChatBuilder(LobbyMessageBuilder):
    def setAffiliation(self, _):
        ...
    def setRole(self, _):
        ...
