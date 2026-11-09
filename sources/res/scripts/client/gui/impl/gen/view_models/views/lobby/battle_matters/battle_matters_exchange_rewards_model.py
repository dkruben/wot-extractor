# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/battle_matters/battle_matters_exchange_rewards_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/battle_matters/battle_matters_exchange_rewards_model.py
from frameworks.wulf import ViewModel

class BattleMattersExchangeRewardsModel(ViewModel):
    __slots__ = ('onConfirm', 'onClose')

    def __init__(self, properties=2, commands=2):
        super(BattleMattersExchangeRewardsModel, self).__init__(properties=properties, commands=commands)

    def getVehicleName(self):
        return self._getString(0)

    def setVehicleName(self, value):
        self._setString(0, value)

    def getVehicleUserName(self):
        return self._getString(1)

    def setVehicleUserName(self, value):
        self._setString(1, value)

    def _initialize(self):
        super(BattleMattersExchangeRewardsModel, self)._initialize()
        self._addStringProperty('vehicleName', '')
        self._addStringProperty('vehicleUserName', '')
        self.onConfirm = self._addCommand('onConfirm')
        self.onClose = self._addCommand('onClose')
