# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/ui_kit/gf_drop_down_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/ui_kit/gf_drop_down_model.py
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.ui_kit.gf_drop_down_item import GfDropDownItem

class GfDropDownModel(ViewModel):
    __slots__ = ('onChange', )

    def __init__(self, properties=3, commands=1):
        super(GfDropDownModel, self).__init__(properties=properties, commands=commands)

    def getItems(self):
        return self._getArray(0)

    def setItems(self, value):
        self._setArray(0, value)

    @staticmethod
    def getItemsType():
        return GfDropDownItem

    def getSelected(self):
        return self._getArray(1)

    def setSelected(self, value):
        self._setArray(1, value)

    @staticmethod
    def getSelectedType():
        return unicode

    def getMultiple(self):
        return self._getBool(2)

    def setMultiple(self, value):
        self._setBool(2, value)

    def _initialize(self):
        super(GfDropDownModel, self)._initialize()
        self._addArrayProperty('items', Array())
        self._addArrayProperty('selected', Array())
        self._addBoolProperty('multiple', False)
        self.onChange = self._addCommand('onChange')
