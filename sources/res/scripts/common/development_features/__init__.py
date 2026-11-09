# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/development_features/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/development_features/__init__.py
from __future__ import absolute_import
from constants import ARENA_BONUS_TYPE, ARENA_BONUS_MASK
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS
from collections import namedtuple
from collections import Counter
_DevBonusTypeDefinition = namedtuple('_DevBonusTypeDefinition', ('name', 'bonusType',
                                                                 'caps'))
_DEV_BONUS_TYPE_DEFS = ()

def initDevBonusTypes():
    __validateDevBonusTypeDefinitions()
    for name, bonusType, caps in _DEV_BONUS_TYPE_DEFS:
        setattr(ARENA_BONUS_TYPE, name, bonusType)
        setattr(ARENA_BONUS_TYPE_CAPS, name, caps)
        ARENA_BONUS_TYPE.RANGE = ARENA_BONUS_TYPE.RANGE + (bonusType,)
        ARENA_BONUS_TYPE_CAPS._typeToCaps[bonusType] = caps

    ARENA_BONUS_MASK.TYPE_BITS = dict((name, 2 ** bonusType) for bonusType, name in enumerate(ARENA_BONUS_TYPE.RANGE[1:]))


def __validateDevBonusTypeDefinitions():
    names = [definition.name for definition in _DEV_BONUS_TYPE_DEFS]
    bonusTypes = [definition.bonusType for definition in _DEV_BONUS_TYPE_DEFS]
