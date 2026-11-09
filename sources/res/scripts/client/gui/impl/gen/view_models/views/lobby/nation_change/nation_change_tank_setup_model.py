# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/nation_change/nation_change_tank_setup_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/nation_change/nation_change_tank_setup_model.py
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.nation_change.nation_change_instruction_model import NationChangeInstructionModel

class NationChangeTankSetupModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(NationChangeTankSetupModel, self).__init__(properties=properties, commands=commands)

    @property
    def instructionSlot(self):
        return self._getViewModel(0)

    @staticmethod
    def getInstructionSlotType():
        return NationChangeInstructionModel

    def getEquipmentList(self):
        return self._getArray(1)

    def setEquipmentList(self, value):
        self._setArray(1, value)

    def getShellList(self):
        return self._getArray(2)

    def setShellList(self, value):
        self._setArray(2, value)

    def getSupplyList(self):
        return self._getArray(3)

    def setSupplyList(self, value):
        self._setArray(3, value)

    def _initialize(self):
        super(NationChangeTankSetupModel, self)._initialize()
        self._addViewModelProperty('instructionSlot', NationChangeInstructionModel())
        self._addArrayProperty('equipmentList', Array())
        self._addArrayProperty('shellList', Array())
        self._addArrayProperty('supplyList', Array())
