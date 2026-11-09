# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/messenger/gui/Scaleform/view/lobby/ConnectToSecureChannelWindow.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/messenger/gui/Scaleform/view/lobby/ConnectToSecureChannelWindow.py
from __future__ import absolute_import
from gui.Scaleform.locale.MESSENGER import MESSENGER
from helpers import i18n
from messenger.gui.Scaleform.meta.ConnectToSecureChannelWindowMeta import ConnectToSecureChannelWindowMeta
from messenger.m_constants import PROTO_TYPE
from messenger.proto import proto_getter
from messenger.proto.events import g_messengerEvents

class ConnectToSecureChannelWindow(ConnectToSecureChannelWindowMeta):

    def __init__(self, ctx=None):
        super(ConnectToSecureChannelWindow, self).__init__()
        self._channel = ctx.get('channel')

    @proto_getter(PROTO_TYPE.MIGRATION)
    def proto(self):
        return

    def onWindowClose(self):
        self.destroy()

    def sendPassword(self, value):
        validator = self.proto.messages.getUserRoomValidator()
        password, error = validator.validateUserRoomPwd(value)
        if error is not None:
            g_messengerEvents.onErrorReceived(error)
        else:
            self.proto.messages.joinToUserRoom(self._channel.getID(), self._channel.getFullName(), password=password)
            self.destroy()
        return

    def cancelPassword(self):
        self.destroy()

    def _populate(self):
        super(ConnectToSecureChannelWindow, self)._populate()
        self.as_infoMessageS(i18n.makeString(MESSENGER.DIALOGS_CONNECTINGTOSECURECHANNEL_LABELS_INFO, self._channel.getFullName()))

    def _dispose(self):
        self._channel = None
        super(ConnectToSecureChannelWindow, self)._dispose()
        return
