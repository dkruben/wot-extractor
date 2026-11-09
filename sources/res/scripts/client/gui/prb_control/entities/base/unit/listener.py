# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/prb_control/entities/base/unit/listener.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/prb_control/entities/base/unit/listener.py
from gui.prb_control.entities.base.listener import IPrbListener

class IUnitIntroListener(IPrbListener):

    def onUnitAutoSearchStarted(self, timeLeft):
        pass

    def onUnitAutoSearchFinished(self):
        pass

    def onUnitAutoSearchSuccess(self, acceptDelta):
        pass

    def onUnitBrowserErrorReceived(self, errorCode):
        pass


class IUnitListener(IUnitIntroListener):

    def onUnitFlagsChanged(self, flags, timeLeft):
        pass

    def onUnitPlayerStateChanged(self, pInfo):
        pass

    def onUnitPlayerRolesChanged(self, pInfo, pPermissions):
        pass

    def onUnitPlayerOnlineStatusChanged(self, pInfo):
        pass

    def onUnitPlayerBecomeCreator(self, pInfo):
        pass

    def onUnitPlayerNoLongerCreator(self, pInfo):
        pass

    def onUnitPlayerEnterOrLeaveArena(self, pInfo):
        pass

    def onUnitRosterChanged(self):
        pass

    def onUnitMembersListChanged(self):
        pass

    def onUnitPlayerAdded(self, pInfo):
        pass

    def onUnitPlayerInfoChanged(self, pInfo):
        pass

    def onUnitPlayerRemoved(self, pInfo):
        pass

    def onUnitPlayersListChanged(self):
        pass

    def onUnitVehiclesChanged(self, dbID, vInfos):
        pass

    def onUnitPlayerVehDictChanged(self, pInfo):
        pass

    def onUnitSettingChanged(self, opCode, value):
        pass

    def onUnitRejoin(self):
        pass

    def onUnitErrorReceived(self, errorCode):
        pass

    def onUnitExtraChanged(self, extra):
        pass

    def onUnitSizeChanged(self):
        pass

    def onUnitCurfewChanged(self):
        pass

    def onUnitPlayerProfileVehicleChanged(self, accountDBID):
        pass

    def onUnitSearchFlagsChanged(self, flags):
        pass


class IStrongholdListener(IPrbListener):

    def onUpdateHeader(self, header, isFirstBattle, isUnitFreezed):
        pass

    def onUpdateTimer(self, timer):
        pass

    def onUpdateState(self, state):
        pass

    def onUpdateReserve(self, reserve, reserveOrder):
        pass

    def onStrongholdDataChanged(self, header, isFirstBattle, reserve, reserveOrder):
        pass

    def onStrongholdOnReadyStateChanged(self):
        pass

    def onStrongholdMaintenance(self, state):
        pass

    def onCommanderIsReady(self, isReady):
        pass

    def onStrongholdDoBattleQueue(self, isFirstBattle, readyButtonEnabled, reserveOrder):
        pass

    def onPlayersMatching(self, isPlayersMatchingInProgress):
        pass

    def onSlotVehileFiltersChanged(self):
        pass

    def onEventFrozenVehiclesChanged(self, data):
        pass
