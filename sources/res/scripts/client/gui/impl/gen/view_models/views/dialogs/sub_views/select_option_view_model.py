# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/dialogs/sub_views/select_option_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/dialogs/sub_views/select_option_view_model.py
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.dialogs.sub_views.select_option_base_item_view_model import SelectOptionBaseItemViewModel

class SelectOptionViewModel(ViewModel):
    __slots__ = ('onClicked', )

    def __init__(self, properties=3, commands=1):
        super(SelectOptionViewModel, self).__init__(properties=properties, commands=commands)

    def getItems(self):
        return self._getArray(0)

    def setItems(self, value):
        self._setArray(0, value)

    @staticmethod
    def getItemsType():
        return SelectOptionBaseItemViewModel

    def getSelectedIndexes(self):
        return self._getArray(1)

    def setSelectedIndexes(self, value):
        self._setArray(1, value)

    @staticmethod
    def getSelectedIndexesType():
        return int

    def getMessage(self):
        return self._getString(2)

    def setMessage(self, value):
        self._setString(2, value)

    def _initialize(self):
        super(SelectOptionViewModel, self)._initialize()
        self._addArrayProperty('items', Array())
        self._addArrayProperty('selectedIndexes', Array())
        self._addStringProperty('message', '')
        self.onClicked = self._addCommand('onClicked')
