# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/vehicle_compare/consumable.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/vehicle_compare/consumable.py
from gui.Scaleform.daapi.view.lobby.vehicle_compare import cmp_helpers
from gui.impl.lobby.tank_setup.array_providers.consumable import ConsumableDeviceProvider
from gui.impl.lobby.tank_setup.configurations.consumable import ConsumableTabsController, ConsumableTabs
from gui.impl.lobby.vehicle_compare.base_sub_view import CompareBaseSetupSubView

class CompareConsumableDeviceProvider(ConsumableDeviceProvider):

    def _fillStatus(self, model, item, slotID):
        super(CompareConsumableDeviceProvider, self)._fillStatus(model, item, slotID)
        if item.name in cmp_helpers.NOT_AFFECTED_EQUIPMENTS:
            model.setIsLocked(True)

    def _fillBuyPrice(self, *args, **kwargs):
        pass

    def _fillBuyStatus(self, model, item, isInstalledOrMounted):
        pass


class _CompareConsumableTabsController(ConsumableTabsController):

    def _getAllProviders(self):
        return {(ConsumableTabs.DEFAULT): CompareConsumableDeviceProvider}


class CompareConsumableSetupSubView(CompareBaseSetupSubView):

    def _createTabsController(self):
        return _CompareConsumableTabsController()
