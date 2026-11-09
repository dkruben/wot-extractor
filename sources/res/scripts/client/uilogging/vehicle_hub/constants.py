# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/uilogging/vehicle_hub/constants.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/uilogging/vehicle_hub/constants.py
from __future__ import absolute_import
from enum import Enum
TIME_LIMIT = 2

class Features(str, Enum):
    ARMOR_INSPECTOR = 'armor_inspector'


class Tabs(str, Enum):
    ARMOR_TAB = 'armor_tab'


class LogItems(str, Enum):
    ARMOR_TOOLTIP = 'armor_tooltip'


class LogActions(str, Enum):
    OPEN = 'open'
    CLOSE = 'close'
    CLICK = 'click'
    TOOLTIP_ACTION = 'watched'
    EXPAND = 'expand'
    COLLAPSE = 'collapse'
