# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/common/base_intro_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/common/base_intro_view_model.py
from frameworks.wulf import Array, ViewModel
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.common.intro_slide_model import IntroSlideModel

class BaseIntroViewModel(ViewModel):
    __slots__ = ('onClose', 'onVideo', 'onViewLoaded')

    def __init__(self, properties=4, commands=3):
        super(BaseIntroViewModel, self).__init__(properties=properties, commands=commands)

    def getTitle(self):
        return self._getResource(0)

    def setTitle(self, value):
        self._setResource(0, value)

    def getAbout(self):
        return self._getResource(1)

    def setAbout(self, value):
        self._setResource(1, value)

    def getButtonLabel(self):
        return self._getResource(2)

    def setButtonLabel(self, value):
        self._setResource(2, value)

    def getSlides(self):
        return self._getArray(3)

    def setSlides(self, value):
        self._setArray(3, value)

    @staticmethod
    def getSlidesType():
        return IntroSlideModel

    def _initialize(self):
        super(BaseIntroViewModel, self)._initialize()
        self._addResourceProperty('title', R.invalid())
        self._addResourceProperty('about', R.invalid())
        self._addResourceProperty('buttonLabel', R.invalid())
        self._addArrayProperty('slides', Array())
        self.onClose = self._addCommand('onClose')
        self.onVideo = self._addCommand('onVideo')
        self.onViewLoaded = self._addCommand('onViewLoaded')
