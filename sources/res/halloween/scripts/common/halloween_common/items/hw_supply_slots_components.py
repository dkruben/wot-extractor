# wot-extractor: codigo DESCOMPILADO de sources/res/halloween/scripts/common/halloween_common/items/hw_supply_slots_components.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: halloween/scripts/common/halloween_common/items/hw_supply_slots_components.py
from __future__ import absolute_import
from items.components.supply_slots_components import EquipmentSlot
from items.vehicles import getItemByCompactDescr

class HWEquipmentSlot(EquipmentSlot):

    def readFromSection(self, section):
        super(HWEquipmentSlot, self).readFromSection(section)
        self.tags = frozenset(section.readString('tags').split())

    def _checkSlotCompatibility(self, parsedCompDescr=None, descr=None):
        item = descr or getItemByCompactDescr(parsedCompDescr)
        eqTags = getattr(item, 'tags', set())
        if self.tags and not eqTags.intersection(self.tags):
            return (False, ('Equipment tags ({}) does not contain any of slot tags ({})').format(eqTags, self.tags))
        return super(HWEquipmentSlot, self)._checkSlotCompatibility(parsedCompDescr, descr)
