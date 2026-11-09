# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/ui_kit/button_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/ui_kit/button_model.py
from frameworks.wulf import ViewModel
from gui.impl.gen import R

class ButtonModel(ViewModel):
    __slots__ = ('onClicked', )

    def __init__(self, properties=5, commands=1):
        super(ButtonModel, self).__init__(properties=properties, commands=commands)

    def getRawLabel(self):
        return self._getString(0)

    def setRawLabel(self, value):
        self._setString(0, value)

    def getLabel(self):
        return self._getResource(1)

    def setLabel(self, value):
        self._setResource(1, value)

    def getIsEnabled(self):
        return self._getBool(2)

    def setIsEnabled(self, value):
        self._setBool(2, value)

    def getIcon(self):
        return self._getResource(3)

    def setIcon(self, value):
        self._setResource(3, value)

    def getIconAfterText(self):
        return self._getBool(4)

    def setIconAfterText(self, value):
        self._setBool(4, value)

    def _initialize(self):
        super(ButtonModel, self)._initialize()
        self._addStringProperty('rawLabel', '')
        self._addResourceProperty('label', R.invalid())
        self._addBoolProperty('isEnabled', True)
        self._addResourceProperty('icon', R.invalid())
        self._addBoolProperty('iconAfterText', True)
        self.onClicked = self._addCommand('onClicked')
