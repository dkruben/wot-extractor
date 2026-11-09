# wot-extractor: codigo DESCOMPILADO de sources/res/battle_royale/scripts/client/battle_royale/gui/impl/gen/view_models/views/lobby/views/battle_result_view/leaderboard_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/impl/gen/view_models/views/lobby/views/battle_result_view/leaderboard_model.py
from frameworks.wulf import Array, ViewModel
from battle_royale.gui.impl.gen.view_models.views.lobby.views.battle_result_view.place_model import PlaceModel

class LeaderboardModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(LeaderboardModel, self).__init__(properties=properties, commands=commands)

    def getPlacesList(self):
        return self._getArray(0)

    def setPlacesList(self, value):
        self._setArray(0, value)

    @staticmethod
    def getPlacesListType():
        return PlaceModel

    def _initialize(self):
        super(LeaderboardModel, self)._initialize()
        self._addArrayProperty('placesList', Array())
