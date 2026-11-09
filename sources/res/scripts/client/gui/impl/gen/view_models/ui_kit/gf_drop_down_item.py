# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/ui_kit/gf_drop_down_item.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/ui_kit/gf_drop_down_item.py
from frameworks.wulf import ViewModel

class GfDropDownItem(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(GfDropDownItem, self).__init__(properties=properties, commands=commands)

    def getId(self):
        return self._getString(0)

    def setId(self, value):
        self._setString(0, value)

    def getLabel(self):
        return self._getString(1)

    def setLabel(self, value):
        self._setString(1, value)

    def getIsDisabled(self):
        return self._getBool(2)

    def setIsDisabled(self, value):
        self._setBool(2, value)

    def _initialize(self):
        super(GfDropDownItem, self)._initialize()
        self._addStringProperty('id', '')
        self._addStringProperty('label', '')
        self._addBoolProperty('isDisabled', False)
