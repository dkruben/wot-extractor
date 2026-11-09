# wot-extractor: codigo DESCOMPILADO de sources/res/comp7_light/scripts/common/comp7_light_constants.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7_light/scripts/common/comp7_light_constants.py
from __future__ import absolute_import
import constants, enum
from constants_utils import ConstInjector
import UnitBase

class Configs(enum.Enum):
    COMP7_LIGHT_CONFIG = 'comp7_light_config'


COMP7_LIGHT_INBATTLE_CONFIGS = (
 Configs.COMP7_LIGHT_CONFIG.value,)
BATTLE_MODE_VEH_TAGS_EXCEPT_COMP7_LIGHT = constants.BATTLE_MODE_VEHICLE_TAGS - {'comp7_light'}

class ARENA_GUI_TYPE(constants.ARENA_GUI_TYPE, ConstInjector):
    COMP7_LIGHT = 35


class PREBATTLE_TYPE(constants.PREBATTLE_TYPE, ConstInjector):
    COMP7_LIGHT = 27


class INVITATION_TYPE(constants.INVITATION_TYPE, ConstInjector):
    COMP7_LIGHT = PREBATTLE_TYPE.COMP7_LIGHT


class UNIT_MGR_FLAGS(UnitBase.UNIT_MGR_FLAGS, ConstInjector):
    COMP7_LIGHT = 16777216


class ROSTER_TYPE(UnitBase.ROSTER_TYPE, ConstInjector):
    COMP7_LIGHT_ROSTER = UNIT_MGR_FLAGS.SQUAD | UNIT_MGR_FLAGS.COMP7_LIGHT


class GameSeasonType(constants.GameSeasonType, ConstInjector):
    COMP7_LIGHT = 9


class CLIENT_UNIT_CMD(UnitBase.CLIENT_UNIT_CMD, ConstInjector):
    SET_COMP7_LIGHT_SQUAD_SIZE = 4302
