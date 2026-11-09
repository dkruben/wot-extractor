# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/battle/battle_page/tab_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/battle/battle_page/tab_view_model.py
from enum import Enum
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.battle.battle_page.personal_reserves_tab_view_model import PersonalReservesTabViewModel
from gui.impl.gen.view_models.views.battle.battle_page.player_list_model import PlayerListModel

class TabAlias(Enum):
    STATS = 'Stats'
    RESERVES = 'Reserves'


class TabViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(TabViewModel, self).__init__(properties=properties, commands=commands)

    @property
    def personalReserves(self):
        return self._getViewModel(0)

    @staticmethod
    def getPersonalReservesType():
        return PersonalReservesTabViewModel

    @property
    def playerList(self):
        return self._getViewModel(1)

    @staticmethod
    def getPlayerListType():
        return PlayerListModel

    def getTabSelection(self):
        return TabAlias(self._getString(2))

    def setTabSelection(self, value):
        self._setString(2, value.value)

    def getShowCommendationAnimations(self):
        return self._getBool(3)

    def setShowCommendationAnimations(self, value):
        self._setBool(3, value)

    def _initialize(self):
        super(TabViewModel, self)._initialize()
        self._addViewModelProperty('personalReserves', PersonalReservesTabViewModel())
        self._addViewModelProperty('playerList', PlayerListModel())
        self._addStringProperty('tabSelection')
        self._addBoolProperty('showCommendationAnimations', True)
