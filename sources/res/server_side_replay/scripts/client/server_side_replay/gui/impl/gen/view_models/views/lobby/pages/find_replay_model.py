# wot-extractor: codigo DESCOMPILADO de sources/res/server_side_replay/scripts/client/server_side_replay/gui/impl/gen/view_models/views/lobby/pages/find_replay_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: server_side_replay/scripts/client/server_side_replay/gui/impl/gen/view_models/views/lobby/pages/find_replay_model.py
from server_side_replay.gui.impl.gen.view_models.views.lobby.table_base_model import TableBaseModel

class FindReplayModel(TableBaseModel):
    __slots__ = ('onFind', )

    def __init__(self, properties=7, commands=5):
        super(FindReplayModel, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(FindReplayModel, self)._initialize()
        self.onFind = self._addCommand('onFind')
