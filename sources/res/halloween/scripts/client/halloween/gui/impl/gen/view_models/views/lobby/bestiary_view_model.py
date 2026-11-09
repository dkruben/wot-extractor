# wot-extractor: codigo DESCOMPILADO de sources/res/halloween/scripts/client/halloween/gui/impl/gen/view_models/views/lobby/bestiary_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: halloween/scripts/client/halloween/gui/impl/gen/view_models/views/lobby/bestiary_view_model.py
from frameworks.wulf import Array
from halloween.gui.impl.gen.view_models.views.lobby.enemy_model import EnemyModel
from gui.impl.gen.view_models.views.selectable_view_model import SelectableViewModel

class BestiaryViewModel(SelectableViewModel):
    __slots__ = ('onClose', 'onChangeEnemy', 'onResize')

    def __init__(self, properties=2, commands=5):
        super(BestiaryViewModel, self).__init__(properties=properties, commands=commands)

    def getSelectedIntCD(self):
        return self._getNumber(0)

    def setSelectedIntCD(self, value):
        self._setNumber(0, value)

    def getEnemies(self):
        return self._getArray(1)

    def setEnemies(self, value):
        self._setArray(1, value)

    @staticmethod
    def getEnemiesType():
        return EnemyModel

    def _initialize(self):
        super(BestiaryViewModel, self)._initialize()
        self._addNumberProperty('selectedIntCD', 0)
        self._addArrayProperty('enemies', Array())
        self.onClose = self._addCommand('onClose')
        self.onChangeEnemy = self._addCommand('onChangeEnemy')
        self.onResize = self._addCommand('onResize')
