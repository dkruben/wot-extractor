# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/training_room_external_handlers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/training_room_external_handlers.py
from __future__ import absolute_import
from gui.prb_control.events_dispatcher import g_eventDispatcher
from gui.shared.system_factory import collectTrainingRoomExternalHandlers

class TrainingRoomBaseHandler(object):

    def getArenaFilter(self):
        return

    def getArenaData(self):
        return

    def getAdditionalInfo(self):
        return

    def getIcon(self):
        return

    def getMaxPlayersInTeam(self):
        return

    def getObserverValidator(self):
        return

    def playerReadyHandler(self, result):
        if result:
            g_eventDispatcher.loadTrainingRoom()
        else:
            g_eventDispatcher.loadHangar()

    def getPrebattleLimits(self):
        return

    def getPrebattlePropertyChecker(self):
        return

    def getVehicleWatcherType(self):
        return

    def getClientMessageData(self, errorType=None):
        return

    def isEnabledForGuiTypeName(self, guiTypeName=None):
        return False


def getTrainingRoomHandler(guiType=None):
    handler = collectTrainingRoomExternalHandlers().get(guiType)
    if handler is not None:
        return handler()
    else:
        return TrainingRoomBaseHandler()


def getAllTrainingRoomHandlers():
    handlers = collectTrainingRoomExternalHandlers()
    return [handler() for handler in handlers.values()]
