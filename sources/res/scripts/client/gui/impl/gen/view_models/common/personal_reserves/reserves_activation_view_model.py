# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/common/personal_reserves/reserves_activation_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/common/personal_reserves/reserves_activation_view_model.py
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.common.personal_reserves.reserves_group_model import ReservesGroupModel

class ReservesActivationViewModel(ViewModel):
    __slots__ = ('onNavigateToStore', 'onClose', 'onBoosterActivate', 'onNavigateToDepot',
                 'onCardHover')

    def __init__(self, properties=5, commands=5):
        super(ReservesActivationViewModel, self).__init__(properties=properties, commands=commands)

    def getReserveGroups(self):
        return self._getArray(0)

    def setReserveGroups(self, value):
        self._setArray(0, value)

    @staticmethod
    def getReserveGroupsType():
        return ReservesGroupModel

    def getGold(self):
        return self._getNumber(1)

    def setGold(self, value):
        self._setNumber(1, value)

    def getCanActivateClanReserves(self):
        return self._getBool(2)

    def setCanActivateClanReserves(self, value):
        self._setBool(2, value)

    def getNextExpirationTime(self):
        return self._getNumber(3)

    def setNextExpirationTime(self, value):
        self._setNumber(3, value)

    def getNextExpirationAmount(self):
        return self._getNumber(4)

    def setNextExpirationAmount(self, value):
        self._setNumber(4, value)

    def _initialize(self):
        super(ReservesActivationViewModel, self)._initialize()
        self._addArrayProperty('reserveGroups', Array())
        self._addNumberProperty('gold', 0)
        self._addBoolProperty('canActivateClanReserves', False)
        self._addNumberProperty('nextExpirationTime', 0)
        self._addNumberProperty('nextExpirationAmount', 0)
        self.onNavigateToStore = self._addCommand('onNavigateToStore')
        self.onClose = self._addCommand('onClose')
        self.onBoosterActivate = self._addCommand('onBoosterActivate')
        self.onNavigateToDepot = self._addCommand('onNavigateToDepot')
        self.onCardHover = self._addCommand('onCardHover')
