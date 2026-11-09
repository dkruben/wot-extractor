# wot-extractor: codigo DESCOMPILADO de sources/res/comp7/scripts/client/comp7/gui/impl/gen/view_models/views/lobby/meta_view/pages/customization_tasks_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7/scripts/client/comp7/gui/impl/gen/view_models/views/lobby/meta_view/pages/customization_tasks_model.py
from frameworks.wulf import ViewModel

class CustomizationTasksModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=0):
        super(CustomizationTasksModel, self).__init__(properties=properties, commands=commands)

    def getIconKey(self):
        return self._getString(0)

    def setIconKey(self, value):
        self._setString(0, value)

    def getDescription(self):
        return self._getString(1)

    def setDescription(self, value):
        self._setString(1, value)

    def getCurrentProgress(self):
        return self._getNumber(2)

    def setCurrentProgress(self, value):
        self._setNumber(2, value)

    def getDelta(self):
        return self._getNumber(3)

    def setDelta(self, value):
        self._setNumber(3, value)

    def getMaxProgress(self):
        return self._getNumber(4)

    def setMaxProgress(self, value):
        self._setNumber(4, value)

    def getCustomizationId(self):
        return self._getNumber(5)

    def setCustomizationId(self, value):
        self._setNumber(5, value)

    def getProgressionLevel(self):
        return self._getNumber(6)

    def setProgressionLevel(self, value):
        self._setNumber(6, value)

    def _initialize(self):
        super(CustomizationTasksModel, self)._initialize()
        self._addStringProperty('iconKey', '')
        self._addStringProperty('description', '')
        self._addNumberProperty('currentProgress', 0)
        self._addNumberProperty('delta', 0)
        self._addNumberProperty('maxProgress', 0)
        self._addNumberProperty('customizationId', 0)
        self._addNumberProperty('progressionLevel', 0)
