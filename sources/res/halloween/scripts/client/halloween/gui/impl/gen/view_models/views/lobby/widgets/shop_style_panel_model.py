# wot-extractor: codigo DESCOMPILADO de sources/res/halloween/scripts/client/halloween/gui/impl/gen/view_models/views/lobby/widgets/shop_style_panel_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: halloween/scripts/client/halloween/gui/impl/gen/view_models/views/lobby/widgets/shop_style_panel_model.py
from frameworks.wulf import ViewModel

class ShopStylePanelModel(ViewModel):
    __slots__ = ('onClick', )

    def __init__(self, properties=3, commands=1):
        super(ShopStylePanelModel, self).__init__(properties=properties, commands=commands)

    def getName(self):
        return self._getString(0)

    def setName(self, value):
        self._setString(0, value)

    def getTimer(self):
        return self._getNumber(1)

    def setTimer(self, value):
        self._setNumber(1, value)

    def getIsOwned(self):
        return self._getBool(2)

    def setIsOwned(self, value):
        self._setBool(2, value)

    def _initialize(self):
        super(ShopStylePanelModel, self)._initialize()
        self._addStringProperty('name', '')
        self._addNumberProperty('timer', 0)
        self._addBoolProperty('isOwned', False)
        self.onClick = self._addCommand('onClick')
