# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/game_control/reactive_comm/packer.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/game_control/reactive_comm/packer.py
from __future__ import absolute_import
import typing, cbor
from gui.game_control.reactive_comm.constants import SubscriptionServerStatus
if typing.TYPE_CHECKING:
    from gui.game_control.reactive_comm.constants import SubscriptionCommand

class ServiceMessage(object):
    __slots__ = ('cid', 'channel', 'status', 'seqid', 'data')

    def __init__(self, cid=None, channel='', status='', seqid=None, data=None, **_):
        super(ServiceMessage, self).__init__()
        self.cid = cid
        self.channel = channel
        self.status = SubscriptionServerStatus.fromString(status)
        self.seqid = seqid
        self.data = data

    @property
    def isStatusReceived(self):
        return self.channel and self.status

    @property
    def isMessageReceived(self):
        return self.cid is not None and self.data is not None

    @property
    def isValid(self):
        return self.isStatusReceived or self.isMessageReceived


def packCommand(channel, command):
    result = cbor.dumps({'channel': channel, 
       'cmd': (command.value)})
    return result


def unpackMessage(payload):
    raw = cbor.loads(payload)
    if not isinstance(raw, dict):
        raw = {}
    return ServiceMessage(**raw)
