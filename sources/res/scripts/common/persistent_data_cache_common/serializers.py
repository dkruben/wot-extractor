# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/persistent_data_cache_common/serializers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/persistent_data_cache_common/serializers.py
from __future__ import absolute_import
import typing, wg_pickle
if typing.TYPE_CHECKING:
    from persistent_data_cache_common.types import TData

class ISerializer(object):
    __slots__ = ()

    def deserialize(self, serializedData):
        raise NotImplementedError

    def serialize(self, rawData):
        raise NotImplementedError

    def rollbackSideEffects(self):
        raise NotImplementedError


class WGPickleSerializer(ISerializer):
    __slots__ = ()

    def deserialize(self, serializedData):
        return wg_pickle.loads(serializedData)

    def serialize(self, rawData):
        return wg_pickle.dumps(rawData)

    def rollbackSideEffects(self):
        pass


defaultSerializer = WGPickleSerializer()
