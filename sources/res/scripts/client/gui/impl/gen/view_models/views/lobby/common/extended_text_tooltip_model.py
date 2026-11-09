# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/common/extended_text_tooltip_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/common/extended_text_tooltip_model.py
from frameworks.wulf import ViewModel

class ExtendedTextTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(ExtendedTextTooltipModel, self).__init__(properties=properties, commands=commands)

    def getText(self):
        return self._getString(0)

    def setText(self, value):
        self._setString(0, value)

    def getStringifyKwargs(self):
        return self._getString(1)

    def setStringifyKwargs(self, value):
        self._setString(1, value)

    def _initialize(self):
        super(ExtendedTextTooltipModel, self)._initialize()
        self._addStringProperty('text', '')
        self._addStringProperty('stringifyKwargs', '')
