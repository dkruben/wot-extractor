# wot-extractor: codigo DESCOMPILADO de sources/res/fun_random/scripts/common/fun_random_common/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fun_random/scripts/common/fun_random_common/__init__.py
from __future__ import absolute_import
import constants
from constants_utils import addArenaGuiTypesFromExtension, initSquadCommonTypes, addArenaBonusTypesFromExtension
from fun_random_common import fun_constants

def injectConsts(personality):
    addArenaGuiTypesFromExtension(fun_constants.ARENA_GUI_TYPE, personality)
    addArenaBonusTypesFromExtension(fun_constants.ARENA_BONUS_TYPE, personality)
    constants.INBATTLE_CONFIGS.append(fun_constants.FUN_GAME_PARAMS_KEY)


def injectSquadConsts(personality):
    initSquadCommonTypes(fun_constants, personality)
    constants.INVITATION_TYPE.TYPES_WITH_EXTRA_DATA += (fun_constants.INVITATION_TYPE.FUN_RANDOM,)
