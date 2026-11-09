# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/battle_results/currency_group_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/battle_results/currency_group_model.py
from frameworks.wulf import Array, ViewModel
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.battle_results.currency_record_model import CurrencyRecordModel

class CurrencyGroupModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(CurrencyGroupModel, self).__init__(properties=properties, commands=commands)

    def getTitle(self):
        return self._getResource(0)

    def setTitle(self, value):
        self._setResource(0, value)

    def getRecords(self):
        return self._getArray(1)

    def setRecords(self, value):
        self._setArray(1, value)

    @staticmethod
    def getRecordsType():
        return CurrencyRecordModel

    def getUseSecondValues(self):
        return self._getBool(2)

    def setUseSecondValues(self, value):
        self._setBool(2, value)

    def _initialize(self):
        super(CurrencyGroupModel, self)._initialize()
        self._addResourceProperty('title', R.invalid())
        self._addArrayProperty('records', Array())
        self._addBoolProperty('useSecondValues', False)
