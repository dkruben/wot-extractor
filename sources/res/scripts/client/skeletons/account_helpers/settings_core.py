# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/skeletons/account_helpers/settings_core.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/skeletons/account_helpers/settings_core.py
from __future__ import absolute_import
import typing
if typing.TYPE_CHECKING:
    from account_helpers.settings_core.ServerSettingsManager import ServerSettingsManager

class ISettingsCache(object):
    onSyncStarted = None
    onSyncCompleted = None

    def init(self):
        raise NotImplementedError

    def isSynced(self):
        raise NotImplementedError

    def fini(self):
        raise NotImplementedError

    def clear(self):
        raise NotImplementedError

    @property
    def waitForSync(self):
        raise NotImplementedError

    @property
    def settings(self):
        raise NotImplementedError

    def update(self, callback=None):
        raise NotImplementedError

    def getSectionSettings(self, section, defaultValue=0):
        raise NotImplementedError

    def setSectionSettings(self, section, value):
        raise NotImplementedError

    def setSettings(self, settings):
        raise NotImplementedError

    def getSetting(self, key, defaultValue=0):
        raise NotImplementedError

    def getVersion(self, defaultValue=0):
        raise NotImplementedError

    def setVersion(self, value):
        raise NotImplementedError

    def delSettings(self, settings):
        raise NotImplementedError


class ISettingsCore(object):
    onOnceOnlyHintsChanged = None
    onSettingsChanged = None
    onSettingsApplied = None
    onSettingsReady = None
    isReady = property()

    def init(self):
        raise NotImplementedError

    def fini(self):
        raise NotImplementedError

    def clear(self):
        raise NotImplementedError

    @isReady.getter
    def isReady(self):
        raise NotImplementedError

    @property
    def options(self):
        raise NotImplementedError

    @property
    def storages(self):
        raise NotImplementedError

    @property
    def interfaceScale(self):
        raise NotImplementedError

    @property
    def serverSettings(self):
        raise NotImplementedError

    def packSettings(self, names):
        raise NotImplementedError

    def getSetting(self, name):
        raise NotImplementedError

    def getApplyMethod(self, diff):
        raise NotImplementedError

    def applySetting(self, key, value):
        raise NotImplementedError

    def previewSetting(self, name, value):
        raise NotImplementedError

    def applySettings(self, diff):
        raise NotImplementedError

    def revertSettings(self):
        raise NotImplementedError

    def isSettingChanged(self, name, value):
        raise NotImplementedError

    def applyStorages(self, restartApproved, force=False):
        raise NotImplementedError

    def confirmChanges(self, confirmators):
        raise NotImplementedError

    def clearStorages(self):
        raise NotImplementedError

    def setOverrideSettings(self, overrideDict, disableStorages):
        raise NotImplementedError

    def unsetOverrideSettings(self):
        raise NotImplementedError


class IBattleCommunicationsSettings(object):
    onChanged = None

    @property
    def isEnabled(self):
        raise NotImplementedError

    @property
    def showStickyMarkers(self):
        raise NotImplementedError

    @property
    def showInPlayerList(self):
        raise NotImplementedError

    @property
    def showCalloutMessages(self):
        raise NotImplementedError

    @property
    def showLocationMarkers(self):
        raise NotImplementedError

    @property
    def showBaseMarkers(self):
        raise NotImplementedError

    @property
    def showCommendationsFeedbackOnReceive(self):
        raise NotImplementedError

    def init(self):
        raise NotImplementedError

    def fini(self):
        raise NotImplementedError
