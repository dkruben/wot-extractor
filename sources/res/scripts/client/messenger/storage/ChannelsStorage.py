# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/messenger/storage/ChannelsStorage.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/messenger/storage/ChannelsStorage.py
from __future__ import absolute_import
from future.utils import lfilter
from debug_utils import LOG_ERROR
from messenger.ext.channel_num_gen import genClientID4Channel
from messenger.storage.local_cache import SimpleCachedStorage
_CHANNELS_MAX_COUNT = 20

class ChannelsStorage(SimpleCachedStorage):
    __slots__ = ('__channels', )

    def __init__(self):
        super(ChannelsStorage, self).__init__()
        self.__channels = []

    def __repr__(self):
        return ('ChannelsStorage(id=0x{0:08X}, len={1:n})').format(id(self), len(self.__channels))

    def clear(self):
        while self.__channels:
            self.__channels.pop().clear()

        super(ChannelsStorage, self).clear()

    def all(self):
        return self.__channels[:]

    def getChannel(self, channel):
        result = None
        if channel in self.__channels:
            index = self.__channels.index(channel)
            result = self.__channels[index]
        return result

    def getChannelsByCriteria(self, criteria):
        return lfilter(criteria.filter, self.__channels)

    def getChannelByCriteria(self, criteria):
        channels = self.getChannelsByCriteria(criteria)
        if channels:
            return channels[0]
        else:
            return

    def addChannel(self, channel):
        result = True
        if channel not in self.__channels:
            channel.setClientID(genClientID4Channel(channel))
            self.__channels.append(channel)
        else:
            LOG_ERROR('Channel already exists in storage', channel)
            result = False
        return result

    def removeChannel(self, channel, clear=True):
        result = True
        if channel in self.__channels:
            index = self.__channels.index(channel)
            stored = self.__channels.pop(index)
            if clear:
                stored.clear()
        else:
            LOG_ERROR('Channel is not in storage', channel)
            result = False
        return result

    def _getCachedData(self):
        data = []
        for channel in self.__channels:
            state = channel.getPersistentState()
            if state:
                data.append((channel.getProtoType(), str(channel.getID()), state))

        return data[-_CHANNELS_MAX_COUNT:]

    def _setCachedData(self, data):
        if not data:
            return None
        else:

            def stateGenerator(requiredType):
                for item in data:
                    if not isinstance(item, tuple):
                        continue
                    if len(item) != 3:
                        continue
                    protoType, channelID, state = item
                    if requiredType != protoType:
                        continue
                    yield (
                     channelID, state)

            return stateGenerator
