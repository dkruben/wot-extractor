# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/account_helpers/settings_core/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/account_helpers/settings_core/__init__.py
from __future__ import absolute_import
from skeletons.account_helpers.settings_core import ISettingsCache, ISettingsCore, IBattleCommunicationsSettings

def getSettingsCoreConfig(manager):
    from account_helpers.settings_core.battle_communications_settings import BattleCommunicationSettings
    from account_helpers.settings_core.SettingsCache import SettingsCache
    from account_helpers.settings_core.SettingsCore import SettingsCore
    cache = SettingsCache()
    manager.addInstance(ISettingsCache, cache, finalizer='fini')
    core = SettingsCore()
    manager.addInstance(ISettingsCore, core, finalizer='fini')
    communications = BattleCommunicationSettings()
    manager.addInstance(IBattleCommunicationsSettings, communications, finalizer='fini')
    cache.init()
    core.init()
    communications.init()


def longToInt32(value):
    if 2147483648L <= value <= 4294967295L:
        value &= 2147483647
        value = int(value)
        value = ~value
        value ^= 2147483647
    return value
