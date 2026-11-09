# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/crew/help_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/crew/help_view_model.py
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.crew.help_slide_view_model import HelpSlideViewModel

class HelpViewModel(ViewModel):
    __slots__ = ('onClose', )

    def __init__(self, properties=2, commands=1):
        super(HelpViewModel, self).__init__(properties=properties, commands=commands)

    def getSelectedSlideIndex(self):
        return self._getNumber(0)

    def setSelectedSlideIndex(self, value):
        self._setNumber(0, value)

    def getSlides(self):
        return self._getArray(1)

    def setSlides(self, value):
        self._setArray(1, value)

    @staticmethod
    def getSlidesType():
        return HelpSlideViewModel

    def _initialize(self):
        super(HelpViewModel, self)._initialize()
        self._addNumberProperty('selectedSlideIndex', 0)
        self._addArrayProperty('slides', Array())
        self.onClose = self._addCommand('onClose')
