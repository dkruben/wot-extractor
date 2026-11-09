# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/shared/gui_items/dossier/achievements/validators.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/validators.py
from __future__ import absolute_import
from future.utils import itervalues
from constants import IS_WEB
if IS_WEB:

    def questHasThisAchievementAsBonus(name, block):
        return False


    def alreadyAchieved(achievementClass, name, block, dossier):
        return False


    def requiresFortification():
        return False


    def requiresReferralProgram():
        return False


    def accountIsRoaming(dossier):
        return False


else:
    from helpers import dependency
    from skeletons.gui.lobby_context import ILobbyContext
    from skeletons.gui.server_events import IEventsCache

    def questHasThisAchievementAsBonus(name, block):
        eventsCache = dependency.instance(IEventsCache)
        return any((block, name) in records for records in itervalues(eventsCache.getQuestsDossierBonuses()))


    def alreadyAchieved(achievementClass, name, block, dossier):
        return achievementClass.checkIsInDossier(block, name, dossier)


    def requiresFortification():
        lobbyContext = dependency.instance(ILobbyContext)
        return lobbyContext.getServerSettings() is not None and lobbyContext.getServerSettings().isStrongholdsEnabled()


    def requiresReferralProgram():
        lobbyContext = dependency.instance(ILobbyContext)
        return lobbyContext.getServerSettings() is not None and lobbyContext.getServerSettings().isReferralProgramEnabled()


    def accountIsRoaming(dossier):
        return dossier.isInRoaming()
