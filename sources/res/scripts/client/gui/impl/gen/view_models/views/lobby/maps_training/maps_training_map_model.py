# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/maps_training/maps_training_map_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/maps_training/maps_training_map_model.py
from frameworks.wulf import ViewModel
from gui.impl.gen import R

class MapsTrainingMapModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(MapsTrainingMapModel, self).__init__(properties=properties, commands=commands)

    def getId(self):
        return self._getString(0)

    def setId(self, value):
        self._setString(0, value)

    def getTitle(self):
        return self._getResource(1)

    def setTitle(self, value):
        self._setResource(1, value)

    def getImage(self):
        return self._getResource(2)

    def setImage(self, value):
        self._setResource(2, value)

    def getIsEnabled(self):
        return self._getBool(3)

    def setIsEnabled(self, value):
        self._setBool(3, value)

    def getIsCompleted(self):
        return self._getBool(4)

    def setIsCompleted(self, value):
        self._setBool(4, value)

    def getGroupId(self):
        return self._getNumber(5)

    def setGroupId(self, value):
        self._setNumber(5, value)

    def _initialize(self):
        super(MapsTrainingMapModel, self)._initialize()
        self._addStringProperty('id', '')
        self._addResourceProperty('title', R.invalid())
        self._addResourceProperty('image', R.invalid())
        self._addBoolProperty('isEnabled', False)
        self._addBoolProperty('isCompleted', False)
        self._addNumberProperty('groupId', 0)
