# wot-extractor: codigo DESCOMPILADO de sources/res/comp7_core/scripts/common/comp7_core_constants.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7_core/scripts/common/comp7_core_constants.py
from __future__ import absolute_import
import enum, constants
from constants_utils import ConstInjector
ROLE_EQUIPMENT_TAG = 'roleEquipment'

class ArenaPrebattlePhase(object):
    NONE = 0
    PREPICK = 1
    VOTING = 2
    PICK = 3


class FINISH_REASON(constants.FINISH_REASON, ConstInjector):
    SURVIVORS_LEFT = 201
    DAMAGE_DEALT = 202
    FIRST_KILL = 203
    DRAW_RESOLVED_REASONS = (
     SURVIVORS_LEFT, DAMAGE_DEALT, FIRST_KILL)


class SubMode(enum.Enum):
    REGULAR = 'regular'
    NIGHT_MAPS = 'night_maps'


def injectCommonConstants(personality):
    if not any(hasattr(constants.FINISH_REASON, attr) for attr in FINISH_REASON.getExtraAttrs()):
        FINISH_REASON.inject(personality)
