# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/gifts/gifts_common.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/gifts/gifts_common.py
from __future__ import absolute_import
from constants import IS_DEVELOPMENT
from soft_exception import SoftException
UNKNOWN_SENDER_ID = 0
UNPROCESSED_GIFT_DB_ID = -1

class ClientReqStrategy(object):
    AUTO = 'auto'
    DEMAND = 'demand'
    ALL = (AUTO, DEMAND)


class GiftEventID(object):
    UNKNOWN = 0
    DEV_TEST = 1
    ALL = (UNKNOWN,) + ((DEV_TEST,) if IS_DEVELOPMENT else ())


class GiftEventState(object):
    ENABLED = 'enabled'
    SUSPENDED = 'suspended'
    DISABLED = 'disabled'
    ALL = (ENABLED, SUSPENDED, DISABLED)


class GiftStatus(object):
    TYPE = int
    NEW = 1
    AVAILABLE = 2
    OPENED = 3
    ACTIVE = (
     NEW, AVAILABLE)
    ALL = (
     NEW, AVAILABLE, OPENED)


class Gift(object):
    __slots__ = ('_giftID', '_senderID', '_giftItemID', '_status', '_meta')

    def __init__(self, giftID, senderID, giftItemID, status, meta):
        self._giftID = giftID
        self._senderID = senderID
        self._giftItemID = giftItemID
        self._status = status
        self._meta = meta

    @property
    def giftID(self):
        return self._giftID

    @property
    def giftItemID(self):
        return self._giftItemID

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        if value not in GiftStatus.ALL:
            raise SoftException('Wrong status', value)
        self._status = value

    def toOpenExtra(self):
        return (
         self._senderID, self._meta)

    def __str__(self):
        return ('Gift:[giftID: {}, senderID: {}, giftItemID: {}, meta: {}, status: {}]').format(self._giftID, self._senderID, self._giftItemID, self._meta, self._status)
