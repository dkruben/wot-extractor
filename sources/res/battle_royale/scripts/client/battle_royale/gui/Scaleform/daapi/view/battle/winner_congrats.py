# wot-extractor: codigo DESCOMPILADO de sources/res/battle_royale/scripts/client/battle_royale/gui/Scaleform/daapi/view/battle/winner_congrats.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/Scaleform/daapi/view/battle/winner_congrats.py
from __future__ import absolute_import
import BigWorld
from battle_royale.gui.battle_control.controllers.br_battle_sounds import BREvents
from gui.Scaleform.daapi.view.meta.BattleRoyaleWinnerCongratsMeta import BattleRoyaleWinnerCongratsMeta
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider
from skeletons.gui.game_control import IBattleRoyaleController

class BattleRoyaleWinnerCongrats(BattleRoyaleWinnerCongratsMeta):
    __battleRoyaleController = dependency.descriptor(IBattleRoyaleController)
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def playWinSound(self):
        BREvents.playSound(BREvents.BATTLE_WIN)

    def _populate(self):
        super(BattleRoyaleWinnerCongrats, self)._populate()
        self.__winnerStpCoins = self.__battleRoyaleController.getStpCoinsPerPlace(1)
        deathScreenCtrl = self.__sessionProvider.dynamic.deathScreen
        if deathScreenCtrl:
            deathScreenCtrl.onWinnerScreen += self.__onWinnerScreen

    def _destroy(self):
        deathScreenCtrl = self.__sessionProvider.dynamic.deathScreen
        if deathScreenCtrl:
            deathScreenCtrl.onWinnerScreen -= self.__onWinnerScreen
        super(BattleRoyaleWinnerCongrats, self)._destroy()

    def __onWinnerScreen(self):
        BREvents.playSound(BREvents.BATTLE_WIN)
        if self.__battleRoyaleController.isStPatrick():
            self.__setStpCoins()

    def __setStpCoins(self):
        vehicle = BigWorld.entity(BigWorld.player().playerVehicleID)
        stPatrickComp = vehicle.dynamicComponents.get('vehicleBRStPatrickComponent')
        if stPatrickComp:
            brComponent = self.__sessionProvider.arenaVisitor.getComponentSystem().battleRoyaleComponent
            self.as_setStpCoinsS(initial=stPatrickComp.totalCoins, factor=brComponent.dailyBonusFactor, bonus=self.__winnerStpCoins)
