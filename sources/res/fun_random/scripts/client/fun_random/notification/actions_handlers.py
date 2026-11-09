# wot-extractor: codigo DESCOMPILADO de sources/res/fun_random/scripts/client/fun_random/notification/actions_handlers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fun_random/scripts/client/fun_random/notification/actions_handlers.py
from __future__ import absolute_import
from adisp import adisp_process
from fun_random.gui.feature.util.fun_mixins import FunSubModesWatcher, FunProgressionWatcher
from fun_random.gui.feature.util.fun_wrappers import hasMultipleSubModes
from helpers import dependency
from notification.actions_handlers import NavigationDisabledActionHandler
from notification.settings import NOTIFICATION_TYPE
from skeletons.gui.lobby_context import ILobbyContext

class SelectFunRandomMode(NavigationDisabledActionHandler, FunSubModesWatcher):
    __lobbyContext = dependency.descriptor(ILobbyContext)

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    @classmethod
    def getActions(cls):
        return ('selectFunRandomMode', )

    @hasMultipleSubModes(defReturn=True)
    def checkHeaderNavigation(self):
        return False

    @adisp_process
    def doAction(self, model, entityID, action):
        navigationPossible = True
        if self.checkHeaderNavigation():
            navigationPossible = yield self.__lobbyContext.isHeaderNavigationPossible()
        if navigationPossible:
            yield self.selectFunRandomBattle()


class ShowFunRandomProgression(NavigationDisabledActionHandler, FunProgressionWatcher):

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    @classmethod
    def getActions(cls):
        return ('showFunRandomProgression', )

    def doAction(self, model, entityID, action):
        self.showActiveProgressionPage()
