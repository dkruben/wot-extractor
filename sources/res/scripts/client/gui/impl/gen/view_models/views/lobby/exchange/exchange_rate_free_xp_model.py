# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/exchange/exchange_rate_free_xp_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/exchange/exchange_rate_free_xp_model.py
from frameworks.wulf import Array
from gui.impl.gen.view_models.views.lobby.exchange.exchange_rate_base_model import ExchangeRateBaseModel
from gui.impl.gen.view_models.views.lobby.exchange.exchange_rate_vehicles_selection_model import ExchangeRateVehiclesSelectionModel

class ExchangeRateFreeXpModel(ExchangeRateBaseModel):
    __slots__ = ('onVehiclesSelected', )

    def __init__(self, properties=10, commands=5):
        super(ExchangeRateFreeXpModel, self).__init__(properties=properties, commands=commands)

    def getVehiclesSelection(self):
        return self._getArray(9)

    def setVehiclesSelection(self, value):
        self._setArray(9, value)

    @staticmethod
    def getVehiclesSelectionType():
        return ExchangeRateVehiclesSelectionModel

    def _initialize(self):
        super(ExchangeRateFreeXpModel, self)._initialize()
        self._addArrayProperty('vehiclesSelection', Array())
        self.onVehiclesSelected = self._addCommand('onVehiclesSelected')
