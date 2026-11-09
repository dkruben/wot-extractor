# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/crew/junk_tankmen_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/crew/junk_tankmen_view_model.py
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.crew.tankman_model import TankmanModel

class JunkTankmenViewModel(ViewModel):
    __slots__ = ('onLoadCards', 'onConfirm', 'onClose')

    def __init__(self, properties=3, commands=3):
        super(JunkTankmenViewModel, self).__init__(properties=properties, commands=commands)

    def getItemsAmount(self):
        return self._getNumber(0)

    def setItemsAmount(self, value):
        self._setNumber(0, value)

    def getItemsOffset(self):
        return self._getNumber(1)

    def setItemsOffset(self, value):
        self._setNumber(1, value)

    def getTankmanList(self):
        return self._getArray(2)

    def setTankmanList(self, value):
        self._setArray(2, value)

    @staticmethod
    def getTankmanListType():
        return TankmanModel

    def _initialize(self):
        super(JunkTankmenViewModel, self)._initialize()
        self._addNumberProperty('itemsAmount', 0)
        self._addNumberProperty('itemsOffset', 0)
        self._addArrayProperty('tankmanList', Array())
        self.onLoadCards = self._addCommand('onLoadCards')
        self.onConfirm = self._addCommand('onConfirm')
        self.onClose = self._addCommand('onClose')
