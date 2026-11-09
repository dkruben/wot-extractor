# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/uilogging/prebattle_highlights/constants.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/uilogging/prebattle_highlights/constants.py
from __future__ import absolute_import
from enum import Enum
FEATURE = 'prebattle_highlights'

class PrebattleHighlightsLogAction(Enum):
    VIEWED = 'viewed'
    COLLAPSE = 'collapse'


class PrebattleHighlightsLogKeys(Enum):
    PBH = 'pbh'
    PBH_OUT_OF_FOCUS = 'pbh_out_of_focus'
    FULLY_VIEWED = 'fully_viewed'
    ESC = 'esc'
    SETTINGS_PBH = 'settings_pbh'
    SETTINGS_HISTORICAL = 'settings_historical'
    NOT_ENOUGH_TIME = 'not_enough_time'
