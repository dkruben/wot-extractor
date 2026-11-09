# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/customization/popovers/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/customization/popovers/__init__.py
from __future__ import absolute_import
from collections import namedtuple
from gui.Scaleform.daapi.view.lobby.customization.shared import TYPES_ORDER
ItemsGroupVO = namedtuple('ItemsGroupVO', ('userName', 'titleLabel', 'isTitle'))

class C11nPopoverItemData(object):
    __slots__ = ('item', 'season', 'slotsIds', 'isBase', 'isRemovable', 'isRemoved',
                 'isFromInventory')

    def __init__(self, item, season=None, isBase=False, isRemovable=False, isRemoved=False, isFromInventory=False):
        self.item = item
        self.season = season
        self.slotsIds = []
        self.isBase = isBase
        self.isRemovable = isRemovable
        self.isRemoved = isRemoved
        self.isFromInventory = isFromInventory


def orderKey(itemData):
    item = itemData.item
    typeOrder = TYPES_ORDER.index(item.itemTypeID)
    return (
     not itemData.isBase, itemData.isRemovable, typeOrder, item.intCD, not itemData.isFromInventory)
