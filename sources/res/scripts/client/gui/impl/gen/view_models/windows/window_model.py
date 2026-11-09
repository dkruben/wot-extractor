# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/windows/window_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/windows/window_model.py
from frameworks.wulf import ViewModel
from gui.impl.gen import R

class WindowModel(ViewModel):
    __slots__ = ('onClosed', 'onMinimized')

    def __init__(self, properties=3, commands=2):
        super(WindowModel, self).__init__(properties=properties, commands=commands)

    def getTitle(self):
        return self._getResource(0)

    def setTitle(self, value):
        self._setResource(0, value)

    def getRawTitle(self):
        return self._getString(1)

    def setRawTitle(self, value):
        self._setString(1, value)

    def getCanMinimize(self):
        return self._getBool(2)

    def setCanMinimize(self, value):
        self._setBool(2, value)

    def _initialize(self):
        super(WindowModel, self)._initialize()
        self._addResourceProperty('title', R.invalid())
        self._addStringProperty('rawTitle', '')
        self._addBoolProperty('canMinimize', False)
        self.onClosed = self._addCommand('onClosed')
        self.onMinimized = self._addCommand('onMinimized')
