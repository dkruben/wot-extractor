# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/battle/battle_page/personal_reserves_tab_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/battle/battle_page/personal_reserves_tab_view_model.py
from enum import IntEnum
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.common.personal_reserves.reserves_group_model import ReservesGroupModel

class TabAlias(IntEnum):
    STATS = 0
    RESERVES = 1


class PersonalReservesTabViewModel(ViewModel):
    __slots__ = ('onBoosterActivate', )

    def __init__(self, properties=2, commands=1):
        super(PersonalReservesTabViewModel, self).__init__(properties=properties, commands=commands)

    def getReserveGroups(self):
        return self._getArray(0)

    def setReserveGroups(self, value):
        self._setArray(0, value)

    @staticmethod
    def getReserveGroupsType():
        return ReservesGroupModel

    def getTabSelection(self):
        return TabAlias(self._getNumber(1))

    def setTabSelection(self, value):
        self._setNumber(1, value.value)

    def _initialize(self):
        super(PersonalReservesTabViewModel, self)._initialize()
        self._addArrayProperty('reserveGroups', Array())
        self._addNumberProperty('tabSelection')
        self.onBoosterActivate = self._addCommand('onBoosterActivate')
