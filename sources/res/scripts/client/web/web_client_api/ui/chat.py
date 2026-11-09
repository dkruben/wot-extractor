# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/web/web_client_api/ui/chat.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/web/web_client_api/ui/chat.py
from __future__ import absolute_import
from past.builtins import basestring
from messenger.m_constants import PROTO_TYPE
from messenger.proto import proto_getter
from messenger.storage import UsersStorage, MessengerStorageDescriptor
from web.web_client_api import W2CSchema, Field, w2c
from web.web_client_api.common import SPA_ID_TYPES

class _OpenChatSchema(W2CSchema):
    user_id = Field(required=True, type=SPA_ID_TYPES)
    user_name = Field(required=True, type=basestring)


class ChatWebApiMixin(object):
    usersStorage = MessengerStorageDescriptor(UsersStorage)

    @proto_getter(PROTO_TYPE.MIGRATION)
    def proto(self):
        return

    @w2c(_OpenChatSchema, 'chat_window')
    def openChat(self, cmd):
        receiver = self.usersStorage.getUser(cmd.user_id)
        if receiver and not receiver.isIgnored():
            self.proto.contacts.createPrivateChannel(cmd.user_id, cmd.user_name.encode('utf-8'))
