# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/messenger/proto/xmpp/xmpp_limits.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/messenger/proto/xmpp/xmpp_limits.py
from __future__ import absolute_import
from messenger.proto.interfaces import IUserSearchLimits, IProtoLimits
from messenger.proto.xmpp.xmpp_constants import USER_SEARCH_LIMITS, MESSAGE_LIMIT

class FindUserSearchLimits(IUserSearchLimits):

    def getMaxResultSize(self):
        return USER_SEARCH_LIMITS.FIND_USERS_BY_NAME_MAX_RESULT_SIZE

    def getRequestCooldown(self):
        return USER_SEARCH_LIMITS.FIND_USERS_BY_NAME_REQUEST_COOLDOWN_SEC


class MessageLimits(IProtoLimits):

    def getMessageMaxLength(self):
        return MESSAGE_LIMIT.MESSAGE_MAX_SIZE

    def getBroadcastCoolDown(self):
        return MESSAGE_LIMIT.COOLDOWN

    def getHistoryMaxLength(self):
        return MESSAGE_LIMIT.HISTORY_MAX_LEN
