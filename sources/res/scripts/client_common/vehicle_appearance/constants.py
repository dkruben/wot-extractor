# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client_common/vehicle_appearance/constants.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client_common/vehicle_appearance/constants.py
from __future__ import absolute_import
import enum
DEFAULT_STICKERS_ALPHA = 1.0
PERIODIC_UPDATE_TIME = 0.25
DIRT_UPDATE_MIN_TIME = 0.05

class AppearanceState(enum.IntEnum):
    CREATED = 0
    CONSTRUCTED = 1
    COMPONENTS_CREATED = 2
    ACTIVATED = 3
    DEACTIVATED = 4
    DESTROYED = 5
