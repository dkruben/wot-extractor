# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/vehicles/components/component_interfaces.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/vehicles/components/component_interfaces.py
from __future__ import absolute_import
from GenericComponents import COMPOSITION_ROOT_SLOT_NAME
from constants import DEFAULT_GUN_INSTALLATION_INDEX
from gui.shared.utils.decorators import ReprInjector
from items.components.gun_installation_components import GunInstallationSlot

@ReprInjector.simple(('getVehicleSlotName', 'slotName'))
class IVehicleSlotComponent(object):

    def getVehicleSlotName(self):
        return COMPOSITION_ROOT_SLOT_NAME


class IVehicleGunSlotComponent(IVehicleSlotComponent):

    def getGunInstallationIndex(self):
        return DEFAULT_GUN_INSTALLATION_INDEX

    def getVehicleSlotName(self):
        return GunInstallationSlot.getPartSlotNameByIndex(self.getGunInstallationIndex())
