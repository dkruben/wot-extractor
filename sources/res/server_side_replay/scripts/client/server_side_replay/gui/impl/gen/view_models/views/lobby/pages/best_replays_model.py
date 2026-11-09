# wot-extractor: codigo DESCOMPILADO de sources/res/server_side_replay/scripts/client/server_side_replay/gui/impl/gen/view_models/views/lobby/pages/best_replays_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: server_side_replay/scripts/client/server_side_replay/gui/impl/gen/view_models/views/lobby/pages/best_replays_model.py
from frameworks.wulf import Array
from server_side_replay.gui.impl.gen.view_models.views.lobby.table_base_model import TableBaseModel
from server_side_replay.gui.impl.gen.view_models.views.lobby.top_replay_model import TopReplayModel

class BestReplaysModel(TableBaseModel):
    __slots__ = ('onLike', 'onTopReplaysWatch')

    def __init__(self, properties=8, commands=6):
        super(BestReplaysModel, self).__init__(properties=properties, commands=commands)

    def getTopReplays(self):
        return self._getArray(7)

    def setTopReplays(self, value):
        self._setArray(7, value)

    @staticmethod
    def getTopReplaysType():
        return TopReplayModel

    def _initialize(self):
        super(BestReplaysModel, self)._initialize()
        self._addArrayProperty('topReplays', Array())
        self.onLike = self._addCommand('onLike')
        self.onTopReplaysWatch = self._addCommand('onTopReplaysWatch')
