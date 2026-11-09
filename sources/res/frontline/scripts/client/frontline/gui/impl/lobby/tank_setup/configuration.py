# wot-extractor: codigo DESCOMPILADO de sources/res/frontline/scripts/client/frontline/gui/impl/lobby/tank_setup/configuration.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: frontline/scripts/client/frontline/gui/impl/lobby/tank_setup/configuration.py
from __future__ import absolute_import
from frontline.gui.impl.lobby.tank_setup.array_provider import BattleAbilityProvider
from gui.impl.common.tabs_controller import tabUpdateFunc
from gui.impl.lobby.tank_setup.configurations.base import BaseTankSetupTabsController, BaseDealPanel

class EpicBattleTabs(object):
    BATTLE_ABILITY = 'battleAbility'
    ALL = (
     BATTLE_ABILITY,)


class EpicBattleTabsController(BaseTankSetupTabsController):
    __slots__ = ()

    def getDefaultTab(self):
        return EpicBattleTabs.BATTLE_ABILITY

    @tabUpdateFunc(EpicBattleTabs.BATTLE_ABILITY)
    def _updateOptDevice(self, viewModel, isFirst=False):
        pass

    def tabOrderKey(self, tabName):
        return EpicBattleTabs.ALL.index(tabName)

    def _getAllProviders(self):
        return {(EpicBattleTabs.BATTLE_ABILITY): BattleAbilityProvider}


class EpicBattleDealPanel(BaseDealPanel):

    @classmethod
    def updateDealPanelPrice(cls, vehicle, items, dealPanelModel):
        pass
