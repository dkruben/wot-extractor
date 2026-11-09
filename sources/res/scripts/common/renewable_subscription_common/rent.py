# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/renewable_subscription_common/rent.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/renewable_subscription_common/rent.py
from __future__ import absolute_import
from enum import Enum

class RentEventTypes(Enum):
    START_RENT = 1
    END_RENT = 2


class RentLogInfo(Enum):
    ADD = 'excl_veh:add'
    START = 'excl_veh:on'
    END = 'excl_veh:off'
