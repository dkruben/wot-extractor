# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/dog_tags/dt_grid_section.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/dog_tags/dt_grid_section.py
from frameworks.wulf import Array, ViewModel
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.dog_tags.dt_component import DtComponent

class DtGridSection(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(DtGridSection, self).__init__(properties=properties, commands=commands)

    def getTitle(self):
        return self._getResource(0)

    def setTitle(self, value):
        self._setResource(0, value)

    def getItems(self):
        return self._getArray(1)

    def setItems(self, value):
        self._setArray(1, value)

    @staticmethod
    def getItemsType():
        return DtComponent

    def getTooltipTitle(self):
        return self._getResource(2)

    def setTooltipTitle(self, value):
        self._setResource(2, value)

    def getTooltipDescription(self):
        return self._getResource(3)

    def setTooltipDescription(self, value):
        self._setResource(3, value)

    def _initialize(self):
        super(DtGridSection, self)._initialize()
        self._addResourceProperty('title', R.invalid())
        self._addArrayProperty('items', Array())
        self._addResourceProperty('tooltipTitle', R.invalid())
        self._addResourceProperty('tooltipDescription', R.invalid())
