# wot-extractor: codigo DESCOMPILADO de sources/res/battle_royale/scripts/client/battle_royale/gui/impl/gen/view_models/views/lobby/views/game_mode_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/impl/gen/view_models/views/lobby/views/game_mode_model.py
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.battle_pass.game_mode_rows_model import GameModeRowsModel

class GameModeModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(GameModeModel, self).__init__(properties=properties, commands=commands)

    def getTableRows(self):
        return self._getArray(0)

    def setTableRows(self, value):
        self._setArray(0, value)

    @staticmethod
    def getTableRowsType():
        return GameModeRowsModel

    def _initialize(self):
        super(GameModeModel, self)._initialize()
        self._addArrayProperty('tableRows', Array())
