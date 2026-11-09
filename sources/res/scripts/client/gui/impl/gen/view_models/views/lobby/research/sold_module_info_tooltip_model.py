# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/research/sold_module_info_tooltip_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/research/sold_module_info_tooltip_model.py
from frameworks.wulf import Array, ViewModel

class SoldModuleInfoTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(SoldModuleInfoTooltipModel, self).__init__(properties=properties, commands=commands)

    def getCompatibleTanks(self):
        return self._getArray(0)

    def setCompatibleTanks(self, value):
        self._setArray(0, value)

    @staticmethod
    def getCompatibleTanksType():
        return unicode

    def _initialize(self):
        super(SoldModuleInfoTooltipModel, self)._initialize()
        self._addArrayProperty('compatibleTanks', Array())
