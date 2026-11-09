# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/tutorial/gui/Scaleform/lobby/dispatcher.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/tutorial/gui/Scaleform/lobby/dispatcher.py
from __future__ import absolute_import
from gui.Scaleform.Waiting import Waiting
from gui.shared import g_eventBus, EVENT_BUS_SCOPE
from gui.shared.events import TutorialEvent
from tutorial.logger import LOG_MEMORY, LOG_ERROR
from tutorial.gui import GUIDispatcher

class SfLobbyDispatcher(GUIDispatcher):

    def __init__(self):
        super(SfLobbyDispatcher, self).__init__()
        self._exit = None
        return

    def __del__(self):
        LOG_MEMORY('SfLobbyDispatcher deleted')

    def start(self, loader):
        if not super(SfLobbyDispatcher, self).start(loader):
            return False
        addListener = g_eventBus.addListener
        addListener(TutorialEvent.START_TRAINING, self.__handleStartTraining, scope=EVENT_BUS_SCOPE.GLOBAL)
        addListener(TutorialEvent.STOP_TRAINING, self.__handleStopTraining, scope=EVENT_BUS_SCOPE.GLOBAL)
        return True

    def stop(self):
        if not super(SfLobbyDispatcher, self).stop():
            return False
        removeListener = g_eventBus.removeListener
        removeListener(TutorialEvent.START_TRAINING, self.__handleStartTraining, scope=EVENT_BUS_SCOPE.GLOBAL)
        removeListener(TutorialEvent.STOP_TRAINING, self.__handleStopTraining, scope=EVENT_BUS_SCOPE.GLOBAL)
        self.clearGUI()
        return True

    def __handleStartTraining(self, event):
        if not event.settingsID:
            LOG_ERROR('Name of tutorial is not defined', event.settingsID)
            return
        Waiting.show('tutorial-chapter-loading', isSingle=True)
        self.startTraining(event.settingsID, event.getState())
        Waiting.hide('tutorial-chapter-loading')

    def __handleStopTraining(self, _):
        self.stopTraining()
