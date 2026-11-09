# wot-extractor: codigo DESCOMPILADO de sources/res/last_stand/scripts/common/last_stand_common/items/ls_artefacts.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: last_stand/scripts/common/last_stand_common/items/ls_artefacts.py
from __future__ import absolute_import
from typing import TYPE_CHECKING
from collections import namedtuple
from items.artefacts import DynComponentsGroupEquipment
from items import _xml
from last_stand_common.ls_utils import formatVehicleInfoString
if TYPE_CHECKING:
    from items.vehicles import VehicleDescriptor
LSEquipmentVariant = namedtuple('LSEquipmentVariant', ('id', 'cooldownSeconds', 'durationSeconds',
                                                       'usageCost', 'equipmentItem',
                                                       'dynComponentsGroups'))

class LSEquipment(DynComponentsGroupEquipment):
    __slots__ = ('equipmentItem', 'usageCost', 'variantIdFormat', 'variants', '_fallbackVariant')

    def _readConfig(self, xmlCtx, scriptSection):
        super(LSEquipment, self)._readConfig(xmlCtx, scriptSection)
        section = scriptSection
        self.equipmentItem = _xml.readString(xmlCtx, section, 'equipmentItem') if section.has_key('equipmentItem') else None
        self.usageCost = _xml.readFloat(xmlCtx, section, 'usageCost')
        self.variantIdFormat = section.readString('variantIdFormat') if section.has_key('variantIdFormat') else None
        variants = _xml.getChildren(xmlCtx, section, 'variants', throwIfMissing=False)
        self.variants = {_xml.readString(xmlCtx, variant, 'id'): self._readVariant(xmlCtx, variant) for _, variant in variants}
        self._fallbackVariant = LSEquipmentVariant(id='', cooldownSeconds=self.cooldownSeconds, durationSeconds=self.durationSeconds, usageCost=self.usageCost, equipmentItem=self.equipmentItem, dynComponentsGroups=self.dynComponentsGroups)
        return

    @property
    def fallbackVariant(self):
        return self._fallbackVariant

    def getVariant(self, vehTypeDescr):
        if not self.variants or self.variantIdFormat is None:
            return self._fallbackVariant
        else:
            return self.variants.get(formatVehicleInfoString(self.variantIdFormat, vehTypeDescr), self._fallbackVariant)

    @staticmethod
    def _readVariant(xmlCtx, section):
        return LSEquipmentVariant(id=_xml.readString(xmlCtx, section, 'id'), cooldownSeconds=_xml.readFloat(xmlCtx, section, 'cooldownSeconds'), durationSeconds=_xml.readFloat(xmlCtx, section, 'durationSeconds'), usageCost=_xml.readFloat(xmlCtx, section, 'usageCost'), equipmentItem=_xml.readString(xmlCtx, section, 'equipmentItem') if section.has_key('equipmentItem') else None, dynComponentsGroups=frozenset(_xml.readString(xmlCtx, section, 'dynComponentsGroups').split()))
