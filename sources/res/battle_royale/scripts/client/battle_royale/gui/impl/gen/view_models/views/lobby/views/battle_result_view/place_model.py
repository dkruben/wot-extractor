# wot-extractor: codigo DESCOMPILADO de sources/res/battle_royale/scripts/client/battle_royale/gui/impl/gen/view_models/views/lobby/views/battle_result_view/place_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/impl/gen/view_models/views/lobby/views/battle_result_view/place_model.py
from frameworks.wulf import Array, ViewModel
from battle_royale.gui.impl.gen.view_models.views.lobby.views.battle_result_view.row_model import RowModel

class PlaceModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(PlaceModel, self).__init__(properties=properties, commands=commands)

    def getPlace(self):
        return self._getString(0)

    def setPlace(self, value):
        self._setString(0, value)

    def getIsSquadMode(self):
        return self._getBool(1)

    def setIsSquadMode(self, value):
        self._setBool(1, value)

    def getPlayersList(self):
        return self._getArray(2)

    def setPlayersList(self, value):
        self._setArray(2, value)

    @staticmethod
    def getPlayersListType():
        return RowModel

    def _initialize(self):
        super(PlaceModel, self)._initialize()
        self._addStringProperty('place', '')
        self._addBoolProperty('isSquadMode', False)
        self._addArrayProperty('playersList', Array())
