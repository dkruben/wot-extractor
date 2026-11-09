# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/battle_pass/battle_royale_conditions_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/battle_pass/battle_royale_conditions_model.py
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.battle_pass.game_mode_rows_model import GameModeRowsModel

class BattleRoyaleConditionsModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(BattleRoyaleConditionsModel, self).__init__(properties=properties, commands=commands)

    def getSolo(self):
        return self._getArray(0)

    def setSolo(self, value):
        self._setArray(0, value)

    @staticmethod
    def getSoloType():
        return GameModeRowsModel

    def getSquad(self):
        return self._getArray(1)

    def setSquad(self, value):
        self._setArray(1, value)

    @staticmethod
    def getSquadType():
        return GameModeRowsModel

    def _initialize(self):
        super(BattleRoyaleConditionsModel, self)._initialize()
        self._addArrayProperty('solo', Array())
        self._addArrayProperty('squad', Array())
