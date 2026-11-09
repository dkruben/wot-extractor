# wot-extractor: codigo DESCOMPILADO de sources/res/open_bundle/scripts/client/open_bundle/gui/impl/gen/view_models/views/lobby/intro_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: open_bundle/scripts/client/open_bundle/gui/impl/gen/view_models/views/lobby/intro_view_model.py
from frameworks.wulf import ViewModel

class IntroViewModel(ViewModel):
    __slots__ = ('onClose', 'onExternalLink')

    def __init__(self, properties=2, commands=2):
        super(IntroViewModel, self).__init__(properties=properties, commands=commands)

    def getBundleType(self):
        return self._getString(0)

    def setBundleType(self, value):
        self._setString(0, value)

    def getTimeLeft(self):
        return self._getNumber(1)

    def setTimeLeft(self, value):
        self._setNumber(1, value)

    def _initialize(self):
        super(IntroViewModel, self)._initialize()
        self._addStringProperty('bundleType', '')
        self._addNumberProperty('timeLeft', 0)
        self.onClose = self._addCommand('onClose')
        self.onExternalLink = self._addCommand('onExternalLink')
