# wot-extractor: codigo DESCOMPILADO de sources/res/frontline/scripts/client/frontline/frontline_account_settings.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: frontline/scripts/client/frontline/frontline_account_settings.py
from __future__ import absolute_import
from account_helpers import AccountSettings
from frontline_common.constants import AccountSettingsKeys, ACCOUNT_DEFAULT_SETTINGS

def getSettings(name):
    settings = AccountSettings.getSettings(AccountSettingsKeys.EVENT_KEY)
    return settings.get(name, ACCOUNT_DEFAULT_SETTINGS[AccountSettingsKeys.EVENT_KEY].get(name))


def setSettings(name, value):
    settings = AccountSettings.getSettings(AccountSettingsKeys.EVENT_KEY)
    settings[name] = value
    AccountSettings.setSettings(AccountSettingsKeys.EVENT_KEY, settings)


def getSkillPointsShown(seasonId):
    data = getSettings(AccountSettingsKeys.SKILL_POINTS_SHOWN)
    return data.get(seasonId, None)


def setSkillPointsShown(seasonId, pointsAmount):
    return setSettings(AccountSettingsKeys.SKILL_POINTS_SHOWN, {seasonId: pointsAmount})


def isWelcomeScreenViewed(seasonId):
    data = getSettings(AccountSettingsKeys.WELCOME_SCREEN_VIEWED)
    return data.get(seasonId, False)


def setWelcomeScreenViewed(seasonId):
    return setSettings(AccountSettingsKeys.WELCOME_SCREEN_VIEWED, {seasonId: True})


def isRentBannerClicked():
    return getSettings(AccountSettingsKeys.RENT_BANNER_CLICKED)


def setRentBannerClicked():
    return setSettings(AccountSettingsKeys.RENT_BANNER_CLICKED, True)


def getReceivedRewardTokens():
    return getSettings(AccountSettingsKeys.REWARD_TOKENS_RECEIVED)


def setReceivedRewardTokens(tokens):
    setSettings(AccountSettingsKeys.REWARD_TOKENS_RECEIVED, tokens)
