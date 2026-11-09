# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/crew/tooltips/qualification_tooltip_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/crew/tooltips/qualification_tooltip_view_model.py
from frameworks.wulf import ViewModel

class QualificationTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(QualificationTooltipViewModel, self).__init__(properties=properties, commands=commands)

    def getRoleName(self):
        return self._getString(0)

    def setRoleName(self, value):
        self._setString(0, value)

    def getQualificationIndex(self):
        return self._getNumber(1)

    def setQualificationIndex(self, value):
        self._setNumber(1, value)

    def getIsFemale(self):
        return self._getBool(2)

    def setIsFemale(self, value):
        self._setBool(2, value)

    def getIsBonusQualification(self):
        return self._getBool(3)

    def setIsBonusQualification(self, value):
        self._setBool(3, value)

    def _initialize(self):
        super(QualificationTooltipViewModel, self)._initialize()
        self._addStringProperty('roleName', '')
        self._addNumberProperty('qualificationIndex', 0)
        self._addBoolProperty('isFemale', False)
        self._addBoolProperty('isBonusQualification', False)
