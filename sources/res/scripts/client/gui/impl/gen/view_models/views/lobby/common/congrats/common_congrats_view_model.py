# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/common/congrats/common_congrats_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/common/congrats/common_congrats_view_model.py
from frameworks.wulf import ViewModel
from gui.impl.gen import R

class CommonCongratsViewModel(ViewModel):
    __slots__ = ('onCloseClick', 'onConfirmClick', 'onBackClick')

    def __init__(self, properties=8, commands=3):
        super(CommonCongratsViewModel, self).__init__(properties=properties, commands=commands)

    def getBackground(self):
        return self._getResource(0)

    def setBackground(self, value):
        self._setResource(0, value)

    def getTitle(self):
        return self._getResource(1)

    def setTitle(self, value):
        self._setResource(1, value)

    def getDescription(self):
        return self._getString(2)

    def setDescription(self, value):
        self._setString(2, value)

    def getImage(self):
        return self._getString(3)

    def setImage(self, value):
        self._setString(3, value)

    def getImageAlt(self):
        return self._getString(4)

    def setImageAlt(self, value):
        self._setString(4, value)

    def getConfirmLbl(self):
        return self._getResource(5)

    def setConfirmLbl(self, value):
        self._setResource(5, value)

    def getBackLbl(self):
        return self._getResource(6)

    def setBackLbl(self, value):
        self._setResource(6, value)

    def getNeedReset(self):
        return self._getBool(7)

    def setNeedReset(self, value):
        self._setBool(7, value)

    def _initialize(self):
        super(CommonCongratsViewModel, self)._initialize()
        self._addResourceProperty('background', R.invalid())
        self._addResourceProperty('title', R.invalid())
        self._addStringProperty('description', '')
        self._addStringProperty('image', '')
        self._addStringProperty('imageAlt', '')
        self._addResourceProperty('confirmLbl', R.invalid())
        self._addResourceProperty('backLbl', R.invalid())
        self._addBoolProperty('needReset', False)
        self.onCloseClick = self._addCommand('onCloseClick')
        self.onConfirmClick = self._addCommand('onConfirmClick')
        self.onBackClick = self._addCommand('onBackClick')
