# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/mapbox/map_box_answers_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/mapbox/map_box_answers_model.py
from frameworks.wulf import Array, ViewModel

class MapBoxAnswersModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(MapBoxAnswersModel, self).__init__(properties=properties, commands=commands)

    def getIsMultipleChoice(self):
        return self._getBool(0)

    def setIsMultipleChoice(self, value):
        self._setBool(0, value)

    def getVariants(self):
        return self._getArray(1)

    def setVariants(self, value):
        self._setArray(1, value)

    @staticmethod
    def getVariantsType():
        return unicode

    def getSelectedVariants(self):
        return self._getArray(2)

    def setSelectedVariants(self, value):
        self._setArray(2, value)

    @staticmethod
    def getSelectedVariantsType():
        return unicode

    def _initialize(self):
        super(MapBoxAnswersModel, self)._initialize()
        self._addBoolProperty('isMultipleChoice', False)
        self._addArrayProperty('variants', Array())
        self._addArrayProperty('selectedVariants', Array())
