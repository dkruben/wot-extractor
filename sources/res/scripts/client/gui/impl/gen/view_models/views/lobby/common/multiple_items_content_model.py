# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/common/multiple_items_content_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/common/multiple_items_content_model.py
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.common.confirmed_item_model import ConfirmedItemModel

class MultipleItemsContentModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(MultipleItemsContentModel, self).__init__(properties=properties, commands=commands)

    def getConfirmedItems(self):
        return self._getArray(0)

    def setConfirmedItems(self, value):
        self._setArray(0, value)

    @staticmethod
    def getConfirmedItemsType():
        return ConfirmedItemModel

    def getItemsType(self):
        return self._getString(1)

    def setItemsType(self, value):
        self._setString(1, value)

    def _initialize(self):
        super(MultipleItemsContentModel, self)._initialize()
        self._addArrayProperty('confirmedItems', Array())
        self._addStringProperty('itemsType', '')
