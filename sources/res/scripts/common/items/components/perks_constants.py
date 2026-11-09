# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/items/components/perks_constants.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/items/components/perks_constants.py
from __future__ import absolute_import
import typing
from functools import reduce
PERKS_XML_FILE = 'perks.xml'
PERK_BONUS_VALUE_PRECISION = 5
POINT_BLAST_DISTANCE = 50
SKIP_SE_PERKS = ('commander_sixthSense', )

class PerkState(object):
    INACTIVE = 0
    ACTIVE = 1


class PerkTags(object):
    AUTOPERK = 4

    @classmethod
    def pack(cls, tags):
        return reduce(int.__or__, (getattr(cls, tag.upper()) for tag in tags), 0)


class PerkMasks(object):
    PERK_ID_MASK = 1023
    PERK_LEVEL_MASK = 63


class StubPerkIDs(object):
    COMMANDER_TUTOR = 103


class PerkIDs(object):
    LOADER_INTUITION = 403
