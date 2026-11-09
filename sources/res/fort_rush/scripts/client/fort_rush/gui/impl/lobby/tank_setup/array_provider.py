# wot-extractor: codigo DESCOMPILADO de sources/res/fort_rush/scripts/client/fort_rush/gui/impl/lobby/tank_setup/array_provider.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fort_rush/scripts/client/fort_rush/gui/impl/lobby/tank_setup/array_provider.py
from __future__ import absolute_import
from past.builtins import xrange
from gui.impl.lobby.tank_setup.array_providers.consumable import ConsumableDeviceProvider
from gui.shared.utils.requesters import REQ_CRITERIA
from items import ITEM_TYPES

class FortRushConsumableProvider(ConsumableDeviceProvider):

    def _getExcludeTags(self):
        vehicle = self._getVehicle()
        if vehicle is None:
            return frozenset()
        else:
            supplySlots = vehicle.descriptor.type.supplySlots
            excludeTags = set()
            for idx in xrange(supplySlots.getAmountForType(ITEM_TYPES.equipment)):
                slot = supplySlots.getSlotByIdxInItemType(ITEM_TYPES.equipment, idx)
                excludeTags.update(getattr(slot, 'excludeTags', ()))

            return frozenset(excludeTags)

    def _getItemCriteria(self):
        criteria = super(FortRushConsumableProvider, self)._getItemCriteria()
        excludeTags = self._getExcludeTags()
        if not excludeTags:
            return criteria
        return criteria | ~REQ_CRITERIA.VEHICLE.HAS_ANY_TAG(excludeTags)
