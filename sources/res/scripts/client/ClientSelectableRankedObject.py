# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/ClientSelectableRankedObject.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/ClientSelectableRankedObject.py
from __future__ import absolute_import
from ClientSelectableObject import ClientSelectableObject
from helpers import dependency
from skeletons.gui.game_control import IRankedBattlesController

class ClientSelectableRankedObject(ClientSelectableObject):
    __rankedController = dependency.descriptor(IRankedBattlesController)

    def onEnterWorld(self, prereqs):
        super(ClientSelectableRankedObject, self).onEnterWorld(prereqs)
        self.__rankedController.onGameModeStatusUpdated += self.__onGameModeStatusUpdate
        self.__onGameModeStatusUpdate()

    def onLeaveWorld(self):
        self.__rankedController.onGameModeStatusUpdated -= self.__onGameModeStatusUpdate
        super(ClientSelectableRankedObject, self).onLeaveWorld()

    def onMouseClick(self):
        super(ClientSelectableRankedObject, self).onMouseClick()
        self.__rankedController.doActionOnEntryPointClick()

    def __onGameModeStatusUpdate(self, *_):
        isEnabled = self.__rankedController.isEnabled()
        hasCurSeason = self.__rankedController.getCurrentSeason() is not None
        hasPrevSeason = self.__rankedController.getPreviousSeason() is not None
        if isEnabled and not hasCurSeason and not hasPrevSeason:
            self.setEnable(False)
        else:
            self.setEnable(True)
        return
