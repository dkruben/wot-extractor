# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/shared/account_settings_helper.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/account_settings_helper.py
from __future__ import absolute_import
from account_helpers import AccountSettings
from account_helpers.AccountSettings import GUI_START_BEHAVIOR
from helpers import dependency
from shared_utils import CONST_CONTAINER
from skeletons.account_helpers.settings_core import ISettingsCore

class WelcomeScreen(CONST_CONTAINER):
    CREW_NPS_WELCOME = 'crewNpsWelcome'


class AccountSettingsHelper(object):
    settingsCore = dependency.descriptor(ISettingsCore)

    @classmethod
    def welcomeScreenShown(cls, screen):
        defaults = AccountSettings.getFilterDefault(GUI_START_BEHAVIOR)
        settings = cls.settingsCore.serverSettings.getSection(GUI_START_BEHAVIOR, defaults)
        settings[screen] = True
        cls.settingsCore.serverSettings.setSectionSettings(GUI_START_BEHAVIOR, settings)

    @classmethod
    def isWelcomeScreenShown(cls, screen):
        settingsCore = dependency.instance(ISettingsCore)
        defaults = AccountSettings.getFilterDefault(GUI_START_BEHAVIOR)
        settings = settingsCore.serverSettings.getSection(GUI_START_BEHAVIOR, defaults)
        return settings.get(screen, False)
