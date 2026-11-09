# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/battle_pass/tankmen_voiceover_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/battle_pass/tankmen_voiceover_view_model.py
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.battle_pass.tankman_model import TankmanModel

class TankmenVoiceoverViewModel(ViewModel):
    __slots__ = ('showShop', 'close')

    def __init__(self, properties=2, commands=2):
        super(TankmenVoiceoverViewModel, self).__init__(properties=properties, commands=commands)

    def getScreenID(self):
        return self._getNumber(0)

    def setScreenID(self, value):
        self._setNumber(0, value)

    def getTankmen(self):
        return self._getArray(1)

    def setTankmen(self, value):
        self._setArray(1, value)

    @staticmethod
    def getTankmenType():
        return TankmanModel

    def _initialize(self):
        super(TankmenVoiceoverViewModel, self)._initialize()
        self._addNumberProperty('screenID', 0)
        self._addArrayProperty('tankmen', Array())
        self.showShop = self._addCommand('showShop')
        self.close = self._addCommand('close')
