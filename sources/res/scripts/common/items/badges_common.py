# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/items/badges_common.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/items/badges_common.py
from __future__ import absolute_import
import struct
from typing import TYPE_CHECKING, List, Tuple, Any
if TYPE_CHECKING:
    from BaseAccount import BaseAccount
ExtraInfo = List[Any]
BadgesInfo = Tuple[(List[int], ExtraInfo)]

class BadgesCommon(object):
    _BADGE_IDS_LEN_FORMAT = '<B'
    _BADGE_IDS = '<{}I'
    _BADGES_EXTRA_INFO = '<I'

    @staticmethod
    def getExtraInfo(account):
        extraInfo = []
        return extraInfo

    @staticmethod
    def selectedBadgesEmpty():
        return ([], [])

    @staticmethod
    def packPlayerBadges(badgesInfo):
        badgeIDs, extraInfo = badgesInfo
        badgesLen, extraInfoLen = len(badgeIDs), len(extraInfo)
        packed = BadgesCommon._packLen(badgesLen)
        if badgesLen:
            packed += struct.pack(BadgesCommon._getBadgeIDsFormat(badgesLen), *badgeIDs)
        packed += BadgesCommon._packLen(extraInfoLen)
        if extraInfoLen:
            packed += struct.pack(BadgesCommon._BADGES_EXTRA_INFO, *extraInfo)
        return packed

    @staticmethod
    def unpackPlayerBadges(packedData, initialOffset):
        offset = initialOffset
        badgeIDsLen, offset = BadgesCommon._unpackLen(packedData, offset)
        if badgeIDsLen:
            fmt = BadgesCommon._getBadgeIDsFormat(badgeIDsLen)
            badgeIDs = list(struct.unpack_from(fmt, packedData, offset))
            offset += struct.calcsize(fmt)
        else:
            badgeIDs = []
        extraInfoLen, offset = BadgesCommon._unpackLen(packedData, offset)
        if extraInfoLen:
            extraInfo = list(struct.unpack_from(BadgesCommon._BADGES_EXTRA_INFO, packedData, offset))
            offset += struct.calcsize(BadgesCommon._BADGES_EXTRA_INFO)
        else:
            extraInfo = []
        return (
         (
          badgeIDs, extraInfo), offset - initialOffset)

    @staticmethod
    def _getBadgeIDsFormat(badgesLen):
        return BadgesCommon._BADGE_IDS.format(badgesLen)

    @staticmethod
    def _packLen(lenValue):
        return struct.pack(BadgesCommon._BADGE_IDS_LEN_FORMAT, lenValue)

    @staticmethod
    def _unpackLen(packedData, offset):
        lenValue = struct.unpack_from(BadgesCommon._BADGE_IDS_LEN_FORMAT, packedData, offset)[0]
        newOffset = offset + struct.calcsize(BadgesCommon._BADGE_IDS_LEN_FORMAT)
        return (lenValue, newOffset)
