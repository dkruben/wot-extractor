# wot-extractor: codigo DESCOMPILADO de sources/res/halloween/scripts/client/halloween/gui/impl/gen/view_models/views/lobby/widgets/difficulty_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: halloween/scripts/client/halloween/gui/impl/gen/view_models/views/lobby/widgets/difficulty_view_model.py
from frameworks.wulf import Array, ViewModel
from halloween.gui.impl.gen.view_models.views.lobby.widgets.difficulty_item_model import DifficultyItemModel

class DifficultyViewModel(ViewModel):
    __slots__ = ('onSwichLevel', )

    def __init__(self, properties=2, commands=1):
        super(DifficultyViewModel, self).__init__(properties=properties, commands=commands)

    def getDifficulties(self):
        return self._getArray(0)

    def setDifficulties(self, value):
        self._setArray(0, value)

    @staticmethod
    def getDifficultiesType():
        return DifficultyItemModel

    def getIsDisabled(self):
        return self._getBool(1)

    def setIsDisabled(self, value):
        self._setBool(1, value)

    def _initialize(self):
        super(DifficultyViewModel, self)._initialize()
        self._addArrayProperty('difficulties', Array())
        self._addBoolProperty('isDisabled', False)
        self.onSwichLevel = self._addCommand('onSwichLevel')
