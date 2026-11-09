# wot-extractor: codigo DESCOMPILADO de sources/res/resource_well/scripts/client/resource_well/gui/feature/constants.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: resource_well/scripts/client/resource_well/gui/feature/constants.py
from __future__ import absolute_import
import logging
from enum import Enum
_logger = logging.getLogger(__name__)
UNAVAILABLE_REWARD_ERROR = 'UNAVAILABLE_REWARD_ERROR'
CHANNEL_NAME_PREFIX = 'suv_'
DEFAULT_SEASON_NUMBER = 0

class PurchaseMode(Enum):
    ONE_SERIAL_PRODUCT = 'ONE_SERIAL_PRODUCT'
    SEQUENTIAL_PRODUCT = 'SEQUENTIAL_PRODUCT'
    TWO_PARALLEL_PRODUCTS = 'TWO_PARALLEL_PRODUCTS'


class ResourceType(Enum):
    BLUEPRINTS = 'blueprints'
    CURRENCY = 'currency'

    @classmethod
    def getMember(cls, value):
        if value in cls._value2member_map_:
            return cls(value)
        else:
            _logger.error('%s does not exist in ResourceType values', value)
            return
