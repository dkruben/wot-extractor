# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/gift_system/constants.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/gift_system/constants.py
from enum import unique, Enum, IntEnum
DEV_STAMP_CODE = 'giftSystem_1_devStamp'

@unique
class GifterResponseState(Enum):
    WEB_FAILURE = 'webFailure'
    WEB_SUCCESS = 'webSuccess'
    REQUESTS_DISABLED = 'requestsDisabled'
    WGCG_NOT_AVAILABLE = 'wgcgNotAvailable'
    REQUEST_IN_PROGRESS = 'requestInProgress'
    CENTER_DISCONNECTED = 'centerDisconnected'


@unique
class GiftMessageType(IntEnum):
    INCOME = 0
    OUTCOME = 1
    HISTORY = 2
    LIMITS = 4


@unique
class HubUpdateReason(IntEnum):
    HISTORY = 0
    SETTINGS = 1
    WEB_STATE = 2
    INCOME_GIFT = 3
    OUTCOME_GIFT = 4
    KEEPER_CLEAR = 5
    STAMPER_UPDATE = 6
