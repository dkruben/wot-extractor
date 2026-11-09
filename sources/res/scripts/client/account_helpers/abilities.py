# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/account_helpers/abilities.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/account_helpers/abilities.py
from __future__ import absolute_import
from builtins import range
import AccountCommands
from items.abilities_manager import AbilitiesManager

class AbilitiesHelper(object):

    def __init__(self):
        self.__account = None
        self.__ignore = True
        self.__abilities = AbilitiesManager()
        return

    def onAccountBecomePlayer(self):
        self.__ignore = False

    def onAccountBecomeNonPlayer(self):
        self.__ignore = True

    def setAccount(self, account):
        self.__account = account

    @property
    def abilitiesManager(self):
        return self.__abilities

    def addPerks(self, battle, vehicleID, scopeIndex, perksList, callback=None):
        if battle:
            if self.__ignore:
                if callback is not None:
                    callback(AccountCommands.RES_NON_PLAYER)
                return
            if callback is not None:
                proxy = lambda requestID, resultID, errorStr, ext={}: callback(resultID)
            else:
                proxy = None
            perksListRes = [
             vehicleID, scopeIndex]
            perksListRes.extend(perksList)
            self.__account._doCmdIntArr(AccountCommands.CMD_ADD_PERK_TO_BATTLE, perksListRes, proxy)
        else:
            perks = {perksList[i]: perksList[i + 1] for i in range(0, len(perksList), 2)}
            self.abilitiesManager.addBuild(vehicleID, 'debug' + str(scopeIndex), perks)
        return

    def resetPerks(self, battle, vehicleID, callback=None):
        if battle:
            if self.__ignore:
                if callback is not None:
                    callback(AccountCommands.RES_NON_PLAYER)
                return
            if callback is not None:
                proxy = lambda requestID, resultID, errorStr, ext={}: callback(resultID)
            else:
                proxy = None
            self.__account._doCmdInt2(AccountCommands.CMD_RESET_PERK_FOR_BATTLE, vehicleID, 0, proxy)
        else:
            self.abilitiesManager.removePerksByVehicle(vehicleID)
        return
