# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/pet_system/pet_house_marker_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/pet_system/pet_house_marker_model.py
from frameworks.wulf import ViewModel

class PetHouseMarkerModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(PetHouseMarkerModel, self).__init__(properties=properties, commands=commands)

    def getPetNameID(self):
        return self._getNumber(0)

    def setPetNameID(self, value):
        self._setNumber(0, value)

    def getHasUpdate(self):
        return self._getBool(1)

    def setHasUpdate(self, value):
        self._setBool(1, value)

    def getIsVisible(self):
        return self._getBool(2)

    def setIsVisible(self, value):
        self._setBool(2, value)

    def _initialize(self):
        super(PetHouseMarkerModel, self)._initialize()
        self._addNumberProperty('petNameID', 0)
        self._addBoolProperty('hasUpdate', False)
        self._addBoolProperty('isVisible', True)
