# wot-extractor: codigo DESCOMPILADO de sources/res/fun_random/scripts/common/fun_random_common/fun_constants_utils.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fun_random/scripts/common/fun_random_common/fun_constants_utils.py
from __future__ import absolute_import
from future.utils import viewvalues
from constants import QUEUE_TYPE
from constants_utils import addQueueTypesFromExtension
from fun_random_common.fun_constants import ARENA_GUI_TYPE, FunSubModeImpl, FunProgressionCondition

def addArenaGuiTypesFromExtensionToFunRange(extArenaGuiType):
    extraAttrs = extArenaGuiType.getExtraAttrs()
    extraValues = tuple(viewvalues(extraAttrs))
    ARENA_GUI_TYPE.FUN_RANDOM_RANGE += extraValues


def addFunRandomSubModeImpl(extSubModeImpl, personality):
    extraAttrs = extSubModeImpl.getExtraAttrs()
    extraValues = tuple(viewvalues(extraAttrs))
    extSubModeImpl.inject(personality)
    FunSubModeImpl.ALL += extraValues


def addFunProgressionConditions(extConditions, personality):
    extraAttrs = extConditions.getExtraAttrs()
    extraValues = tuple(viewvalues(extraAttrs))
    extConditions.inject(personality)
    FunProgressionCondition.ALL += extraValues


def addFunRandomQueueTypesFromExtension(extQueueType, personality):
    extraAttrs = extQueueType.getExtraAttrs()
    extraValues = tuple(viewvalues(extraAttrs))
    QUEUE_TYPE.FUN_RANDOM_RANGE += extraValues
    addQueueTypesFromExtension(extQueueType, personality)
