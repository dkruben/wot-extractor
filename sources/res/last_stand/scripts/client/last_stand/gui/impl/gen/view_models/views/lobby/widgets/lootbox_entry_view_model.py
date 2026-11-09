# wot-extractor: codigo DESCOMPILADO de sources/res/last_stand/scripts/client/last_stand/gui/impl/gen/view_models/views/lobby/widgets/lootbox_entry_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: last_stand/scripts/client/last_stand/gui/impl/gen/view_models/views/lobby/widgets/lootbox_entry_view_model.py
from frameworks.wulf import ViewModel

class LootboxEntryViewModel(ViewModel):
    __slots__ = ('onEntryClick', )

    def __init__(self, properties=2, commands=1):
        super(LootboxEntryViewModel, self).__init__(properties=properties, commands=commands)

    def getIsEnabled(self):
        return self._getBool(0)

    def setIsEnabled(self, value):
        self._setBool(0, value)

    def getBoxesCount(self):
        return self._getNumber(1)

    def setBoxesCount(self, value):
        self._setNumber(1, value)

    def _initialize(self):
        super(LootboxEntryViewModel, self)._initialize()
        self._addBoolProperty('isEnabled', False)
        self._addNumberProperty('boxesCount', 0)
        self.onEntryClick = self._addCommand('onEntryClick')
