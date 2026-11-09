# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/profile/ProfileTotalPage.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/profile/ProfileTotalPage.py
from __future__ import absolute_import
from gui.Scaleform.framework.entities.inject_component_adaptor import InjectComponentAdaptor
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.impl.lobby.achievements.achievements_main_view import AchievementMainView, AchievementsViewCtx

class ProfileTotalPage(InjectComponentAdaptor):

    def __init__(self, *args):
        self.__userID = args[1]
        if len(args) > 3 and args[3]:
            self.__closeCallback = args[3].get('closeCallback')
        else:
            self.__closeCallback = None
        super(ProfileTotalPage, self).__init__()
        return

    def _makeInjectView(self):
        ctx = AchievementsViewCtx(menuName=VIEW_ALIAS.PROFILE_TOTAL_PAGE, userID=self.__userID, closeCallback=self.__closeCallback)
        self.__view = AchievementMainView(ctx)
        return self.__view

    def onSectionActivated(self):
        pass

    def onSectionDeactivated(self):
        pass
