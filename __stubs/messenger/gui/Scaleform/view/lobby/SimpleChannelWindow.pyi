# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/gui/Scaleform/view/lobby/SimpleChannelWindow.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams as SFViewLoadParams
from gui.Scaleform.managers.windows_stored_data import g_windowsStoredData as g_windowsStoredData, TARGET_ID as TARGET_ID
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.events import FocusEvent as FocusEvent, ChannelWindowEvent as ChannelWindowEvent
from messenger import MessengerEntry as MessengerEntry
from messenger.gui.Scaleform.lobby_entry import LobbyEntry as LobbyEntry
from messenger.gui.Scaleform.meta.ChannelWindowMeta import ChannelWindowMeta as ChannelWindowMeta
from gui.shared import events as events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from messenger.gui.Scaleform.view.lobby import MESSENGER_VIEW_ALIAS as MESSENGER_VIEW_ALIAS
from messenger.inject import channelsCtrlProperty as channelsCtrlProperty
from messenger.m_constants import PROTO_TYPE as PROTO_TYPE, MESSENGER_SCOPE as MESSENGER_SCOPE
from messenger.proto import proto_getter as proto_getter

class SimpleChannelWindow(ChannelWindowMeta):
    _clientID: Any
    _controller: Any
    def __init__(self, ctx):
        ...
    # decorador original: @proto_getter(...)
    def proto(self):
        ...
    def onFocusIn(self, alias):
        ...
    # decorador original: @channelsCtrlProperty
    def channelsCtrl(self):
        ...
    def onWindowClose(self):
        ...
    def onWindowMinimize(self):
        ...
    def showFAQWindow(self):
        ...
    def getClientID(self):
        ...
    def getChannelID(self):
        ...
    def getProtoType(self):
        ...
    @property
    def chat(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _onRegisterFlashComponent(self, viewPy, alias):
        ...
    def __ce_onChannelInfoUpdated(self, channel):
        ...
    def __ce_onConnectStateChanged(self, _):
        ...
    def __checkConnectStatus(self):
        ...
    def __setInitialGeometry(self):
        ...
