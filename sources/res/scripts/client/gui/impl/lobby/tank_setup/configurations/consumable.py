# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/tank_setup/configurations/consumable.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/tank_setup/configurations/consumable.py
from gui.impl.common.tabs_controller import tabUpdateFunc
from gui.impl.lobby.tank_setup.configurations.base import BaseTankSetupTabsController
from gui.impl.lobby.tank_setup.array_providers.consumable import ConsumableDeviceProvider

class ConsumableTabs(object):
    DEFAULT = 'default'
    ALL = (
     DEFAULT,)


class ConsumableTabsController(BaseTankSetupTabsController):
    __slots__ = ()

    def getDefaultTab(self):
        return ConsumableTabs.DEFAULT

    @tabUpdateFunc(ConsumableTabs.DEFAULT)
    def _updateDefault(self, viewModel, isFirst=False):
        pass

    def tabOrderKey(self, tabName):
        return ConsumableTabs.ALL.index(tabName)

    def _getAllProviders(self):
        return {(ConsumableTabs.DEFAULT): ConsumableDeviceProvider}
