# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/messenger/proto/xmpp/extensions/shared_queries.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/messenger/proto/xmpp/extensions/shared_queries.py
from __future__ import absolute_import
from messenger.proto.xmpp.extensions import PyQuery
from messenger.proto.xmpp.extensions.wg_items import WgClientExtension

class MessageQuery(PyQuery):
    __slots__ = ('_body', )

    def __init__(self, msgType, to, msgBody='', ext=None):
        super(MessageQuery, self).__init__(msgType, ext, to)
        self._body = msgBody

    def getBody(self):
        return self._body


class PresenceQuery(PyQuery):

    def __init__(self, queryType, to=''):
        super(PresenceQuery, self).__init__(queryType, WgClientExtension(), to)

    def getStatus(self):
        return ('', '')

    def isMucNsUsed(self):
        return False

    def setIgrID(self, igrID):
        if self._ext:
            self._ext.setIgrID(igrID)

    def setIgrRoomID(self, igrRoomID):
        if self._ext:
            self._ext.setIgrRoomID(igrRoomID)

    def setGameServerHost(self, host):
        if self._ext:
            self._ext.setGameServerHost(host)

    def setArenaGuiLabel(self, label):
        if self._ext:
            self._ext.setArenaGuiLabel(label)
