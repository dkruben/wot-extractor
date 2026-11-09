# wot-extractor: codigo DESCOMPILADO de sources/res/battle_royale/scripts/client/battle_royale/skeletons/game_controller.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: battle_royale/scripts/client/battle_royale/skeletons/game_controller.py
from __future__ import absolute_import
import typing
from skeletons.gui.game_control import IGameController
if typing.TYPE_CHECKING:
    from typing import Dict
    from Event import Event

class IBRProgressionOnTokensController(IGameController):
    progressionToken = ''
    PROGRESSION_COMPLETE_TOKEN = ''
    onProgressPointsUpdated = None
    onSettingsChanged = None

    @property
    def isEnabled(self):
        raise NotImplementedError

    @property
    def isFinished(self):
        raise NotImplementedError

    def init(self):
        raise NotImplementedError

    def fini(self):
        raise NotImplementedError

    def setSettings(self, settings):
        raise NotImplementedError

    def saveCurPoints(self):
        raise NotImplementedError

    def getPrevPoints(self):
        raise NotImplementedError

    def getCurPoints(self):
        raise NotImplementedError

    def getProgessionPointsData(self):
        raise NotImplementedError

    def getProgressionData(self):
        raise NotImplementedError
