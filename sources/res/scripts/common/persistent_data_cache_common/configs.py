# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/persistent_data_cache_common/configs.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/persistent_data_cache_common/configs.py
from __future__ import absolute_import
import typing
from soft_exception import SoftException
if typing.TYPE_CHECKING:
    from persistent_data_cache_common.types import TPDCVersion

class BasePDCConfig(object):
    __slots__ = ('version', 'cacheFilePath')

    def __init__(self, version, cacheFilePath):
        self.version = version
        if not cacheFilePath:
            raise SoftException('Cache file path cannot be empty.')
        self.cacheFilePath = cacheFilePath

    def __repr__(self):
        return ('<{}>(version={}, cacheFilePath={})').format(self.__class__.__name__, self.version, self.cacheFilePath)
