# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/prb_control/entities/base/legacy/listener.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/prb_control/entities/base/legacy/listener.py
from gui.prb_control.entities.base.listener import IPrbListener

class ILegacyIntroListener(IPrbListener):

    def onLegacyListReceived(self, prebattles):
        pass

    def onLegacyRosterReceived(self, prebattleID, iterator):
        pass


class ILegacyListener(ILegacyIntroListener):

    def onSettingUpdated(self, entity, settingName, settingValue):
        pass

    def onPropertyUpdated(self, entity, propertyName, propertyValue):
        pass

    def onTeamStatesReceived(self, entity, team1State, team2State):
        pass

    def onPlayerAdded(self, entity, playerInfo):
        pass

    def onPlayerRemoved(self, entity, playerInfo):
        pass

    def onRostersChanged(self, entity, rosters, full):
        pass

    def onPlayerTeamNumberChanged(self, entity, team):
        pass

    def onPlayerRosterChanged(self, entity, actorInfo, playerInfo):
        pass

    def onPlayerStateChanged(self, entity, roster, accountInfo):
        pass
