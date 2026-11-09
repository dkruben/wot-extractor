# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/shared/gui_items/customization/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/gui_items/customization/__init__.py
from __future__ import absolute_import
from collections import namedtuple
from items.components.c11n_constants import ProjectionDecalDirectionTags
from shared_utils import first

def directionByTag(tags):
    directionTags = (tag for tag in tags if tag.startswith(ProjectionDecalDirectionTags.PREFIX))
    return first(directionTags, ProjectionDecalDirectionTags.ANY)


def isNeedToMirrorProjectionDecal(item, slot):
    if not item.canBeMirroredHorizontally:
        return False
    itemDirection = directionByTag(item.tags)
    slotDirection = directionByTag(slot.tags)
    if itemDirection == ProjectionDecalDirectionTags.ANY or slotDirection == ProjectionDecalDirectionTags.ANY:
        return False
    return itemDirection != slotDirection


CustomizationTooltipContext = namedtuple('CustomizationTooltipContext', ('itemCD',
                                                                         'vehicleIntCD',
                                                                         'showInventoryBlock',
                                                                         'level',
                                                                         'showOnlyProgressBlock',
                                                                         'skipQuestValidation',
                                                                         'context'))
CustomizationTooltipContext.__new__.__defaults__ = (
 -1, -1, False, -1, False, False, None)
C11nStyleProgressData = namedtuple('C11nStyleProgressData', ('styleID', 'branch', 'level'))
C11nStyleProgressData.__new__.__defaults__ = (-1, -1, -1)
