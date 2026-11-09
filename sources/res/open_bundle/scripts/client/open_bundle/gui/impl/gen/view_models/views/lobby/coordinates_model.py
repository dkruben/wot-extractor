# wot-extractor: codigo DESCOMPILADO de sources/res/open_bundle/scripts/client/open_bundle/gui/impl/gen/view_models/views/lobby/coordinates_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: open_bundle/scripts/client/open_bundle/gui/impl/gen/view_models/views/lobby/coordinates_model.py
from frameworks.wulf import ViewModel
from open_bundle.gui.impl.gen.view_models.views.lobby.coordinate_model import CoordinateModel

class CoordinatesModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(CoordinatesModel, self).__init__(properties=properties, commands=commands)

    @property
    def start(self):
        return self._getViewModel(0)

    @staticmethod
    def getStartType():
        return CoordinateModel

    @property
    def end(self):
        return self._getViewModel(1)

    @staticmethod
    def getEndType():
        return CoordinateModel

    def _initialize(self):
        super(CoordinatesModel, self)._initialize()
        self._addViewModelProperty('start', CoordinateModel())
        self._addViewModelProperty('end', CoordinateModel())
