# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/gui/Scaleform/view/lobby/ConnectToSecureChannelWindow.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.locale.MESSENGER import MESSENGER as MESSENGER
from helpers import i18n as i18n
from messenger.gui.Scaleform.meta.ConnectToSecureChannelWindowMeta import ConnectToSecureChannelWindowMeta as ConnectToSecureChannelWindowMeta
from messenger.m_constants import PROTO_TYPE as PROTO_TYPE
from messenger.proto import proto_getter as proto_getter
from messenger.proto.events import g_messengerEvents as g_messengerEvents

class ConnectToSecureChannelWindow(ConnectToSecureChannelWindowMeta):
    _channel: Any
    def __init__(self, ctx=None):
        ...
    # decorador original: @proto_getter(...)
    def proto(self):
        ...
    def onWindowClose(self):
        ...
    def sendPassword(self, value):
        ...
    def cancelPassword(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
