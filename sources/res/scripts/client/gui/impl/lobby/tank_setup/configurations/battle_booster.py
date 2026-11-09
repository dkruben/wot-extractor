# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/tank_setup/configurations/battle_booster.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/tank_setup/configurations/battle_booster.py
from gui.impl.common.tabs_controller import tabUpdateFunc
from gui.impl.lobby.tank_setup.array_providers.battle_booster import OptDeviceBattleBoosterProvider, CrewBattleBoosterProvider
from gui.impl.lobby.tank_setup.configurations.base import BaseTankSetupTabsController

class BattleBoosterTabs(object):
    OPT_DEVICE = 'optDevice'
    CREW = 'crew'
    ALL = (
     OPT_DEVICE, CREW)


class BattleBoostersTabsController(BaseTankSetupTabsController):
    __slots__ = ()

    def getDefaultTab(self):
        return BattleBoosterTabs.OPT_DEVICE

    @tabUpdateFunc(BattleBoosterTabs.OPT_DEVICE)
    def _updateOptDevice(self, viewModel, isFirst=False):
        pass

    @tabUpdateFunc(BattleBoosterTabs.CREW)
    def _updateCrew(self, viewModel, isFirst=False):
        pass

    def tabOrderKey(self, tabName):
        return BattleBoosterTabs.ALL.index(tabName)

    def _getAllProviders(self):
        return {(BattleBoosterTabs.OPT_DEVICE): OptDeviceBattleBoosterProvider, 
           (BattleBoosterTabs.CREW): CrewBattleBoosterProvider}
