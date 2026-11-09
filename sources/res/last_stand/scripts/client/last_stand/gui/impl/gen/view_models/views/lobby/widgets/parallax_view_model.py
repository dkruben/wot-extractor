# wot-extractor: codigo DESCOMPILADO de sources/res/last_stand/scripts/client/last_stand/gui/impl/gen/view_models/views/lobby/widgets/parallax_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: last_stand/scripts/client/last_stand/gui/impl/gen/view_models/views/lobby/widgets/parallax_view_model.py
from frameworks.wulf import ViewModel
from last_stand.gui.impl.gen.view_models.views.lobby.widgets.parallax_model import ParallaxModel

class ParallaxViewModel(ViewModel):
    __slots__ = ('onSlide', )

    def __init__(self, properties=2, commands=1):
        super(ParallaxViewModel, self).__init__(properties=properties, commands=commands)

    @property
    def parallax(self):
        return self._getViewModel(0)

    @staticmethod
    def getParallaxType():
        return ParallaxModel

    def getIsParallaxEnabled(self):
        return self._getBool(1)

    def setIsParallaxEnabled(self, value):
        self._setBool(1, value)

    def _initialize(self):
        super(ParallaxViewModel, self)._initialize()
        self._addViewModelProperty('parallax', ParallaxModel())
        self._addBoolProperty('isParallaxEnabled', False)
        self.onSlide = self._addCommand('onSlide')
