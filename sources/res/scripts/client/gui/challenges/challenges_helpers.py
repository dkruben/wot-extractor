# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/challenges/challenges_helpers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/challenges/challenges_helpers.py
from __future__ import absolute_import
from account_helpers import AccountSettings
from account_helpers.AccountSettings import ChallengesMissions
from gui import GUI_SETTINGS
from helpers import time_utils
TIME_BEFORE_END_OF_EXPIRATION = time_utils.ONE_DAY + time_utils.ONE_MINUTE

def getSettings(settingName, defaultValue=None):
    settings = AccountSettings.getSettings(ChallengesMissions.SETTINGS)
    return settings.get(settingName, defaultValue)


def setSettings(settingName, value):
    settings = AccountSettings.getSettings(ChallengesMissions.SETTINGS)
    settings[settingName] = value
    AccountSettings.setSettings(ChallengesMissions.SETTINGS, settings)


def setVisitedChallenge(challengeID):
    settings = AccountSettings.getSettings(ChallengesMissions.SETTINGS)
    settings[ChallengesMissions.VISITED_CHALLENGES].add(challengeID)
    AccountSettings.setSettings(ChallengesMissions.SETTINGS, settings)


def getChallengesInfoUrl():
    return ('').join((GUI_SETTINGS.baseUrls['webBridgeRootURL'], GUI_SETTINGS.challenges['info']))
