# wot-extractor: codigo DESCOMPILADO de sources/res/fort_rush/scripts/common/fort_rush_common/items/fr_supply_slots_components.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fort_rush/scripts/common/fort_rush_common/items/fr_supply_slots_components.py
from __future__ import absolute_import
from items import vehicles
from items.components.supply_slots_components import EquipmentSlot

class FortRushEquipmentSlot(EquipmentSlot):
    __slots__ = ('excludeTags', )

    def __init__(self):
        super(FortRushEquipmentSlot, self).__init__()
        self.excludeTags = frozenset()

    def readFromSection(self, section):
        super(FortRushEquipmentSlot, self).readFromSection(section)
        self.excludeTags = frozenset(section.readString('excludeTags').split())

    def _checkSlotCompatibility(self, parsedCompDescr=None, descr=None):
        item = descr
        if item is None:
            _, _, itemID = parsedCompDescr
            item = vehicles.g_cache.equipments()[itemID]
        itemTags = getattr(item, 'tags', frozenset())
        excluded = self.excludeTags.intersection(itemTags)
        if excluded:
            return (False,
             ('Equipment tags ({}) are excluded from this slot ({})').format(sorted(itemTags), sorted(excluded)))
        else:
            return super(FortRushEquipmentSlot, self)._checkSlotCompatibility(parsedCompDescr, descr)
