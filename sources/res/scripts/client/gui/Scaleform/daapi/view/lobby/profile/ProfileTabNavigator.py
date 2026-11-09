# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/profile/ProfileTabNavigator.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/profile/ProfileTabNavigator.py
from __future__ import absolute_import
from future.utils import viewvalues
from gui.Scaleform.daapi.view.lobby.profile.ProfileSection import ProfileSection
from gui.Scaleform.daapi.view.meta.ProfileTabNavigatorMeta import ProfileTabNavigatorMeta
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.impl.lobby.achievements.achievements_main_view import AchievementsViewCtx
from gui.shared import events, g_eventBus, EVENT_BUS_SCOPE

class ProfileTabNavigator(ProfileTabNavigatorMeta):
    gf_views_map = [
     VIEW_ALIAS.PROFILE_TOTAL_PAGE, VIEW_ALIAS.PROFILE_ACHIEVEMENTS_PAGE]

    def __init__(self, *args):
        ProfileTabNavigatorMeta.__init__(self)
        self.__userName = args[0]
        self.__userID = args[1]
        self.__databaseID = args[2]
        self.__navigatorOwnInitInfo = args[3]
        self.__selectedData = None
        if len(args) > 4 and args[4]:
            self.__selectedData = args[4]
        self.tabId = None
        return

    def invokeUpdate(self):
        for component in viewvalues(self.components):
            if isinstance(component, ProfileSection):
                component.invokeUpdate()

    def _populate(self):
        super(ProfileTabNavigator, self)._populate()
        self.as_setInitDataS(self.__navigatorOwnInitInfo)

    def registerFlashComponent(self, component, alias, *args):
        super(ProfileTabNavigator, self).registerFlashComponent(component, alias, self.__userName, self.__userID, self.__databaseID, self.__selectedData)

    def onTabChange(self, tabId):
        self.__safeCall(self.components.get(self.tabId), 'onSectionDeactivated')
        self.tabId = tabId
        self.__safeCall(self.components.get(self.tabId), 'onSectionActivated')

    def onViewReady(self, alias):
        if alias in self.gf_views_map:
            closeCallback = self.__selectedData.get('closeCallback') if self.__selectedData else None
            g_eventBus.handleEvent(events.Achievements20Event(events.Achievements20Event.CHANGE_GF_VIEW, ctx=AchievementsViewCtx(menuName=alias, userID=self.__userID, closeCallback=closeCallback)), scope=EVENT_BUS_SCOPE.LOBBY)
        return

    @staticmethod
    def __safeCall(obj, attrName, *args, **kwargs):
        return getattr(obj, attrName, (lambda *__, **_: None))(*args, **kwargs)
