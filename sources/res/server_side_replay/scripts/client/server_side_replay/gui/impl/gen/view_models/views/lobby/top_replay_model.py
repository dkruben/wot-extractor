# wot-extractor: codigo DESCOMPILADO de sources/res/server_side_replay/scripts/client/server_side_replay/gui/impl/gen/view_models/views/lobby/top_replay_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: server_side_replay/scripts/client/server_side_replay/gui/impl/gen/view_models/views/lobby/top_replay_model.py
from enum import Enum
from server_side_replay.gui.impl.gen.view_models.views.lobby.replay_model import ReplayModel

class StatParams(Enum):
    EARNEDXP = 'earnedXp'
    DAMAGEDEALT = 'damageDealt'
    DAMAGEASSISTED = 'damageAssisted'
    DAMAGEBLOCKEDBYARMOR = 'damageBlockedByArmor'
    KILLS = 'kills'
    MARKSOFMASTERY = 'marksOfMastery'
    DATE = 'date'


class TopReplayModel(ReplayModel):
    __slots__ = ()

    def __init__(self, properties=14, commands=0):
        super(TopReplayModel, self).__init__(properties=properties, commands=commands)

    def getParam(self):
        return StatParams(self._getString(13))

    def setParam(self, value):
        self._setString(13, value.value)

    def _initialize(self):
        super(TopReplayModel, self)._initialize()
        self._addStringProperty('param', StatParams.EARNEDXP.value)
