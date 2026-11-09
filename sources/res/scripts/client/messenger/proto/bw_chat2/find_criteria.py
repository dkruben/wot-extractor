# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/messenger/proto/bw_chat2/find_criteria.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/messenger/proto/bw_chat2/find_criteria.py
from __future__ import absolute_import
from constants import PREBATTLE_TYPE
from messenger.ext import channel_num_gen
from messenger.m_constants import BATTLE_CHANNEL, PROTO_TYPE
from messenger.proto.interfaces import IEntityFindCriteria

class BWBattleChannelFindCriteria(IEntityFindCriteria):

    def __init__(self):
        super(BWBattleChannelFindCriteria, self).__init__()
        self.__ids = []
        for item in BATTLE_CHANNEL.ALL:
            clientID = channel_num_gen.getClientID4BattleChannel(item.name)
            if clientID:
                self.__ids.append(clientID)

        clientID = channel_num_gen.getClientID4Prebattle(PREBATTLE_TYPE.SQUAD)
        if clientID:
            self.__ids.append(clientID)

    def filter(self, entity):
        return entity.getProtoType() is PROTO_TYPE.BW_CHAT2 and entity.getClientID() in self.__ids


class BWPrebattleChannelFindCriteria(IEntityFindCriteria):

    def filter(self, entity):
        return entity.getProtoType() is PROTO_TYPE.BW_CHAT2 and entity.getPrebattleType()


class BWChatTypeFindCriteria(IEntityFindCriteria):

    def __init__(self, chatType):
        super(BWChatTypeFindCriteria, self).__init__()
        self.__chatType = chatType

    def filter(self, entity):
        return entity.getProtoType() is PROTO_TYPE.BW_CHAT2 and entity.getProtoData().chatType == self.__chatType
