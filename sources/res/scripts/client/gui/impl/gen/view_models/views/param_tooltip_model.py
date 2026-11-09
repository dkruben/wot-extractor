# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/param_tooltip_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/param_tooltip_model.py
from frameworks.wulf import ViewModel

class ParamTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(ParamTooltipModel, self).__init__(properties=properties, commands=commands)

    def getType(self):
        return self._getString(0)

    def setType(self, value):
        self._setString(0, value)

    def getParams(self):
        return self._getString(1)

    def setParams(self, value):
        self._setString(1, value)

    def getResId(self):
        return self._getNumber(2)

    def setResId(self, value):
        self._setNumber(2, value)

    def _initialize(self):
        super(ParamTooltipModel, self)._initialize()
        self._addStringProperty('type', '')
        self._addStringProperty('params', '{}')
        self._addNumberProperty('resId', 0)
