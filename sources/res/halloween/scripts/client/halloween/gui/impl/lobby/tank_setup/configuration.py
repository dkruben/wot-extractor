# wot-extractor: codigo DESCOMPILADO de sources/res/halloween/scripts/client/halloween/gui/impl/lobby/tank_setup/configuration.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: halloween/scripts/client/halloween/gui/impl/lobby/tank_setup/configuration.py
from __future__ import absolute_import
from gui.impl.lobby.tank_setup.configurations.consumable import ConsumableTabsController, ConsumableTabs
from halloween.gui.impl.lobby.tank_setup.array_provider import HalloweenConsumableProvider

class HalloweenTabsController(ConsumableTabsController):
    __slots__ = ()

    def _getAllProviders(self):
        return {(ConsumableTabs.DEFAULT): HalloweenConsumableProvider}
