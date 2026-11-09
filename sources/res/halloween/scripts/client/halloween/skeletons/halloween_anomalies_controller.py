# wot-extractor: codigo DESCOMPILADO de sources/res/halloween/scripts/client/halloween/skeletons/halloween_anomalies_controller.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: halloween/scripts/client/halloween/skeletons/halloween_anomalies_controller.py
from __future__ import absolute_import
import typing
from skeletons.gui.game_control import IGameController
if typing.TYPE_CHECKING:
    from collections import OrderedDict
    from Event import Event
    from typing import List, Optional
    from halloween.gui.game_control.halloween_anomalies_controller import AnomalyData, RecipeData

class IHalloweenAnomaliesController(IGameController):
    onRefreshData = None
    onChangeSystemAnomaliesUnlock = None

    @property
    def anomalies(self):
        raise NotImplementedError

    @property
    def lootAnomalies(self):
        raise NotImplementedError

    @property
    def recipes(self):
        raise NotImplementedError

    def getAnomalyByID(self, anomalyID):
        raise NotImplementedError
