# wot-extractor: codigo DESCOMPILADO de sources/res/advent_calendar/scripts/client/advent_calendar/gui/impl/gen/view_models/views/lobby/marker_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: advent_calendar/scripts/client/advent_calendar/gui/impl/gen/view_models/views/lobby/marker_view_model.py
from frameworks.wulf import ViewModel

class MarkerViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(MarkerViewModel, self).__init__(properties=properties, commands=commands)

    def getAvailableDoorsAmount(self):
        return self._getNumber(0)

    def setAvailableDoorsAmount(self, value):
        self._setNumber(0, value)

    def getIsVisible(self):
        return self._getBool(1)

    def setIsVisible(self, value):
        self._setBool(1, value)

    def getIsPostEvent(self):
        return self._getBool(2)

    def setIsPostEvent(self, value):
        self._setBool(2, value)

    def getIsAnimationEnabled(self):
        return self._getBool(3)

    def setIsAnimationEnabled(self, value):
        self._setBool(3, value)

    def _initialize(self):
        super(MarkerViewModel, self)._initialize()
        self._addNumberProperty('availableDoorsAmount', 0)
        self._addBoolProperty('isVisible', True)
        self._addBoolProperty('isPostEvent', False)
        self._addBoolProperty('isAnimationEnabled', False)
