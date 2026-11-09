# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/nation_change/nation_change_instruction_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/nation_change/nation_change_instruction_model.py
from frameworks.wulf import ViewModel
from gui.impl.gen import R

class NationChangeInstructionModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(NationChangeInstructionModel, self).__init__(properties=properties, commands=commands)

    def getImage(self):
        return self._getResource(0)

    def setImage(self, value):
        self._setResource(0, value)

    def getIsInstalled(self):
        return self._getBool(1)

    def setIsInstalled(self, value):
        self._setBool(1, value)

    def getIsActive(self):
        return self._getBool(2)

    def setIsActive(self, value):
        self._setBool(2, value)

    def getIsPerkReplace(self):
        return self._getBool(3)

    def setIsPerkReplace(self, value):
        self._setBool(3, value)

    def getIntCD(self):
        return self._getNumber(4)

    def setIntCD(self, value):
        self._setNumber(4, value)

    def getLayoutIDx(self):
        return self._getNumber(5)

    def setLayoutIDx(self, value):
        self._setNumber(5, value)

    def _initialize(self):
        super(NationChangeInstructionModel, self)._initialize()
        self._addResourceProperty('image', R.invalid())
        self._addBoolProperty('isInstalled', False)
        self._addBoolProperty('isActive', False)
        self._addBoolProperty('isPerkReplace', False)
        self._addNumberProperty('intCD', 0)
        self._addNumberProperty('layoutIDx', 0)
