# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/browser_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/browser_view_model.py
from gui.impl.gen.view_models.common.browser_model import BrowserModel

class BrowserViewModel(BrowserModel):
    __slots__ = ('onClose', )

    def __init__(self, properties=8, commands=5):
        super(BrowserViewModel, self).__init__(properties=properties, commands=commands)

    def getIsClosable(self):
        return self._getBool(7)

    def setIsClosable(self, value):
        self._setBool(7, value)

    def _initialize(self):
        super(BrowserViewModel, self)._initialize()
        self._addBoolProperty('isClosable', False)
        self.onClose = self._addCommand('onClose')
