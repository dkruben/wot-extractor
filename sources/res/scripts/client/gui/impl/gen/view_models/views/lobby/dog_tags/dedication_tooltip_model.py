# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/dog_tags/dedication_tooltip_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/dog_tags/dedication_tooltip_model.py
from frameworks.wulf import Array, ViewModel
from gui.impl.gen import R

class DedicationTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(DedicationTooltipModel, self).__init__(properties=properties, commands=commands)

    def getCurrentGrade(self):
        return self._getNumber(0)

    def setCurrentGrade(self, value):
        self._setNumber(0, value)

    def getGradeValues(self):
        return self._getArray(1)

    def setGradeValues(self, value):
        self._setArray(1, value)

    def getComponentTitle(self):
        return self._getResource(2)

    def setComponentTitle(self, value):
        self._setResource(2, value)

    def getProgressNumberType(self):
        return self._getString(3)

    def setProgressNumberType(self, value):
        self._setString(3, value)

    def _initialize(self):
        super(DedicationTooltipModel, self)._initialize()
        self._addNumberProperty('currentGrade', 0)
        self._addArrayProperty('gradeValues', Array())
        self._addResourceProperty('componentTitle', R.invalid())
        self._addStringProperty('progressNumberType', '')
