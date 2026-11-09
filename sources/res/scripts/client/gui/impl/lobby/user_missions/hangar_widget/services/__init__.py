# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/user_missions/hangar_widget/services/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/user_missions/hangar_widget/services/__init__.py
from __future__ import absolute_import
import typing
from gui.prb_control.entities.listener import IGlobalListener
if typing.TYPE_CHECKING:
    from typing import List
    from gui.impl.lobby.user_missions.hangar_widget.plugins import IUserMissionPlugin

class IBattlePassService(IGlobalListener):
    onBattlePassChanged = None

    def startListening(self):
        raise NotImplementedError

    def stopListening(self):
        raise NotImplementedError

    def isVisible(self):
        raise NotImplementedError

    def finalize(self):
        raise NotImplementedError


class IEventsService(IGlobalListener):
    onEventsListChanged = None

    def startListening(self):
        raise NotImplementedError

    def stopListening(self):
        raise NotImplementedError

    def getEntries(self):
        raise NotImplementedError

    def getEntryData(self):
        raise NotImplementedError

    def updateEntries(self):
        raise NotImplementedError

    def finalize(self):
        raise NotImplementedError

    @property
    def isAvailable(self):
        raise NotImplementedError


class IMissionsService(IGlobalListener):
    onMissionsChanged = None

    def startListening(self):
        raise NotImplementedError

    def stopListening(self):
        raise NotImplementedError

    def isVisible(self):
        raise NotImplementedError

    def finalize(self):
        raise NotImplementedError


class IPersonalMissionsService(IMissionsService):
    onPersonalMissionsChanged = None
    onWidgetQuestIDMarkedAsNew = None
    onServicePMSyncCompleted = None

    def clearWidgetQuestIDMarkedAsNew(self):
        raise NotImplementedError

    def setWidgetQuestIDMarkedAsNew(self, questID, doUpdateWidget=True):
        raise NotImplementedError

    def getWidgetQuestIDMarkedAsNew(self):
        raise NotImplementedError


class IMissionsContainerService(IGlobalListener):
    onShowPlugin = None
    onHidePlugin = None

    def setPluginVisibility(self, viewAlias, visible):
        raise NotImplementedError

    def getVisiblePlugins(self):
        raise NotImplementedError

    def isPluginVisible(self, viewAlias):
        raise NotImplementedError

    def getSelectedSlide(self, sliderId):
        raise NotImplementedError

    def onSlideChanged(self, selectedSlide):
        raise NotImplementedError

    def finalize(self):
        raise NotImplementedError


class IUserMissionWidgetService(object):
    onVisibleGroupsChanged = None

    def setGroupVisibility(self, groupName, isVisible):
        raise NotImplementedError

    def getVisibleGroups(self):
        raise NotImplementedError

    def isGroupVisible(self, groupName):
        raise NotImplementedError

    def finalize(self):
        raise NotImplementedError
